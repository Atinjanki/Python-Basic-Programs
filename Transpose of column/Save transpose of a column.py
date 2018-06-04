import csv 
from itertools import zip_longest

#File also available on Bitbucket
#Create rows
row_one = [1,2,3,4,5,6,7,8,9,10]
row_two = [11,12,13,14,15,16,17,18,19,20]
combined_list = []

combined_list.append(row_one)
combined_list.append(row_two)
print(combined_list)

#zip longest is used for transpose of a column
data = zip_longest(*combined_list)

#Save in a file the values
with open('new_file.csv', 'w', newline='') as f:
    wr = csv.writer(f)
    wr.writerows(data)
    print('\nFile written successfully')
f.close()
