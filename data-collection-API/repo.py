import requests
import time
import random
import argparse
import pandas as pd
from tqdm import tqdm
import os

# Set up argument parsing
parser = argparse.ArgumentParser()
parser.add_argument('--start', required=True, type=int, help='Starting index for processing repositories')
args = parser.parse_args()
start = int(args.start)

# Load the list of repository names from a CSV file
repo_list = pd.read_csv('project_all.csv')['project_clean'].tolist()
result_file = "repo_descriptions.csv"
process_file = "process.csv"

# Initialize result DataFrame
if os.path.exists(result_file):
    df_result = pd.read_csv(result_file)
else:
    df_result = pd.DataFrame(columns=['repo_name', 'repo_description'])

# Initialize process DataFrame
if os.path.exists(process_file):
    df_process = pd.read_csv(process_file)
else:
    df_process = pd.DataFrame(columns=['last_processed_index'])

# Set GitHub API tokens - replace with yours
token_list = [
    "ghp_",
    "ghp_",
    "ghp_",
    "ghp_",
    "ghp_"
]

headers = {"Authorization": "token " + random.choice(token_list)}

# Process repositories
for i in tqdm(range(start, len(repo_list))):
    repo_name = repo_list[i]
    url = f"https://api.github.com/repos/{repo_name}"
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        repo_description = data.get('description', '')
        
        df_result.loc[len(df_result)] = [repo_name, repo_description]
        df_result.to_csv(result_file, index=False)
        
        df_process.loc[0, 'last_processed_index'] = i + 1
        df_process.to_csv(process_file, index=False)
        
        time.sleep(1)  # Pause to avoid hitting the rate limit
    else:
        rate_limit_remaining = int(response.headers.get("X-RateLimit-Remaining", 0))
        if rate_limit_remaining == 0:
            rate_limit_reset = int(response.headers["X-RateLimit-Reset"])
            wait_time = rate_limit_reset - time.time()
            print(f"Rate limit exceeded. Waiting {wait_time} seconds until rate limit resets.")
            if wait_time > 0:
                time.sleep(wait_time)
        else:
            print(f"Failed to fetch data for {repo_name}. Status code: {response.status_code}")

print("Processing complete.")
