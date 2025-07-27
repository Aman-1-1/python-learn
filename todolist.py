todo=[]
def add(data):
    if not todo:
        todo.insert(0,data)
    else:
        todo.append(data)
def remove(data):
    todo.remove(data)
print ("Enter the action to be Performed")
print ("if u need to create new list just use Add")
tasks =input ("1.Add  \n 2.Remove \n 3.View \n 4.Exit \n")
task=tasks.lower()
if tasks=="1" or tasks=="add" :
    data=input ("Enter the task to be added :")
    add (data)
if task=="2"or task=="remove":
    data=input ("Enter the task to be added :")
    remove(data)
if task=="3" or 