import random as rd
import matplotlib.pyplot as plt
from collections import defaultdict

#List for iterating number of people and list for their probability
no_of_people = []
probability = []
x = []
birth_days = []

#input number of persons
print("Enter number of person(s) to check birthday paradox problem: ")
value = int(input())

def gen_random_birthdays(k):
    counts = defaultdict(int)
    for i in range(1,k):
        birthday = rd.randint(1, 365)   #Here not considered as leap year
        counts[birthday] += 1
    return counts

def identify_same_bdays(count_bdays):
    for day in count_bdays.keys():
        birth_days.append(day)
        if count_bdays[day] > 1:
            return True
    return False

def prob_match(size, times):
    match = 0.0
    for i in range(times):
        bday_count = gen_random_birthdays(size)
        if identify_same_bdays(bday_count):
            match += 1.0
    return match / times

for i in range(1,value+1):
    no_of_people.append(i)
    probability.append(prob_match(i,1000))

print("No of people: ",no_of_people)
print("Probability :", probability)
plt.plot(no_of_people,probability, 'ro')
plt.ylabel("Probability of a pair")
plt.xlabel("Number of people")
plt.show()