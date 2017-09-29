import sys
from todo_view import TodoView
from todo_model import TodoModel

class TodoController():

    def __init__(self):
        self.view = TodoView()
        self.model = TodoModel()
        self.command()

    def get_arguments(self):
        if len(sys.argv) > 1:
            return sys.argv[1]
        return None

    def command(self):
        if self.get_arguments() == None:
            self.view.usage()
        elif self.get_arguments() == "l":
            self.view.printer(self.model.work_list)
        elif self.get_arguments() == "a":
            self.model.add_todo()
            #open w todos.txt add new todo line
        elif self.get_arguments() == "r":
            pass
            #open w todos, delete by index
        elif self.get_arguments() == "c":
            pass
            #open w todos, change todo's 0 to 1

