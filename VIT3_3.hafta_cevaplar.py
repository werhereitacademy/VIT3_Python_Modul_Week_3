'''Project Description: In this assignment, you will create a task manager application using the Python programming language. This application allows users to add, complete, delete, and list their tasks.
'''


task_list = []
empty_sequence_numbers = []
deleted_tasks = []

def add_task(task, status='Pending'):
    new_task = {'Task': task , 'Status' : status, 'Sequence Number' : find_sequence_number()}
    task_list.append(new_task)
    return new_task

#We are getting the sequence number from the number of elements in the list.

def find_sequence_number():
    if len(empty_sequence_numbers) == 0:
        if len(task_list) == 0:
            return 1
        else:
            return len(task_list) + 1
 #  If there are no empty sequence numbers, we return one more than the sequence number of the last element. If there are empty sequence numbers, we remove and return the smallest sequence number from the list, thus preventing two tasks from having the same sequence number.
     
    else:
        empty_sequence_numbers.sort()
        return empty_sequence_numbers.pop(0)

def complete_task(task_number):
    for i in task_list:
        if i['Sequence Number'] == task_number:
            i['Status'] = 'Successful'
            return i
    #If the task is completed, it returns the task; otherwise, it returns False. The returned value is used to check if the task is completed, providing the necessary information to the user.
    return False

def delete_task(task_number):
    for task in task_list:
        if task['Sequence Number'] == task_number:
            task['Status'] = 'Deleted'
            deleted_tasks.append(task)
            task_list.remove(task)
            empty_sequence_numbers.append(task_number)
            return task
    return False

def list_completed_tasks():
    completed_tasks = []
    for task in task_list:
        if task['Status'] == 'Successful':
            completed_tasks.append(task)
    return completed_tasks

def list_all_tasks():
    all_tasks = task_list + deleted_tasks
    all_tasks.sort(key = lambda i: i['Sequence Number'])
    return all_tasks


def program():
    print('''
    1. Add Task
    2. Complete Task
    3. Delete Task
    4. List Completed Tasks
    5. List All Tasks
    6. Exit''')

    while True:
        choice = input('Select the action you want to perform: ')
        if choice == '1':
            task = input("ENTER THE TASK:")
            new_task = add_task(task)
            print("Task Added")
            print(new_task)

        elif choice == '2':
            task_number = int(input('Enter the Task Number: '))
            completed = complete_task(task_number)
            if completed:
                print('Task Completed')
                print(completed)
            else:
                print('Task Not Found')

        elif choice == '3':
            task_number = int(input('Enter the Task Number: '))
            deleted_task = delete_task(task_number)
            if deleted_task:
                print('Task Deleted')
                print(deleted_task)
            else:
                print('Task Not Found')

        elif choice == '4':
            print('Completed Tasks:')
            print(list_completed_tasks())

        elif choice == '5':
            print('All Tasks:')
            print(list_all_tasks())

        elif choice == '6':
            print('Exiting')
            break

        else:
            print('Invalid Choice')

program()
