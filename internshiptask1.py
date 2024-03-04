import tkinter as tk
from tkinter import ttk
from datetime import datetime

class Task:
    def __init__(self, description, priority, due_date=None, completed=False):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.completed = completed

    def __str__(self):
        return f"{self.description} (Priority: {self.priority}, Due: {self.due_date}, Completed: {self.completed})"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, index):
        del self.tasks[index]

    def mark_task_completed(self, index):
        self.tasks[index].completed = True

    def get_all_tasks(self):
        return self.tasks

    def save_tasks_to_file(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(str(task) + '\n')

def add_task():
    description = description_entry.get()
    priority = priority_var.get()
    due_date_str = due_date_entry.get()
    due_date = datetime.strptime(due_date_str, "%Y-%m-%d") if due_date_str else None
    task_manager.add_task(Task(description, priority, due_date))
    update_task_list()

def remove_task():
    index = task_listbox.curselection()[0]
    task_manager.remove_task(index)
    update_task_list()

def mark_completed():
    index = task_listbox.curselection()[0]
    task_manager.mark_task_completed(index)
    update_task_list()

def save_tasks():
    filename = "tasks.txt"
    task_manager.save_tasks_to_file(filename)
    status_label.config(text=f"Tasks saved to {filename}, search for {filename} on your system")

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in task_manager.get_all_tasks():
        if task.completed:
            task_listbox.insert(tk.END, str(task), "completed")
        else:
            task_listbox.insert(tk.END, str(task))

task_manager = TaskManager()

root = tk.Tk()
root.title("Taski: To-Do List Application")
root.geometry("500x300")

style = ttk.Style()
style.configure("not_completed.TLabel", foreground="black")
style.configure("completed.TLabel", foreground="gray")

description_label = ttk.Label(root, text="Task:")
description_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)
description_entry = ttk.Entry(root)
description_entry.grid(row=0, column=1, padx=5, pady=5)

priority_label = ttk.Label(root, text="Priority:")
priority_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)
priority_var = tk.StringVar()
priority_combobox = ttk.Combobox(root, textvariable=priority_var, values=["High", "Medium", "Low"])
priority_combobox.grid(row=1, column=1, padx=5, pady=5)

due_date_label = ttk.Label(root, text="Due Date (YYYY-MM-DD):")
due_date_label.grid(row=2, column=0, padx=5, pady=5, sticky=tk.W)
due_date_entry = ttk.Entry(root)
due_date_entry.grid(row=2, column=1, padx=5, pady=5)

add_button = ttk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=tk.EW)

task_listbox = tk.Listbox(root, height=10, width=50)
task_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5, sticky=tk.NSEW)

remove_button = ttk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=5, column=0, padx=5, pady=5, sticky=tk.EW)

mark_completed_button = ttk.Button(root, text="Mark Completed", command=mark_completed)
mark_completed_button.grid(row=5, column=1, padx=5, pady=5, sticky=tk.EW)

save_button = ttk.Button(root, text="Save Tasks", command=save_tasks)
save_button.grid(row=6, column=0, columnspan=2, padx=5, pady=5, sticky=tk.EW)

status_label = ttk.Label(root, text="")
status_label.grid(row=7, column=0, columnspan=2, padx=5, pady=5)

update_task_list()

root.mainloop()
