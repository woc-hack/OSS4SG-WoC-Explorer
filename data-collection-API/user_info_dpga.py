
import requests
import pandas as pd
import time
# Load data
df = pd.read_csv('project_all.csv')

# Define the function to get repository descriptions
def get_repo_description(repo):
    url = f"https://api.github.com/repos/{repo}"
    token = 'ghp_' #replace with yours
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    time.sleep(1)
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        return data.get('description', '')
    else:
        return '' 


df['description'] = ''

# Iterate over each row using iterrows() which is suitable for this operation
for index, row in df.iterrows():
    repo = row['project_clean']
    description = get_repo_description(repo)
    df.at[index, 'description'] = description

# Save the updated DataFrame to a new CSV file
df.to_csv('project_all_description.csv', index=False)

