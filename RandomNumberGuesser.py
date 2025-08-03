import random

def num_guesser (random_number,attempt):
    Number=input("Enter the number number")
    attempt=attempt+1
    length=len(Number)
    print(f"Attempt {attempt} u can only attempt 5 times")
    if attempt>5:
        exit()
    if length!=3:
        print ("error! enter the right amount of number")
        exit()
    if Number==random_number:
        print ("Number Correct")
        return
    else:
        process(random_number,Number,attempt)
def process(random_number,Number,attempt):
    for i in range(0,3):
        if random_number[i]==Number[i]:
            print(f"{Number[i]} is  in right position")
            
        elif Number[i] in random_number:
            print(f"{Number[i]} is not in right position")
           
    num_guesser(random_number,attempt)
def main():
    random_number=str(random.randint(100,999))
    print (random_number)
    attempt=0
    num_guesser(random_number,attempt)
    
main()