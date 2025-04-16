import json
import os
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import random

# Directory where your JSON files are stored
json_dir = r"C:\Users\passc\Projects\lalller_league\runs\test"

# Get a list of all the JSON files in the directory
json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]

# Function to load JSON data from a file
def load_json(file):
    with open(file, 'r') as f:
        return json.load(f)

# Function to plot data
def plot_data(data):
    figures = []

    for label, d in data.items():
        if isinstance(d, dict):
            fig, ax = plt.subplots()
            keys = list(d.keys())
            values = list(d.values())
            ax.plot(keys, values, marker='o')
            ax.set_title(f'JSON Data Plot - {label}')
            ax.set_xlabel('Key')
            ax.set_ylabel('Value')
            figures.append(fig)
    return figures
# Tkinter application class
class JSONViewerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("JSON Viewer")

        # Initial index to select a JSON
        self.index = 0
        self.total_jsons = len(json_files)

        # Frame for the plot
        self.frame = ttk.Frame(self.root)
        self.frame.pack()

        # Navigation buttons
        self.prev_button = ttk.Button(self.root, text="Previous", command=self.prev_json)
        self.prev_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.next_button = ttk.Button(self.root, text="Next", command=self.next_json)
        self.next_button.pack(side=tk.LEFT, padx=10, pady=10)

        # Plot canvas
        self.canvas = None

        # Show the first JSON data
        self.show_json_plot()

    # Function to display the plot for the current JSON
    def show_json_plot(self):
        json_file = os.path.join(json_dir, json_files[self.index])
        data = load_json(json_file)

        # Remove old plots
        for widget in self.frame.winfo_children():
            widget.destroy()

        # Create the plots
        figs = plot_data(data)

        # Add each figure to the Tkinter window
        for fig in figs:
            canvas = FigureCanvasTkAgg(fig, master=self.frame)
            canvas.draw()
            canvas.get_tk_widget().pack()

       
    # Function to navigate to the next JSON
    def next_json(self):
        self.index = (self.index + 1) % self.total_jsons  # Wrap around
        self.show_json_plot()

    # Function to navigate to the previous JSON
    def prev_json(self):
        self.index = (self.index - 1) % self.total_jsons  # Wrap around
        self.show_json_plot()

# Initialize the tkinter root window

def on_close():
    root.quit()  # This ensures the application exits

root = tk.Tk()
root.protocol("WM_DELETE_WINDOW", on_close)  # Close the window correctly
app = JSONViewerApp(root)
root.mainloop()