n=int(input("Enter a Number : "))

for i in range(1,n+1):
    value=i*i
    if i%2==0:
        value=-value
    print(value, end=" ")