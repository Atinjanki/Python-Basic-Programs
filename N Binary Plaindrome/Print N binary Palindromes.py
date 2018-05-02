#Generate first n binary palindromes

#Generate 99999 binary numbers and then check for palindromes
n = int(input('Input n to print n binary Palindromes: '))
lst = []
palindrome_lst = []
for i in range(99999):
    b = bin(i)[2:]
    l = len(b)
    lst.append(b)

#Check each binary number in list for palindrome
for i in lst:
    reverse_i = reversed(i)
    if list(i) == list(reverse_i):
        palindrome_lst.append(i)
print('First ',n,' binary palindromes are: \n',palindrome_lst[0:n])