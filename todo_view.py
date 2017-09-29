class TodoView():
    
    def printer(self, todo):
        
        for element in todo:
            if element[0] == "0":
                print("[ ] " + element[2:])
            elif element[0] == "1":
                print("[X] " + element[2:])

    def usage(self):
        print(" Command Line Todo application \n\
        ============================= \n\
        Command line arguments: \n\
            -l   Lists all the tasks \n\
            -a   Adds a new task \n\
            -r   Removes a task \n\
            -c   Completes a task")