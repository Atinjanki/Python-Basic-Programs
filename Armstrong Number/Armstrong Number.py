#Input from user
number = input("Enter a number: ")
int_number = int(number)    #Conversion of string to integer
len_num = len(number)       #Length of number
sum = 0

temp = int_number
while temp > 0:
    digit = temp % 10
    sum += digit ** len_num
    temp //= 10     #Floor division

if int_number == sum:
    print("Entered number is an Armtrong number")
else:
    print("Entered number is not an Armtrong number")