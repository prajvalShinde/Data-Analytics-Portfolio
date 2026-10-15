n=int(input("Enter non-negative number: "))
if n<0: print("Not an Armstrong number")
else:
    digits=str(n)
    print("Armstrong" if sum(int(d)**len(digits) for d in digits)==n else "Not Armstrong")
