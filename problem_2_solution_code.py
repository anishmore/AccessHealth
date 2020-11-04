num=int(input("enter no:"))

n1, n2 = 0, 1
count = 0
total=0
if num <= 0:
   print("Please enter a positive integer")
elif num == 1:
   print("Fibonacci sequence upto",num,":")
   print(n1)
else:
    print("Fibonacci sequence:")
    while count < num:
        # print(n1)
        n1, n2 = n2, n1 + n2
        if n2 >= 4000000:
            break
        if n2 % 2 == 0:
            total += n2
print(total)
       