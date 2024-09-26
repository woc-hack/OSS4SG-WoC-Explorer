# Description

We provide scripts designed to facilitate the exploration of Open Source Software for Social Good (OSS4SG) projects on GitHub using the WoC. The objective is to streamline the process of mining OSS4SG data through the use of WoC, enhancing accessibility and efficiency in the analysis of these projects.

- data-collection-script/commit_dpga.py: use user index provided by WoC to collect users' commit history through oscar.py API

- lable.oss.py is the labeling code to categorize reporitory into different OSS themes. This Python code creates a GUI tool using the Tkinter library to label repository data stored in a CSV file. It loads the data, displays repository details such as name, description, and URL, and allows the user to select a label from predefined options for each repository. After the user selects a label, it saves the selection and moves to the next entry. The process continues until all entries are labeled. The URL is clickable, opening the repository in a browser. Users can start from a specific index, and the labeled data is saved back to the CSV file. 
