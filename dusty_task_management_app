tasks = []

def add_task(task_name):
    deleted_indexes = [task['Sequence Number'] for task in tasks if task['Status'] == 'Deleted']
    if deleted_indexes:
        seq_number = min(deleted_indexes)
        for task in tasks:
            if task['Sequence Number'] == seq_number:
                task['Task Name'] = task_name
                task['Status'] = 'Pending'
                print(f"Task '{task_name}' added with sequence number {seq_number}.")
                return
    else:
        if len(tasks) == 0:
            seq_number = 1
        else:
            seq_number = tasks[-1]['Sequence Number'] + 1
        tasks.append({'Sequence Number': seq_number, 'Task Name': task_name, 'Status': 'Pending'})
        print(f"Task '{task_name}' added with sequence number {seq_number}.")

def complete_task(seq_number):
    task = next((task for task in tasks if task['Sequence Number'] == seq_number and task['Status'] != 'Deleted'), None)
    if task:
        task['Status'] = 'Completed'
        print(f"Task '{task['Task Name']}' marked as completed.")
    else:
        print("Task not found or already completed.")

def delete_task(seq_number):
    task = next((task for task in tasks if task['Sequence Number'] == seq_number), None)
    if task:
        task['Status'] = 'Deleted'
        print(f"Task '{task['Task Name']}' deleted.")
    else:
        print("Task not found.")

def list_completed_tasks():
    completed_tasks = [task for task in tasks if task['Status'] == 'Completed']
    if completed_tasks:
        print("Completed Tasks:")
        for task in completed_tasks:
            print(f"Sequence Number: {task['Sequence Number']}, Task Name: {task['Task Name']}")
    else:
        print("No completed tasks.")

def list_all_tasks():
    sorted_tasks = sorted(tasks, key=lambda x: x['Sequence Number'])
    print("All Tasks with Status:")
    for task in sorted_tasks:
        print(f"Sequence Number: {task['Sequence Number']}, Task Name: {task['Task Name']}, Status: {task['Status']}")

def display_menu():
    print("\nTask Manager Menu:")
    print("1. Add Task")
    print("2. Complete Task")
    print("3. Delete Task")
    print("4. List Completed Tasks")
    print("5. List All Tasks")
    print("6. Exit")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == '2':
            seq_number = int(input("Enter sequence number of task to mark as completed: "))
            complete_task(seq_number)
        elif choice == '3':
            seq_number = int(input("Enter sequence number of task to delete: "))
            delete_task(seq_number)
        elif choice == '4':
            list_completed_tasks()
        elif choice == '5':
            list_all_tasks()
        elif choice == '6':
            print("Exiting Task Manager. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 6.")

if __name__ == "__main__":
    main()
