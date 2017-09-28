from todo_model import TodoModel

class TodoView():
    
    def printer(self, todo):
        self.todo_work = TodoModel()
        for element in self.todo_work.work_list:
            print(element)
    
    def usage(self):
        print(" Command Line Todo application \n\
        ============================= \n\
        Command line arguments: \n\
            -l   Lists all the tasks \n\
            -a   Adds a new task \n\
            -r   Removes an task \n\
            -c   Completes an task")