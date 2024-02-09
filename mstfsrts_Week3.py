"""
Question 1: Task Manager Application
Project Description: In this assignment, you will create a task manager application using the Python programming language. This application allows users to add, complete, delete, and list their tasks.

Requirements:
1- Tasks will be stored in a Python list, and each task will be represented as a dictionary. Each task should have the following properties:

Sequence Number (Automatically assigned)
Task Name
Status (Successful, Pending, or Deleted)
2- Operations that users can perform:

Add a new task
Complete a task
Delete a task
List completed tasks
List all tasks with their statuses
Exit
3- Tasks should automatically receive a sequence number based on the order of addition.

4- Newly added tasks should be saved in place of deleted task numbers.

5- Tasks should be sorted according to their sequence numbers when listed.

6- Users should receive appropriate feedback after each operation. For example, when adding a new task, they should see a message indicating that the task has been added.
"""

import json

TASK_FILE = "tasks.json"

#Load Tasks Data From File
def load_tasks_from_file():
    try:
        with open(TASK_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {"tasks": [], "deleted_tasks": []}

#Save Task Data in Dictionary to File
def save_tasks_to_file(data):
    with open(TASK_FILE, 'w') as file:
        json.dump(data, file)

#Creates a new task with the given task name and adds this task to the existing task list.
def add_new_task(task_name):
    data = load_tasks_from_file()
    tasks = data["tasks"]
    deleted_tasks = data["deleted_tasks"]
    
    if deleted_tasks:
        new_task_number = deleted_tasks.pop(0)["Task Number"]
    else:
        new_task_number = len(tasks) + 1

    new_task = {
        "Task Number": new_task_number,
        "Task Name": task_name,
        "Status": "Pending",
    }
    tasks.append(new_task)
    tasks.sort(key=lambda x: x["Task Number"])  # Sorting
    data["tasks"] = tasks
    save_tasks_to_file(data)
    print(f"New task added: {task_name}")

#Updates the status of the task with the specified task number to "Completed" and saves the changes to the task list file.
def complete_task(task_number):
    data = load_tasks_from_file()
    tasks = data["tasks"]
    for task in tasks:
        if task["Task Number"] == task_number:
            task["Status"] = "Completed"
            save_tasks_to_file(data)
            print(f"Task completed: {task['Task Name']}")
            return
    print("No task found with the specified task number.")

#This function allows the user to delete tasks either individually or all at once.
def delete_task():
    data = load_tasks_from_file()
    tasks = data["tasks"]
    deleted_tasks = data["deleted_tasks"]
    print("1. Delete Specific Task")
    print("2. Delete All Tasks")
    print("3. Go Back")
    choice = input("Select an option (1-3): ")
    if choice == "1":
        print("All Tasks:")
        for task in tasks:
            print(f"{task['Task Number']}. {task['Task Name']} - Status: {task['Status']}")

        task_number = int(input("Enter the task number of the task to be deleted: "))
        deleted_task = None

        for task in tasks:
            if task["Task Number"] == task_number:
                deleted_task = task
                break

        if deleted_task:
            print("Task Information to be Deleted:")
            print(f"Task Name: {deleted_task['Task Name']}")
            
            answer = input("Do you want to delete this task? (Yes/No): ").lower()
            if answer == "yes":
                tasks.remove(deleted_task)
                deleted_tasks.append(deleted_task)
                tasks.sort(key=lambda x: x["Task Number"])  # Sorting
                save_tasks_to_file(data)
                print("Task deleted.")
            else:
                print("Task not deleted.")
        else:
            print("No task found with the specified task number.")
    elif choice == "2":
        answer = input("Are you sure you want to delete all tasks? (Yes/No): ").lower()
        if answer == "yes":
            data["deleted_tasks"].extend(tasks)
            data["tasks"] = []
            save_tasks_to_file(data)
            print("All tasks deleted.")
        else:
            print("Tasks not deleted.")
    elif choice == "3":
        pass
    else:
        print("Invalid choice. Please try again.")

#This function lists all tasks that have been marked as completed.
def list_completed_tasks():
    tasks = load_tasks_from_file()["tasks"]
    completed_tasks = [task for task in tasks if task["Status"] == "Completed"]
    if completed_tasks:
        print("Completed Tasks:")
        for task in completed_tasks:
            print(f"{task['Task Number']}. {task['Task Name']} - Status: {task['Status']}")
    else:
        print("No completed tasks found.")

#This function lists all tasks, including both active tasks and deleted tasks, along with their respective statuses.
def list_all_tasks():
    data = load_tasks_from_file()
    tasks = data["tasks"]
    deleted_tasks = data["deleted_tasks"]
    if tasks:
        print("All Tasks:")
        for task in tasks:
            print(f"{task['Task Number']}. {task['Task Name']} - Status: {task['Status']}")
    if deleted_tasks:
        print("Deleted Tasks:")
        for task in deleted_tasks:
            print(f"{task['Task Number']}. {task['Task Name']} - Status: {task['Status']}")
    if not tasks and not deleted_tasks:
        print("No tasks found.")

def main_menu():
    while True:
        print("\n--- MAIN MENU ---")
        print("1. Add New Task")
        print("2. Complete Task")
        print("3. Delete Task")
        print("4. List Completed Tasks")
        print("5. List All Tasks")
        print("6. Exit")

        choice = input("Select an operation (1-6): ")

        if choice == "1": #Add New Task
            new_task_name = input("Enter the name of the new task: ")
            add_new_task(new_task_name)
        elif choice == "2": #Complete Task
            pending_tasks = [task for task in load_tasks_from_file()["tasks"] if task["Status"] == "Pending"]
            if pending_tasks:
                print("Pending Tasks:")
                for task in pending_tasks:
                    print(f"{task['Task Number']}. {task['Task Name']} - Status: {task['Status']}")
                task_number = int(input("Enter the task number of the completed task: "))
                complete_task(task_number)
            else:
                print("No pending tasks found.")
        elif choice == "3": #Delete Task
            delete_task()
        elif choice == "4": #List Completed Tasks
            list_completed_tasks()
        elif choice == "5": #List All Tasks
            list_all_tasks()
        elif choice == "6": #Exit
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
    