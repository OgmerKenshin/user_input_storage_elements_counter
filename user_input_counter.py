#set 5 boxes or arrays labeled 1-10, 11-20,etc...
#num = int(input())
#insert a while loop so the input can be repeated
#insert if and elif statements to organize which use input numbers go to which arrays
#else statement's output is how many numbers have been input unto each of the 5 boxes

one_to_10 = []
elevn_to_20 = []
twntyone_to_30 = []
thrtyone_to_40 = []
frtyone_to_50 = []

num = int(input("enter a number here: "))

while True:
    if num > 0 and num < 11:
        print("your input has been placed in the 1-10 box: ")
        one_to_10.append(num)
        num = int(input("input another number:"))
    elif num > 11 and num < 20:
        print("your input has been stored in box 11-20")
        elevn_to_20.append(num)
        num = int(input("input another number:"))
    elif num > 21 and num > 30:
        print("your input has been stored in the 21-30 box")
        twntyone_to_30.append(num)
        num = int(input("input another number:"))