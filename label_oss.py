import tkinter as tk
from tkinter import ttk, messagebox
import pandas as pd
import webbrowser

def load_data(file_path):
    return pd.read_csv(file_path, encoding='ISO-8859-1')

def save_data(repo_data, file_path):
    repo_data.to_csv(file_path, index=False)

def create_widgets(frame, repo_data, index):
    # Clear the frame
    for widget in frame.winfo_children():
        widget.destroy()

    # Get the current repository entry
    repo = repo_data.iloc[index]

    # Display the current index
    ttk.Label(frame, text=f"Editing Entry: {index + 1} of {len(repo_data)}").grid(row=0, column=0, columnspan=2, sticky=tk.W)

    # Display repository information
    ttk.Label(frame, text="Repository Name:").grid(row=1, column=0, sticky=tk.W)
    ttk.Label(frame, text=repo["repo_name"]).grid(row=1, column=1, sticky=tk.W)

    ttk.Label(frame, text="Description:").grid(row=2, column=0, sticky=tk.W)
    ttk.Label(frame, text=repo["repo_description"]).grid(row=2, column=1, sticky=tk.W)

    ttk.Label(frame, text="URL:").grid(row=3, column=0, sticky=tk.W)
    url_label = ttk.Label(frame, text=repo["URL"], foreground="blue", cursor="hand2")
    url_label.grid(row=3, column=1, sticky=tk.W)
    url_label.bind("<Button-1>", lambda e: webbrowser.open_new(repo["URL"]))

    ttk.Label(frame, text="Select a Label:").grid(row=4, column=0, sticky=tk.W)

    def save_and_next(option):
        # Save the selected option
        repo_data.at[index, "manual"] = option
        save_data(repo_data, file_path)

        # Move to the next entry
        if index + 1 < len(repo_data):
            create_widgets(frame, repo_data, index + 1)
        else:
            messagebox.showinfo("Info", "All entries have been labeled. Data saved.")

    # Create buttons for each option
    row_num = 5
    col_num = 0
    for option in options:
        button = ttk.Button(frame, text=option, command=lambda opt=option: save_and_next(opt))
        button.grid(row=row_num, column=col_num, sticky=tk.W, padx=5, pady=5)
        col_num += 1
        if col_num > 2:
            col_num = 0
            row_num += 1

def main(start_index):
    # Load the CSV file
    global file_path
    file_path = 'sg_2.csv'
    repo_data = load_data(file_path)

    # Initialize the main application window
    root = tk.Tk()
    root.title("Repository Labeling Tool")

    # Create a frame to hold the widgets
    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    # Start with the given repository entry
    create_widgets(frame, repo_data, start_index)

    # Start the Tkinter event loop
    root.mainloop()

if __name__ == "__main__":
    options = [
        "no-poverty", "zero-hunger", "good-health", "quality-education", "gender-equality",
        "clean-water", "affordable-clean-energy", "decent-work-economic-growth",
        "industry-innovation-infrastructure", "reduced-inequality", "sustainable-cities",
        "responsible-consumption-production", "climate-change", "life-below-water", "life-on-land",
        "peace-and-justice", "strengthen-partnerships", "not-social-good"
    ]

    start_index = int(input("Enter the start index: "))
    main(start_index)