# print("welcome ....")
# import random
# a=[1,2,4,3,6,5,7,8,9,]
# list= random.sample(a,5)
# print(list)
# def cowbull():
#     i=0
#     while i< len(list):
#         j=0
#         list3=[]
#         list4=[]
#         while j<5:
#             sec=int(input("enter the sec"))
#             pos=int(input("enter the pos"))
#             if list[pos]==sec:
#                 if sec not in list3:
#                     list3.append(sec)
#                     print(list3)
#                     print("bull")
#                     break
#             elif list[pos]!=sec:
#                 list4.append(pos)
#                 print(list4)
#                 print("cow")
#                 print("losser")
#                 break
#             else:
#                     print("not cow")
#             j=j+1
#         i=i+1
#     print("you are winner")
# cowbull()



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
