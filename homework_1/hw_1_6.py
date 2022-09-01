f = int(input("Enter a number that is both positive and whole: \n"))

def factorial(f):
    
    if f == 1 :
     
        return 1
    
    else:

        return f * factorial(f - 1)

print("The factorial of the number", f, "is", factorial(f))
