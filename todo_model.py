import sys

class TodoModel():
    
    def __init__(self):
        self.work_list = []
        self.todo_file = open("todo.txt", "r")
        self.scanned_text = self.todo_file.readlines()

        for line in self.scanned_text:
            self.work_list.append(line)
    
    def add_todo(self):
        self.todo_expression = str(sys.argv[4:])
        self.todo_file = open("todo.txt", "w")
        self.todo_file.write(self.todo_expression)