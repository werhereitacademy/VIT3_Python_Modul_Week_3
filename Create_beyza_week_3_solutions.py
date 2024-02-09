print("Task Manager Application")

menu = ("≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ≀" +     # The menu design that will be shown to the user at first entry.
        "\n≀                                                  ≀" +
        "\n≀   Press 1 to add a new task                      ≀" +
        "\n≀   Press 2 to complete a task                     ≀" +
        "\n≀   Press 3 to delete a task                       ≀" +
        "\n≀   Press 4 to list completed tasks                ≀" +
        "\n≀   Press 5 to list all tasks and their statuses   ≀" +
        "\n≀   Press Q to exit                                ≀" +
        "\n≀                                                  ≀" +
        "\n≀~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ≀")

print(menu)

task_list = []  # Empty list to add dictionaries created by the function.


def add_task(name):
    global task_list  # To be able to use the globally defined list within the function.

    task_dict = {"Task Name": name, "Status": "Pending"}  # Dictionary defined within the function for each task to be added to the list each time the function is called.
    task_list.append(task_dict)  # The dictionary created is added to the list.
    print("{} task added.".format(name))  # Information is provided to the user that the task has been added.
    return task_dict


def complete_task(task_number):
    global task_list

    for index, task_dict in enumerate(task_list, start=1):  # We use this function to match the items with index numbers in a list.
        # Normally, the enumeration starts from 0 with enumarate, but we started from 1 with start=1.
        if index == task_number:
            task_dict["Status"] = "Successful"
            print("Task number {} completed.".format(task_number))
            return


def delete_task(task_number):
    global task_list

    for index, task_dict in enumerate(task_list, start=1):  # We arranged it again like in the task completion function.
        if index == task_number:
            task_list.remove(task_dict)
            print("Task number {} deleted.".format(task_number))
            return


def list_completed_tasks():
    global task_list

    completed_tasks = [(index, task_dict) for index, task_dict in enumerate(task_list, start=1) if
                       task_dict["Status"] == "Successful"]
    # We define a list shortcut for completed tasks with list comprehension method.

    if completed_tasks:  # This expression actually means "if the list is not empty."
        for index, task_dict in completed_tasks:
            print("{}. {}".format(index, task_dict["Task Name"]))
    else:
        print("No completed tasks found.")


def list_all_tasks():
    global task_list

    print("All Tasks:")
    for index, task_dict in enumerate(task_list, start=1):  # Again, we start the ranking from the beginning.
        print("{}. {} - Status: {}".format(index, task_dict["Task Name"], task_dict["Status"]))


while True:
    choice = input("Select an operation you want to perform: ")

    if choice == "1":
        task_name = input("Enter the name of the task to be performed: ")
        add_task(task_name)
    elif choice == "2":
        task_number = int(input("Enter the sequence number of the completed task: "))
        complete_task(task_number)
    elif choice == "3":
        task_number = int(input("Enter the sequence number of the task to be deleted: "))
        delete_task(task_number)
    elif choice == "4":
        list_completed_tasks()
    elif choice == "5":
        list_all_tasks()
    elif choice.upper() == "Q":
        print("Exiting the application...")
        break
    else:
        print("You made an invalid selection. Please check the menu again;")
        print(menu)
