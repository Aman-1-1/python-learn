#To give set target value and find that target value by using sum  of the numbers in array
Target = input ("Give an Target Value")

arr = [2,3,4,5,1,0]

length=len (arr)   
for i in range (0,length-1):
   for j in range (i+1,length):
    if arr[i]+arr[j] ==int(Target):
        print (f"arr[{i}] and arr[{j}]")