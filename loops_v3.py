# Exercise 1: Convert input string to lowercase
string = input()

print(string.lower())

# Exercise 2: Strip leading and trailing whitespace from input
S = input()
print(S.strip())

# Exercise 3: Replace '-' with '/' in a date string
date = input()
print(date.replace('-', '/'))

# Exercise 4: Check if the input string is numeric
word = input()
print(word.isdigit())

# Exercise 5: Check if the input string is all uppercase
word = input()
print(word.isupper())

# Exercise 6: Remove '-', '@', and '#' characters from the string
word = input()

word = word.replace('-', '')
word = word.replace('@', '')
print(word.replace('#', ''))

# Exercise 7: Extract all uppercase letters from the string
word = input()

upp = ''
for i in word:
	if i.isupper():
		upp = upp + i
print(upp)

# Exercise 8: Check if URL starts with 'https://'
url = input()

print(url.startswith('https://'))

# Exercise 9: Check if filename ends with '.py'
file_name = input()

print(file_name.endswith('.py'))

# Exercise 10: Swap case of letters in the string
word = input()
print(word.swapcase())

# Exercise 11: Validate password has at least one uppercase letter
password = input()

is_valid = ''

for i in password:
	if i.isupper():
		is_valid = is_valid + i
if len(is_valid) > 0:
	print('Valid Password')
else:
	print('Invalid Password')

# Exercise 12: Case-insensitive palindrome check
word = input()
word = word.lower()
rev_word = ''
for i in range(len(word)-1, -1, -1):
	rev_word = rev_word + word[i]
print(word == rev_word)

# Exercise 13: Validate password contains upper, lower, and digit
password = input()

upper_count = 0
lower_count = 0
digit_count = 0

for i in password:
	if i.isupper():
		upper_count = upper_count + 1
	if i.islower():
		lower_count = lower_count + 1
	if i.isdigit():
		digit_count = digit_count + 1

if upper_count >= 1 and lower_count >= 1 and digit_count >= 1:
	print('Valid Password')
else:
	print('Invalid Password')

# Exercise 14: Insert space before uppercase letters (split camel case)
word = input()

modified_word = ''

for i in range(0, len(word)):
	if i != 0:
		if word[i].isupper():
			modified_word = modified_word + ' ' + word[i]
		else:
			modified_word = modified_word + word[i]
	else:
		modified_word = modified_word + word[i]
print(modified_word)

# Exercise 15: Case-insensitive palindrome check (simple)
word = input()
word = word.lower()
rev_word = ''
for i in range(len(word)-1, -1, -1):
	rev_word = rev_word + word[i]

if word == rev_word:
	print('Palindrome')
else:
	print('Not a Palindrome')

# Exercise 16: Palindrome check ignoring spaces and apostrophes
word = input()
word = word.lower()
word = word.replace(' ', '')
word = word.replace("'", '')

rev_word = ''

for i in range(len(word)-1, -1, -1):
	rev_word = rev_word + word[i]

print(word == rev_word)

# Exercise 17: Remove all vowels from the string
word = input()

word = word.replace('a', '')
word = word.replace('e', '')
word = word.replace('i', '')
word = word.replace('o', '')
word = word.replace('u', '')
word = word.replace('A', '')
word = word.replace('E', '')
word = word.replace('I', '')
word = word.replace('O', '')
word = word.replace('U', '')
print(word)

# Exercise 18: Check if S1 starts with or ends with S2
S1 = input()
S2 = input()

if S1.startswith(S2) or S1.endswith(S2):
	print('True')
else:
	print('False')

# Exercise 19: Classify a single character as letter/digit/special
char = input()

if char.islower():
	print('Lowercase Letter')
elif char.isupper():
	print('Uppercase Letter')
elif char.isdigit():
	print('Digit')
else:
	print('Special Character')
	
word = input()
for i in range(1,len(word)+1):
    print(word[:i])
	
word = input()
suffle_word = ""
for i in range(0, len(word)):
    index = int(input())
    suffle_word = suffle_word + word[index]
print(suffle_word)
    

number = int(input())
for i in range(0, number):
    pattern = str(str(i)+" ")*number
    print(pattern)

number = int(input())

factors = 0

for i in range(2, number):
    if number%i == 0:
        factors = factors + 1 
        
if factors > 0:
    print("Not a Prime Number")
else:
    print("Prime Number")

number = int(input())

even_count = 0
for i in range(0, len(str(number))):
    if int(str(number)[i])%2==0:
        even_count = even_count + 1 
        
if even_count>2:
    print("Count of even digits is greater than two")
else:
    print("Count of even digits is not greater than two")

number = int(input())
star_pattern = "* "

for i in range(1,number+1):
    print(star_pattern*((2*i)-1))


number = int(input())

for i in range(0, number+2):
    if i == 0 or i == number+1:
        minus_pattern = "- "
        print("+ "+minus_pattern*number+"+")
    else:
        print("| "+"  "*number+"|")	


m = int(input())
n = int(input())



for i in range(1, m+1):
    series = ""
    for j in range(1, n+1):
        series = series+str(j)+" "
    print(series)
	

s = int(input())
n = int(input())

for i in range(1, n+1):
    series = ""
    for j in range(s, s+n):
        series = series + str(j)+" "
    print(series)
	
word = input()
modified_word = ""
for i in range(0, len(word)):
    if i != 0 and str(word[i]).isupper():
        modified_word = modified_word + "-"+word[i]
    else:
        modified_word = modified_word +word[i]
print(modified_word.lower())


number = int(input())

count_zero = 0
for i in range(0, len(str(number))):
    if str(number)[i] == "0":
        count_zero = count_zero + 1
        
if count_zero>3:
    print("Count of zeroes is greater than three")
else:
    print("Count of zeroes is not greater than three")
	
word = input()

for i in range(len(word), 0, -1):
    print(word[:i])
	

number = int(input())

for i in range(number, 0, -1):
    star_pattern = "* "*((2*i)-1)
    space_pattern = "  "*(2*(number-i))
    print(space_pattern+star_pattern)


sentence1 = input()
sentence2 = input()
new_sentence = ""
for i in range(0, len(sentence1)):
    if i%2==0:
        new_sentence = new_sentence+sentence1[i]
    else:
        new_sentence = new_sentence+sentence2[i]
print(new_sentence)

number = int(input())

sum_even = 0
for i in range(1, number+1):
    if i%2==0:
        sum_even = sum_even + i 
print(sum_even)


number = int(input())

sum_odd = 0
for i in range(1, number+1):
    if i%2==1:
        sum_odd = sum_odd + i 
print(sum_odd)


number = int(input())

factors_count = 0

for i in range(2, number+1):
    if number%i == 0 and i !=number:
        factors_count = factors_count + 1 
print(factors_count>0)

m = int(input())
n = int(input())

for i in range(0, m):
    if i%2 == 0:
        print("+ "*n)
    else:
        print("- "*n)


m = int(input())
n = int(input())

for i in range(0, m+2):
    if i == 0 or i == m+1:
        start_plus_pattern = "+"
        hyphen_pattern = "-"
        end_plus_pattern = "+"
        print(start_plus_pattern+hyphen_pattern*n+end_plus_pattern)
    else:
        start_pipe_pattern = "|"
        space_pattern = " "
        end_pipe_pattern = "|"
        print(start_pipe_pattern+space_pattern*n+end_pipe_pattern)


number = int(input())

for i in range(1, number+1):
    series = ""
    for j in range(1, i+1):
        series = series + str(j)+" "
    print(series)


number = int(input())


for i in range(1, number+1):
    sum = 0
    for j in range(0, len(str(i))):
        sum = sum + int((str(i)[j]))**len(str(i))
    if sum == i:
        print(i)

number = int(input())

for i in range(1, number+1):
    series = ""
    for j in range(1, number+1):
        series = series + str(j) + " "
    print(series)

s = int(input())
n = int(input())

for i in range(1, n+1):
    series = ""
    spaces = " "*(n-i)
    for j in range(s, s+i):
        series = series + str(j) + " "
    print(spaces+series)
        
number = int(input())

num = 1
for i in range(1, number+1):
    series = ""
    for j in range(i):
        series = series + str(num)+" "
        num = num + 1
    print(series)   

m = int(input())
n = int(input())

num = 1
for i in range(1,m+1):
    series = ""
    for j in range(1, n+1):
        series = series+str(num)+" "
        num = num + 1
    print(series)

number = int(input())

for i in range(number, 0, -1):
    series = ""
    # number = 1
    for j in range(1, i+1):
        series = series + str(j) + " "
    print(series)


m = int(input())
n = int(input())

series = ""
for i in range(m, n+1):
    fact = 0
    for j in range(2, i-1):
        if i%j == 0:
            fact = fact + 1 
    if fact == 0:
        print(i)

number = int(input())


for i in range(2, number+1):
    fact = 0
    for j in range(2, i+1):
        if i%j == 0 and i!=j:
            fact = fact + 1 
    if fact == 0:
        print(i)


m = int(input())
n = int(input())

prime = ""
count = 0 
for i in range(m, n+1):
    fact = 0
    if i != 1:
        for j in range(2, i-1):
            if i%j==0:
                fact = fact + 1 
        if fact == 0:
            prime = prime + str(i) + " "
            count = count + 1

if count>0:
    print(prime)
else:
    print("No Prime Numbers Found")


