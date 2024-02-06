def add_task():
    pass


def complete_task():
    pass


def delete_task():
    pass


def list_completed_tasks():
    pass


def list_all_tasks():
    pass


def get_help():
    print('You should write the commands below;\n'
          '"add" | for adding a new task\n'
          '"complete" | for completing a task\n'
          '"delete" | for deleting a task\n'
          '"listcmp" | for listing the completed tasks\n'
          '"listall" | for listing all tasks\n'
          '"quit" | for terminating the program')


def quit_app():
    quit()


if __name__ == "__main__":
    user_input = 'dummy'
    while user_input != 'quit':
        get_help()
        user_input = input('What would you like to do?: ')
        pass
