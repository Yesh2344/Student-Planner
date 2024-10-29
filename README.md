Student Study Planner
Description
Student Study Planner is a Python-based desktop application designed to help students organize their tasks, assignments, and study schedules effectively. With an intuitive graphical user interface, it allows users to manage their academic responsibilities with ease.

Features
Task Management: Add, view, and complete tasks
Due Date Tracking: Set and monitor due dates for each task
Categorization: Organize tasks into categories (Homework, Project, Exam, Other)
Priority Setting: Assign priority levels (High, Medium, Low) to tasks
Task Completion: Mark tasks as completed
Data Persistence: Tasks are saved automatically and loaded on startup
CSV Export: Export your task list to a CSV file for external use
Notification System: Receive reminders for upcoming tasks
Requirements
Python 3.x
tkinter
tkcalendar
Installation
Ensure you have Python 3.x installed on your system.
Install the required packages:
pip install tkcalendar
Download the student_planner.py file.
Usage
Run the script:
python student_planner.py
The main window of the Student Study Planner will open.
To add a task:
Enter the task name
Select a due date
Choose a category
Set a priority
Click "Add Task"
To complete a task:
Select the task in the list
Click "Complete Task"
To export tasks to CSV:
Click "Export to CSV"
A file named tasks.csv will be created in the same directory
Features in Detail
Task Input
Task Name: Enter the name or description of your task
Due Date: Select the due date using the calendar widget
Category: Choose from Homework, Project, Exam, or Other
Priority: Set as High, Medium, or Low
Task List
Displays all tasks sorted by due date and priority
Shows task name, due date, category, and priority
Indicates if a task is overdue or completed
Notifications
The application checks for upcoming tasks every minute
Displays a warning for tasks due within the next day
Data Persistence
Tasks are automatically saved to a file (tasks.pkl)
Tasks are loaded from this file when the application starts
Contributing
Contributions to improve the Student Study Planner are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

License
This project is open source and available under the MIT License.
