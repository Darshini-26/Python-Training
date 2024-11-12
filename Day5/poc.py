class Task:
      
    def __init__(self,taskid,taskname,priority,status,location):
        self.taskid=taskid
        self.taskname=taskname
        self.priority=priority
        self.status=status
        self.location=location

    def __str__(self):
        return f"taskid {self.taskid}- taskname {self.taskname}- priority {self.priority}- status {self.status}- location {self.location}"

tasks = [     Task(1,"ABC", 1,"Success","Cbe"),
              Task(2,"XYZ", 3,"Completed","Chennai"),     
              Task(3,"PQR", 2,"In Progress","Bglr")]

def sort_taskname(tasks):
    return sorted(tasks, key=lambda i: i.taskname)

def sort_priority(tasks):
    return sorted(tasks, key=lambda i: i.priority)

def sort_location(tasks):
    return sorted(tasks, key=lambda i: i.location)

def filter_location(tasks,location):
    return [i for i in tasks if i.location==location]

print("Based on taskname")
a=sort_taskname(tasks)
for i in a:
    print(i)
print()


print("Based on priority")
b=sort_priority(tasks)
for i in b:
    print(i)
print()

print("Based on location")
c=sort_location(tasks)
for i in c:
    print(i)
print()

print("Filtering Based on location")
d=filter_location(tasks,"Cbe")
for i in d:
    print(i)
print()



