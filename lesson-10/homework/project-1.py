<<<<<<< HEAD

class Task:
    
    def __init__(self,task_title, description,due_date,status):
        self.task_title = task_title
        self.description = description
        self.due_date = due_date
        self.status = status   

class TodoList:
    task_list = {}

    def add_task(self):
        
        title = input('   Type the task title: ')
        description = input('   Type the task description: ')
        due_date = input('   When is the task due date : ')
        task = Task(title,description,due_date,'Incompleted')

        TodoList.task_list[len(TodoList.task_list)+1] = task

        print()
        print('✅ Task Added Successfully!')

        
    def mark_as_complete(self):
        for i in TodoList.task_list.items():
            print(f'{i[0]}.', f'{i[1].task_title} | {i[1].status}')
        print()

        task_complete = int(input('   Which task do you mark as complete: '))
        the_task = TodoList.task_list[task_complete]
        the_task.status = 'Completed'
        print()
        print(f'{task_complete}.', f'{the_task.task_title} | {the_task.status}')
        print()
        print('✅ Task Completed Successfully!')

    
    def list_all_tasks(self):
        for i in TodoList.task_list.items():
            print(f'       Task-{i[0]}')
            print(f'task_title:  {i[1].task_title}')
            print(f'description: {i[1].description}')
            print(f'due_date:    {i[1].due_date}')
            print(f'status:      {i[1].status}')
            print()

        if len(TodoList.task_list) == 1:
            print(f'✅ You have {len(TodoList.task_list)} task')
        elif len(TodoList.task_list) > 1:
            print(f'✅ You have {len(TodoList.task_list)} tasks')
        else:
            print(f'❗You don\'t have any task yet!')
    

    def incomplete_tasks(self):
        n = 0
        for i in TodoList.task_list.items():
            if i[1].status == 'Incompleted':
                n += 1
                print(f'       Task-{i[0]}')
                print(f'task_title:  {i[1].task_title}')
                print(f'description: {i[1].description}')
                print(f'due_date:    {i[1].due_date}')
                print(f'status:      {i[1].status}')
                print()
        if n == 1:
            print(f'✅ You have {n} incompleted task')
        elif n > 1:
            print(f'✅ You have {n} incompleted tasks')
        else:
            print(f'❗You don\'t have any incompleted task!')
            
   

my_todolist = TodoList()

def print_menu():
    print('--------------------------------')
    print('ToDo List menu:')
    print('1. Add tasks')
    print('2. Mark tasks as complete')
    print('3. List all tasks')
    print('4. Display only incomplete tasks')
    print('0. Exit')

    
while True:

    a = print_menu()
    print()
    command = input('Please enter your command: ')
    print()

    if command == '1':
        my_todolist.add_task()
    elif command == '2':
        my_todolist.mark_as_complete() 
    elif command == '3':
        my_todolist.list_all_tasks()
    elif command == '4':
        my_todolist.incomplete_tasks() 
    else:
        break
=======

class Task:
    
    def __init__(self,task_title, description,due_date,status):
        self.task_title = task_title
        self.description = description
        self.due_date = due_date
        self.status = status   

class TodoList:
    task_list = {}

    def add_task(self):
        
        title = input('   Type the task title: ')
        description = input('   Type the task description: ')
        due_date = input('   When is the task due date : ')
        task = Task(title,description,due_date,'Incompleted')

        TodoList.task_list[len(TodoList.task_list)+1] = task

        print()
        print('✅ Task Added Successfully!')

        
    def mark_as_complete(self):
        for i in TodoList.task_list.items():
            print(f'{i[0]}.', f'{i[1].task_title} | {i[1].status}')
        print()

        task_complete = int(input('   Which task do you mark as complete: '))
        the_task = TodoList.task_list[task_complete]
        the_task.status = 'Completed'
        print()
        print(f'{task_complete}.', f'{the_task.task_title} | {the_task.status}')
        print()
        print('✅ Task Completed Successfully!')

    
    def list_all_tasks(self):
        for i in TodoList.task_list.items():
            print(f'       Task-{i[0]}')
            print(f'task_title:  {i[1].task_title}')
            print(f'description: {i[1].description}')
            print(f'due_date:    {i[1].due_date}')
            print(f'status:      {i[1].status}')
            print()

        if len(TodoList.task_list) == 1:
            print(f'✅ You have {len(TodoList.task_list)} task')
        elif len(TodoList.task_list) > 1:
            print(f'✅ You have {len(TodoList.task_list)} tasks')
        else:
            print(f'❗You don\'t have any task yet!')
    

    def incomplete_tasks(self):
        n = 0
        for i in TodoList.task_list.items():
            if i[1].status == 'Incompleted':
                n += 1
                print(f'       Task-{i[0]}')
                print(f'task_title:  {i[1].task_title}')
                print(f'description: {i[1].description}')
                print(f'due_date:    {i[1].due_date}')
                print(f'status:      {i[1].status}')
                print()
        if n == 1:
            print(f'✅ You have {n} incompleted task')
        elif n > 1:
            print(f'✅ You have {n} incompleted tasks')
        else:
            print(f'❗You don\'t have any incompleted task!')
            
   

my_todolist = TodoList()

def print_menu():
    print('--------------------------------')
    print('ToDo List menu:')
    print('1. Add tasks')
    print('2. Mark tasks as complete')
    print('3. List all tasks')
    print('4. Display only incomplete tasks')
    print('0. Exit')

    
while True:

    a = print_menu()
    print()
    command = input('Please enter your command: ')
    print()

    if command == '1':
        my_todolist.add_task()
    elif command == '2':
        my_todolist.mark_as_complete() 
    elif command == '3':
        my_todolist.list_all_tasks()
    elif command == '4':
        my_todolist.incomplete_tasks() 
    else:
        break
>>>>>>> cf8d6416b90c8d8e28c2db3a2b57789798afffb2
