import tkinter as tk
from tkinter import messagebox, ttk
import datetime
# Added comment
import csv
import os
import threading
import time
from tkcalendar import DateEntry
import pickle

# Function to load tasks from a file
def load_tasks():
    if os.path.exists("tasks.pkl"):
        with open("tasks.pkl", "rb") as file:
            return pickle.load(file)
    return []

# Function to save tasks to a file
def save_tasks():
    with open("tasks.pkl", "wb") as file:
        pickle.dump(tasks, file)

# Function to add task
def add_task():
    task_name = task_entry.get()
    due_date = due_entry.get_date()
    category = category_combobox.get()
    priority = priority_combobox.get()

    if not task_name:
        messagebox.showerror("Missing Task Name", "Please enter a task name")
        return
    if category == 'Select Category':
        messagebox.showerror("Missing Category", "Please select a category")
        return
    if priority == 'Select Priority':
        messagebox.showerror("Missing Priority", "Please select a priority")
        return

    tasks.append({'name': task_name, 'due': due_date, 'category': category, 'priority': priority, 'completed': False})
    save_tasks()
    update_task_list()
    task_entry.delete(0, tk.END)
    category_combobox.set('Select Category')
    priority_combobox.set('Select Priority')

# Function to update the task list
def update_task_list():
    task_listbox.delete(0, tk.END)
    today = datetime.date.today()
    for task in sorted(tasks, key=lambda x: (x['due'], x['priority'])):
        task_str = f"{task['name']} - Due: {task['due'].strftime('%Y-%m-%d')} - Category: {task['category']} - Priority: {task['priority']}"
        if task['due'] < today:
            task_str += " (Overdue!)"
        if task['completed']:
            task_str += " (Completed)"
        task_listbox.insert(tk.END, task_str)

# Function to mark task as completed
def complete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        tasks[selected_task[0]]['completed'] = True
        save_tasks()
        update_task_list()

# Function to export tasks to a CSV file
def export_to_csv():
    with open('tasks.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'due', 'category', 'priority', 'completed']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({'name': task['name'], 'due': task['due'].strftime('%Y-%m-%d'), 'category': task['category'], 'priority': task['priority'], 'completed': task['completed']})
    messagebox.showinfo("Export Successful", "Tasks have been exported to tasks.csv")

# Function to check for upcoming tasks and set notifications
def task_notification():
    while True:
        time.sleep(60)  # Check every minute
        now = datetime.datetime.now().date()
        for task in tasks:
            if not task['completed'] and 0 <= (task['due'] - now).days <= 1:
                messagebox.showwarning("Task Reminder", f"Task '{task['name']}' is due within the next day!")

# Setting up the GUI
root = tk.Tk()
root.title("Student Study Planner")
root.geometry("600x600")
root.configure(bg='#f0f0f0')

# Task list
tasks = load_tasks()

# Task input fields
task_frame = tk.Frame(root, bg='#f0f0f0')
task_frame.pack(pady=10)

task_label = tk.Label(task_frame, text="Task:", bg='#f0f0f0')
task_label.grid(row=0, column=0, padx=5, pady=5, sticky='w')

task_entry = tk.Entry(task_frame, width=40)
task_entry.grid(row=0, column=1, padx=5, pady=5)

due_label = tk.Label(task_frame, text="Due Date:", bg='#f0f0f0')
due_label.grid(row=1, column=0, padx=5, pady=5, sticky='w')

due_entry = DateEntry(task_frame, width=38, date_pattern='yyyy-mm-dd')
due_entry.grid(row=1, column=1, padx=5, pady=5)

category_label = tk.Label(task_frame, text="Category:", bg='#f0f0f0')
category_label.grid(row=2, column=0, padx=5, pady=5, sticky='w')

category_combobox = ttk.Combobox(task_frame, values=["Homework", "Project", "Exam", "Other"])
category_combobox.set('Select Category')
category_combobox.grid(row=2, column=1, padx=5, pady=5)

priority_label = tk.Label(task_frame, text="Priority:", bg='#f0f0f0')
priority_label.grid(row=3, column=0, padx=5, pady=5, sticky='w')

priority_combobox = ttk.Combobox(task_frame, values=["High", "Medium", "Low"])
priority_combobox.set('Select Priority')
priority_combobox.grid(row=3, column=1, padx=5, pady=5)

# Buttons
button_frame = tk.Frame(root, bg='#f0f0f0')
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", command=add_task, width=15, bg='#4caf50', fg='white')
add_button.grid(row=0, column=0, padx=5, pady=5)

complete_button = tk.Button(button_frame, text="Complete Task", command=complete_task, width=15, bg='#2196f3', fg='white')
complete_button.grid(row=0, column=1, padx=5, pady=5)

export_button = tk.Button(button_frame, text="Export to CSV", command=export_to_csv, width=15, bg='#ff9800', fg='white')
export_button.grid(row=0, column=2, padx=5, pady=5)

# Task listbox
# Added comment
task_listbox = tk.Listbox(root, width=80, height=15, bg='#ffffff', selectbackground='#cfe2f3')
task_listbox.pack(pady=10)

# Load initial tasks into the listbox
update_task_list()
# Added comment

# Start notification thread
notification_thread = threading.Thread(target=task_notification, daemon=True)
notification_thread.start()

# Run the GUI loop
root.mainloop()