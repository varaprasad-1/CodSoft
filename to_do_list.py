import tkinter as tk
from tkinter import messagebox

tasks = []

def add_task():
    task = entry_task.get()
    if task:
        tasks.append({"task": task, "completed": False})
        update_listbox()
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def update_listbox():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = "✅" if task["completed"] else "❌"
        listbox_tasks.insert(tk.END, f"{task['task']} [{status}]")

def complete_task():
    selected = listbox_tasks.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to complete.")

def delete_task():
    selected = listbox_tasks.curselection()
    if selected:
        index = selected[0]
        tasks.pop(index)
        update_listbox()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def create_gui():
    global window, entry_task, listbox_tasks
    window = tk.Tk()
    window.title("To-Do List")
    window.geometry("400x400")

    entry_task = tk.Entry(window, width=30)
    entry_task.pack(pady=10)

    btn_add = tk.Button(window, text="Add Task", width=20, command=add_task)
    btn_add.pack(pady=5)

    listbox_tasks = tk.Listbox(window, width=50, height=10)
    listbox_tasks.pack(pady=10)

    btn_complete = tk.Button(window, text="Mark as Completed", width=20, command=complete_task)
    btn_complete.pack(pady=5)

    btn_delete = tk.Button(window, text="Delete Task", width=20, command=delete_task)
    btn_delete.pack(pady=5)

    window.mainloop()

# This block ensures the GUI only runs when the file is executed directly
if __name__ == "__main__":
    create_gui()
