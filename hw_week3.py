import json
import os.path

file = 'task_list.json'


def check_file(current_file):  # Dosya yolunda dosyanin olup olmadiginin kontrolu
    return os.path.exists(current_file)


def read_from_json():
    global file
    with open(file, 'r') as fp:
        task_list = json.load(fp)
    return task_list


def write2json(task_list: list):
    global file
    with open(file, 'w') as fp:
        json.dump(task_list, fp)
    return task_list


def add_task(task_name):
    task_list = []
    task_id = 1
    if not check_file(file):  # Eger dosya mevcut degilse, gorevi bos listeye ekliyor ve json dosyasina yazdiriyoruz
        task_list += [{'task_id': task_id, 'task_name': task_name, 'task_status': 'Pending'}]
        res = write2json(task_list)

    else:  # Eger dosya mevcut ise, once dosyadaki veriyi okuyor...
        task_list = read_from_json()
        list_id = None
        for i in range(len(task_list)):  # Silinen gorev varsa listedeki konumunun tespit edilmesi
            if task_list[i]['task_status'] == 'Deleted':
                list_id = i
                task_id = task_list[i]['task_id']
                break
        if list_id is None:  # Eger silinen gorev yoksa, siradan normal bir gorev ekle
            task_id = task_list[-1]['task_id'] + 1
            task_list += [{'task_id': task_id, 'task_name': task_name, 'task_status': 'Pending'}]
        else:  # Silinen bir gorev varsa, yeni ekleneni listede onun yerine ekle
            task_list[list_id]['task_id'] = task_id
            task_list[list_id]['task_name'] = task_name
            task_list[list_id]['task_status'] = 'Pending'
        res = write2json(task_list)  # En son guncellenmis listeyi json dosyasina yazdiriyoruz

    return res  # task_add fonksiyonu listeyi geri donduruyor


def complete_task(task_id):
    res = False
    if check_file(file):
        task_list = read_from_json()
        for i in range(len(task_list)):
            if task_list[i]['task_id'] == task_id:
                task_list[i]['task_status'] = 'Completed'
                res = True
                write2json(task_list)
                break
    return res


def delete_task(task_id):
    res = False
    if check_file(file):
        task_list = read_from_json()
        for i in range(len(task_list)):
            if task_list[i]['task_id'] == task_id:
                task_list[i]['task_status'] = 'Deleted'
                res = True
                write2json(task_list)
                break
    return res


def list_tasks(lists):
    new_list = []
    if check_file(file):
        task_list = read_from_json()
        for i in task_list:
            if i['task_status'] in lists:
                new_list += [i]
    return new_list


def get1task(task_id):
    res = 'Error!!!'
    if check_file(file):
        task_list = read_from_json()
        for i in task_list:
            if i['task_id'] == task_id:
                res = i
    return res


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
        if user_input == 'add':
            the_task_name = input('Enter the task name: ')
            result = add_task(the_task_name)
            if type(result) != list:
                print('There is an error!')
            else:
                print(f'The task is named \"{the_task_name}\" is successfully added to TMS!')
                print(result)

        elif user_input == 'complete':
            print(list_tasks('Pending'))
            the_task_id = int(input('Enter the "Task ID" that you have wanted to sign as "Completed": '))
            result = complete_task(the_task_id)
            if result:
                print('The task is signed as Completed!\n'
                      f'Info: {get1task(the_task_id)}')
            else:
                print('There is an error!')

        elif user_input == 'delete':
            print(list_tasks(['Pending', 'Completed']))
            the_task_id = int(input('Enter the "Task ID" that you have wanted to delete: '))
            result = delete_task(the_task_id)
            if result:
                print('The task is deleted from TMS!\n'
                      f'Info: {get1task(the_task_id)}')
            else:
                print('There is an error!')

        elif user_input == 'listcmp':
            print(list_tasks('Completed'))

        elif user_input == 'listall':
            print(list_tasks(['Pending', 'Completed']))

        elif user_input == 'quit':
            pass

        else:
            continue
