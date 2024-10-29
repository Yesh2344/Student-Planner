Student Study Planner

A simple and effective task management tool for students, built using Python and Tkinter. This application helps students organize their tasks, set due dates, assign categories and priorities, mark tasks as completed, and export their tasks to a CSV file for easy tracking.

Features

Add Tasks: Create tasks with a name, due date, category, and priority.

Mark as Completed: Mark tasks as completed when finished.

View Tasks: Tasks are displayed with details like due date, category, priority, and whether they are overdue or completed.

Notifications: Get reminders for tasks that are due within the next day.

Export to CSV: Export your tasks to a CSV file for external reference.

Persistent Storage: Tasks are saved locally, so they are available even after restarting the application.

Getting Started

Prerequisites

Python 3.x

Required Python libraries: tkinter, tkcalendar, pickle

To install tkcalendar, run the following command:

pip install tkcalendar

Installation

Clone the repository:

git clone https://github.com/yourusername/study-planner.git

Navigate to the project directory:

cd study-planner

Run the application:

python student_planner.py

Usage

Adding a Task: Fill in the task name, select the due date, category, and priority, then click on "Add Task".

Marking as Completed: Select a task from the list and click on "Complete Task" to mark it as done.

Exporting Tasks: Click on "Export to CSV" to save the tasks in a CSV file.

Categories & Priorities

Categories: Tasks can be categorized as Homework, Project, Exam, or Other.

Priorities: Set the priority of the task as High, Medium, or Low.

Notifications

The application checks for tasks that are due within the next day and notifies you via a pop-up message.

Files

student_planner.py: The main script that runs the application.

tasks.pkl: Stores the tasks data for persistence.

tasks.csv: A CSV file that contains exported tasks.

Screenshots




Contributing

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -am 'Add new feature').

Push to the branch (git push origin feature-branch).

Create a new Pull Request.

License

This project is licensed under the MIT License - see the LICENSE file for details.

Acknowledgments

Thanks to the contributors of the Tkinter and tkcalendar libraries for making GUI development in Python more accessible.

Feel free to contribute, report issues, or suggest new features!

