n=int(input("Enter non-negative number: "))
if n<0: print("Factorial is undefined for negative numbers")
else:
    result=1
    for i in range(2,n+1): result*=i
    print("Factorial:",result)
