from task import Task 

class Logic:
    def __init__(self):
        self.tasks=[]

    def add(self,ad):
        for i in self.tasks:
            if i.taskid==ad.taskid:
                return False
        self.tasks.append(ad)  
        return True
            
    
    def update(self,taskid,priority,status,location):
        for i in self.tasks:
            if i.taskid==taskid:
                i.priority==priority
                i.status==status
                i.location==location
                return True
            else:
                return False
            
    def remove(self,taskid):
        for i in self.tasks:
            if i.taskid==taskid:
                self.tasks.remove(i)
                return True
        return False
                
    def view_all(self):
        return self.tasks
    
    def view_priority(self,priority):
        prior=[]
        for i in self.tasks:
            if i.priority == priority:
                prior.append(i)
        if prior:
            return prior
        else:
            return False
        
    def view_location(self,location):
        locate=[]
        for i in self.tasks:
            if i.location == location:
                locate.append(i)
        if locate:
            return locate
        else:
            return False
        
    def view_status(self,status):
        stat=[]
        for i in self.tasks:
            if i.status == status:
                stat.append(i)
        if stat:
            return stat
        else:
            return False
        


            

    
       