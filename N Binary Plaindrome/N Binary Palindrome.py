#Generate n binary numbers (take input from user)
n = int(input('How many binary numbers do you need? '))
lst = []
palindrome_lst = []
for i in range(n):
    b = bin(i)[2:]
    l = len(b)
    lst.append(b)
print('All ',n, ' binary numbers are', lst)

#Check each binary number in list for palindrome
for i in lst:
    reverse_i = reversed(i)
    if list(i) == list(reverse_i):
        palindrome_lst.append(i)
print('In the above list palindrome binary numbers are: ',palindrome_lst)