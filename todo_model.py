class TodoModel():
    
    def __init__(self):
        self.work_list = []
        self.todo_file = open("todo.txt", "r")
        self.scanned_text = self.todo_file.readlines()

        for line in self.scanned_text:
            self.work_list.append(line)