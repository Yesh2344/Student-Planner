import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import csv
import os
import threading
import time

# Function to add task
def add_task():
    task_name = task_entry.get()
    due_date = due_entry.get()
    category = category_combobox.get()

    try:
        due_date_obj = datetime.datetime.strptime(due_date, '%Y-%m-%d')
        tasks.append({'name': task_name, 'due': due_date_obj, 'category': category, 'completed': False})
        update_task_list()
        task_entry.delete(0, tk.END)
        due_entry.delete(0, tk.END)
        category_combobox.set('Select Category')
    except ValueError:
        messagebox.showerror("Invalid Date", "Please enter date in YYYY-MM-DD format")

# Function to update the task list
def update_task_list():
    task_listbox.delete(0, tk.END)
    today = datetime.datetime.now()
    for task in tasks:
        task_str = f"{task['name']} - Due: {task['due'].strftime('%Y-%m-%d')} - Category: {task['category']}"
        if task['due'] < today:
            task_str += " (Overdue!)"
        task_listbox.insert(tk.END, task_str)

# Function to mark task as completed
def complete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks.pop(selected_task[0])
        update_task_list()

# Function to export tasks to a CSV file
def export_to_csv():
    with open('tasks.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'due', 'category', 'completed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({'name': task['name'], 'due': task['due'].strftime('%Y-%m-%d'), 'category': task['category'], 'completed': task['completed']})
    messagebox.showinfo("Export Successful", "Tasks have been exported to tasks.csv")

# Function to check for upcoming tasks and set notifications
def task_notification():
    while True:
        time.sleep(60)  # Check every minute
        now = datetime.datetime.now()
        for task in tasks:
            if not task['completed'] and 0 <= (task['due'] - now).total_seconds() <= 3600:
                messagebox.showwarning("Task Reminder", f"Task '{task['name']}' is due within the next hour!")

# Setting up the GUI
root = tk.Tk()
root.title("Student Study Planner")
root.geometry("500x500")

# Task list
tasks = []

# Task input fields
task_label = tk.Label(root, text="Task:")
task_label.pack(pady=5)

task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=5)

due_label = tk.Label(root, text="Due Date (YYYY-MM-DD):")
due_label.pack(pady=5)

due_entry = tk.Entry(root, width=50)
due_entry.pack(pady=5)

category_label = tk.Label(root, text="Category:")
category_label.pack(pady=5)

category_combobox = ttk.Combobox(root, values=["Homework", "Project", "Exam", "Other"])
category_combobox.set('Select Category')
category_combobox.pack(pady=5)

# Buttons
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

complete_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_button.pack(pady=5)

export_button = tk.Button(root, text="Export to CSV", command=export_to_csv)
export_button.pack(pady=5)

# Task listbox
task_listbox = tk.Listbox(root, width=75, height=15)
task_listbox.pack(pady=10)

# Start notification thread
notification_thread = threading.Thread(target=task_notification, daemon=True)
notification_thread.start()

# Run the GUI loop
root.mainloop()
