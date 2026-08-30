while True:
    def app():
        try:
            taskmain=''
            print('To Do list App')
            print('''1.Enter task
2.View task
3.delete task
                  ''')
            a=int(input('Enter number (1 to 3):'))
            if a==1:
                task=input('Enter task :')
                task=taskmain
                print('Task saved')
                print('''1.exit
2.view task
                ''')
                b=int(input('Enter number (1,2):'))
                if b==1:
                    app()
                elif b==2:
                    print('your task :',taskmain)
                    d=input('want to exit(press 1):')
                    if d==1:
                        app()
                    else:
                        app()
            elif a==2:
                print('your task:',taskmain)
                
            elif a==3:
                taskmain='---no tasks---'
                print('Task deleted')
                taskmain=task
                app()
        except ValueError:
            print('somethig went wrong')
    app()