todo=[]
def add(data):
    if not todo:
        todo.insert(0,data)
    else:
        todo.append(data)
    return main()
def remove(data):
    todo.remove(data)
    return main()
def view():
    for todoes in todo:
        print (todoes)
    return main()
def main():
    print ("Enter the action to be Performed")
    print ("if u need to create new list just use Add")
    tasks =input ("1.Add  \n 2.Remove \n 3.View \n 4.Exit \n")
    task=tasks.lower()
    if task=="1" or task=="add" :
        data=input ("Enter the task to be added :")
        add (data)
    if tasks=="2"or task=="remove":
        data=input ("Enter the task to be added :")
        remove(data)
    if task=="3" or task=="view":
        view()
    if task=="4" or task=="exit":
        exit()
main()
