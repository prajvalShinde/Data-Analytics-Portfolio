n=int(input("Enter number: "))
print("Palindrome" if str(n)==str(n)[::-1] else "Not palindrome")
