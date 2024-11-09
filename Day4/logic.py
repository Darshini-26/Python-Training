from task import Task 

class Logic:
    def __init__(self):
        self.tasks=[]

    def add(self,ta):
        for i in self.tasks:
            if i.taskid==ta.taskid:
                return False
        self.tasks.append(ta)  
        return True
            
    def view_all(self):
        return self.tasks
    
    def update(self,taskid,priority,status,location):
        for i in self.tasks:
            if i.taskid==taskid:
                i.priority==priority
                i.status==status
                i.location==location
                


            

    
       