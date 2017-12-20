#Program to find prime numbers from a list
prime_num_list = []
not_prime_num_list = []

#Get list of numbers from user
num_list=[]
print("How many numbers you need to input? ")
b=int(input())
print("Enter values to check if its prime number or not: ")
for i in range(b):
    c=int(input())
    num_list.append(c)

#Check if the number is prime number or not and return values
def prime_num(num):
    for x in num:
        if x > 0:
        # check for factors
            for i in range(2,x):
                if x==1 or x ==2:
                    prime_num_list.append(x)
                elif (x % i) == 0:
                    not_prime_num_list.append(x)
                    break
            else:
                prime_num_list.append(x)
    print("Prime Numbers in list are: ", prime_num_list)
    print("Not prime numbers in list are: ", not_prime_num_list)
prime_num(num_list)