“””Question 1: Task Manager Application Project Description: In this assignment, you will create a task manager application using the Python programming language. 
This application allows users to add, complete, delete, and list their tasks.
Requirements: 1- Tasks will be stored in a Python list, and each task will be represented as a dictionary. Each task should have the following properties:
Sequence Number (Automatically assigned)
Task Name
Status (Successful, Pending, or Deleted)
2- Operations that the user can perform:
Add a new task
Complete a task
Delete a task
List completed tasks
List all tasks along with their statuses
Exit
3- Tasks should automatically receive a sequence number based on the order of addition.
4- Newly added tasks should be saved in place of deleted task numbers.
5- Tasks should be sorted by sequence number when listed.
6- Appropriate feedback should be provided to the user after each operation. For example, when adding a new task, the user should see a message indicating that
the task has been added.”””


tasks = []

def display_menu():
    print("\nTask Manager Application")
    print("1. Add a new task")
    print("2. Complete a task")
    print("3. Delete a task")
    print("4. List completed tasks")
    print("5. List all tasks")
    print("6. Exit")

def add_task():
    print("\nAdding a new task:")
    task_name = input("Enter the task name: ")
    task = {"Task Name": task_name, "Status": "Pending"}
    tasks.append(task)
    print("New task added:", task_name)

def complete_task():
    if not tasks:
        print("No tasks to complete.")
        return

    print("\nTasks to be completed:")
    for i, task in enumerate(tasks, start=1):
        if task["Status"] == "Pending":
            print(f"{i}. {task['Task Name']}")

    task_number = int(input("Enter the number of the completed task: "))
    if 1 <= task_number <= len(tasks):
        tasks[task_number - 1]["Status"] = "Completed"
        print("Task completed.")
    else:
        print("Invalid task number.")

def delete_task():
    if not tasks:
        print("No tasks to delete.")
        return

    print("\nTasks to be deleted:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['Task Name']}")

    task_number = int(input("Enter the number of the task to be deleted: "))
    if 1 <= task_number <= len(tasks):
        deleted_task = tasks.pop(task_number - 1)
        print("Deleted task:", deleted_task["Task Name"])
    else:
        print("Invalid task number.")

def list_completed_tasks():
    completed_tasks = [task for task in tasks if task["Status"] == "Completed"]
    if completed_tasks:
        print("\nCompleted Tasks:")
        for i, task in enumerate(completed_tasks, start=1):
            print(f"{i}. {task['Task Name']}")
    else:
        print("No completed tasks.")

def list_all_tasks():
    if tasks:
        print("\nAll Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task['Task Name']} - Status: {task['Status']}")
    else:
        print("No tasks.")

def main():
    while True:
        display_menu()
        choice = input("Enter the number of the action you want to perform (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            complete_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            list_completed_tasks()
        elif choice == "5":
            list_all_tasks()
        elif choice == "6":
            print("Exiting the program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
