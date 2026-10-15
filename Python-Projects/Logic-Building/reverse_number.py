n=int(input("Enter number: "))
sign=-1 if n<0 else 1
reverse=int(str(abs(n))[::-1]) * sign
print("Reverse:",reverse)
