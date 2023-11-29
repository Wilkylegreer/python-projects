import os


def DisplayMenu():
    print('1. Add Task')
    print('2. View Task(s)')
    print('3. Mark Task(s) As Completed')
    print('4. Exit')


def ChangeText(completeText):
    if completeText == True:
        return 'Completed'
    else:
        return 'Incomplete'


tasks = []


def ChooseOption():
    return input('What do you want to do? \n')


while True:
    DisplayMenu()
    menuNav = ChooseOption()

    if int(menuNav) == 1:
        # Add Task
        task = input('Enter a new task: ')
        tasks.append({"task": task, "completed": False})
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Task added! \n')
    elif int(menuNav) == 2:
        # View Task(s)
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Task(s): \n')
        for tisk in tasks:
            print(tisk['task'] + ' - ' +
                  ChangeText(tisk['completed']) + ' \n')
    elif int(menuNav) == 3:
        # Mark Task(s) As Completed
        if tasks:
            task_number = int(
                input('Enter the task number to mark as complete: '))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Task marked as completed')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('Invalid task number.')
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            print('No tasks in the list')
    elif int(menuNav) == 4:
        # Exit
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Chao')
        break
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('Error: Option not found')
