#Given an array of integers, find a triplet of numbers adding up to a given number

class triplet:
    def find_triplet(x, n_elements, sum):
        #Fix 1st number in array
        for i in range(0, n_elements - 2):
            #Fix 2nd number in array
            for j in range(i+1, n_elements - 1):
                #Fix 3rd number in arary
                for k in range(j+1, n_elements):
                    total = x[i] + x[j] + x[k]
                    if total == sum:
                        print('Triplets are: ',x[i],', ',x[j],' and ',x[k])
        print('No triplets found in the given array :(')

no_of_elements = int(input('How many numbers in an array? '))
print('Enter values one by one')
lst = []
for i in range(no_of_elements):
    num = int(input())
    lst.append(num)
print(lst)
sum_input = int(input('How much should be the sum? '))
print(triplet.find_triplet(lst, no_of_elements, sum_input))