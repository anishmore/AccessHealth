num=int(input("enter no:"))
sum=0

if num < 0:  
   print("Enter a positive number")  
else:  
    for i in range(1,num):
        if i % 3 == 0  or i % 5 == 0:
            print ("!!!",i)
            sum=sum+i


print("===sum",sum)
