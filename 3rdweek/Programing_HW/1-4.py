n = input("Please enter number: ")

try:
    print (10/int(n))

except ZeroDivisionError:
    print ("Don't divide with 0")

except ValueError:
    print ("Please enter digit")

