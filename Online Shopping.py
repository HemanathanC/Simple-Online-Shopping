#!/usr/bin/env python
# coding: utf-8

# In[ ]:


items=["Sandisk 16GB",
       "Logitech Mouse",
       "Pendriv16GB",
       "Adidas",
       "Nike",
       "Leecooper"
       ,"Mi Note 3"
       ,"Nokia 3"
       ,"Samung A30"]

c=1;totcost=0;
cost=[355,500,550,3550,5000,2800,11000,9866,12800]
a=[]

for i in range(9):
        a.append(0)
name=input("Please Enter Your Name:")
print("HELLO",name," WELCOME TO ONLINE SHOPPING")
print("\n")

while c==1 or c==2:
    if c==1:
        print("1.Computer Accessories\n2.Shoes\n3.Mobiles\n4.Exit")
        choice=int(input("Select your choice:"))
        
        if choice==1:
            print("1.Sandisk 16GB - Rs.355\n2.Logitech Mouse -    Rs.500\n3.Pendrive 16GB - Rs.550\n4.Exit")
            accessorieschoice=int(input("Choose which you want:"))
            if accessorieschoice==1:
                print("You choose Sandisk 16GB with Rs.355.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[0]+=1
                    totcost+=355
            elif accessorieschoice==2:
                print("You choose Logitech Mouse with Rs.500.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[1]+=1
                    totcost+=500
            elif accessorieschoice==3:
                print("You choose Pendrive 16GB with Rs.550.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[2]+=1
                    totcost+=550
                    
        elif choice==2:
            print("1.Adidas - Rs.3550\n2.Nike - Rs.5000\n3.Leecooper- Rs.2800\n4.Exit")
            shoeschoice=int(input("Choose which you want:"))
            if shoeschoice==1:
                print("You choose Adidas with Rs.3550.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[3]+=1
                    totcost+=3550
            elif shoeschoice==2:
                print("You choose Nike with Rs.5000.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[4]+=1
                    totcost+=5000
            elif shoeschoice==3:
                print("You choose Leecooper with Rs.2800.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[5]+=1
                    totcost+=2800
                    
        elif choice==3:
            print("1.Mi Note 3 - Rs.11000\n2.Nokia 3 - Rs.9866\n3.Samsung A30\n4.Exit")
            mobileschoice=int(input("Choose which you want:"))
            if mobileschoice==1:
                print("You choose Mi Note 3 with Rs.11000.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[6]+=1
                    totcost+=11000
            elif mobileschoice==2:
                print("You choose Nokia 3 with Rs.9866.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[7]+=1
                    totcost+=9866
            elif mobileschoice==3:
                print("You choose Samsung A30 with Rs.12800.")
                n=int(input("Are you want to buy press 1 else any number:"))
                if n==1:
                    a[8]+=1
                    totcost+=12800
                    
    elif c==2:
        Id=int(input("Enter id to delete item:"))
        if Id<9 and Id>=0:
            totcost-=cost[Id]*a[Id]
        a[Id]=0
        
    else:
        exit()
    print(name,"'s Cart")
    print("ID\tITEMS\t\t\tQUANTITY\t\tCOST")
    
    for i in range(9):
        if a[i]!=0:
            print(i,"\t",items[i],"\t\t",a[i],"\t\t\t",cost[i]*a[i])
    print("The Totalcost is ",totcost)
    
    print("If you want to buy anything more Enter \n1.Add item\n2.Delete item\n3.Exit")
    c=int(input())
    
print("Your Final Cost is ",totcost)
print(“\n”)
print("\tTHANKS",name," FOR CHOOSING US AND VISIT US AGAIN")

