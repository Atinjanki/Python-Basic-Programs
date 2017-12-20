#Check if a given string is palindrome or not

#Input from user
input_str = input("Enter a string/number to check if it is a palindrome: ")

#Remove case sensitivity
input_str = input_str.casefold()

#Reverse the string
reversed_str = reversed(input_str)

#Check if given string is equal to its reverse
if list(input_str) == list(reversed_str):
    print("Given string is a palindrome")
else:
    print("Given string is not a palindrome")