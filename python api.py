import requests
import tkinter as tk
from tkinter import messagebox

# ... (rest of the code)

def fetch_data():
  global data, citations
  try:
    api_url = url_entry.get()
    data = fetch_all_pages(api_url)
    citations = identify_citations(data)
    display_results()
  except Exception as e:
    messagebox.showerror("Error", f"An error occurred: {e}")

def display_results():
  text_box.delete("1.0", tk.END)
  for item, citation_list in zip(data, citations):
    text_box.insert(tk.END, f"Response Text: {item['response_text']}\n")
    text_box.insert(tk.END, f"Citations: {citation_list}\n\n")

# Creating the main window and UI elements
root = tk.Tk()
root.title("Citation Finder")

url_label = tk.Label(root, text="API URL:")
url_label.pack()

url_entry = tk.Entry(root)
url_entry.pack()

fetch_button = tk.Button(root, text="Fetch Data", command=fetch_data)
fetch_button.pack()

text_box = tk.Text(root)
text_box.pack()

def fetch_all_pages(url):
  """Fetches data from all paginated API pages.

  Args:
    url: The base URL of the paginated API.

  Returns:
    A list containing all data objects retrieved from all API pages.
  """
  # ... (rest of the fetch_all_pages function)

def identify_citations(data):
  """Identifies citations (source of response) for each response-sources pair.

  Args:
    data: A list of data objects retrieved from the API.

  Returns:
    A list containing citations (source of response) for each data object.
  """
  # ... (rest of the identify_citations function)

def main():
  """Fetches data, identifies citations, and prints the results."""
  # ... (This function is empty as the data fetching is handled by fetch_data)

if __name__ == "__main__":
  main()
  root.mainloop()  # Call fetch_data at the end of mainloop
