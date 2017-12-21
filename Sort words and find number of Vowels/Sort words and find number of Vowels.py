#Input from user
input_string = input("Enter the string:")

#Split words and sort them
words = input_string.split()
words.sort()

#Display Sorted words
print("Sorted words are:")
for word in words:
    print(word)

#Find vowels
vowels = 'aeiou'

#Remove case sensitivity
input_string = input_string.casefold()

#Store each vowel in seperate dictionary
count_vowel = {}.fromkeys(vowels,0)

#Count total number of vowels present in string
for each_char in input_string:
    if each_char in count_vowel:
        count_vowel[each_char] += 1
print("\nVowel count(s):\n", count_vowel)