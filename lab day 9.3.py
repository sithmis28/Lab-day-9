even_count=0
odd_count=0
count=0
while count<5:
    num=int(input("enter your number"))
    if num % 2==0:
        even_count=even_count+1

    else:
        odd_count=odd_count+1
    count=count+1
print("odd_count is",odd_count)
print("even_count is",even_count)
