import random
print("welcome")
def cowbull():
    a=[0,1,2,3,4,5,6,7,8,9]
    list=random.sample(a,5)
    print(list)
    cow=0
    bull=0
    cow=[]
    bull=[]
    for i in range(5):
        if bull==list:
            print("you are winner")
            play=input("do you want to play y or n")
            if play=="y":
                cowbull()
            if play=="n":
                print("this  is finished")
                break
        guess_number=int(input("enter the...."))
        position_number=int(input("enter the...."))
        for i in list:
            if guess_number  in list:
                if guess_number in list and list.index(guess_number)==position_number:
                    bull.insert(position_number,guess_number)
                    print("bull",bull)
                    break
                else:
                    cow.insert(position_number,guess_number)
    
                    print("cow",cow)
                    break    
        else:
            print("you are losser")
            break
    else:
        print("you are winner")
       
cowbull()