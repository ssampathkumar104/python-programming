# Exercise 1: Print 0 n times using while loop
n = int(input())
i=0
while i<n:
    print("0")
    i = i+1 

# Exercise 2: Print numbers from 1 to n
n = int(input())
i=1 

while i<=n:
    print(i)
    i = i+1

# Exercise 3: Print n to n+9 (increment n by 1 in each iteration)
n = int(input())

i = 1 

while i<=10:
    n=n+1
    print(n)
    i=i+1

# Exercise 4: Calculate sum of numbers from 1 to n
n = int(input())

i =1
sum=0
while i<=n:
    sum = sum+i
    i=i+1 
print(sum)

# Exercise 5: Sum n input numbers
numbers = int(input())
i=0
sum=0

while i<numbers:
    sum = sum+int(input())
    i=i+1
print(sum)

# Exercise 6: Print n input numbers
numbers = int(input())
i=0

while i<numbers:
    print(int(input()))
    i=i+1

# Exercise 7: Calculate average of numbers from 1 to n
numbers = int(input())
i=1
sum=0

while i<=numbers:
    sum = sum+i
    i=i+1 
print(sum/numbers)

# Exercise 8: Print numbers from m to n (both inclusive)
m = int(input())
n= int(input())
i = 0

while i<n:
    m = m+1 
    i= i+1 
    print(m)

# Exercise 9: Print numbers from m to n
m = int(input())
n = int(input())

while m<=n:
    print(m)
    m=m+1 

# Exercise 10: Print m rows with n stars per row
m = int(input())
n = int(input())
i=1 

while i<=m:
    pattern = "* "*n 
    print(pattern)
    i=i+1 

# Exercise 11: Print triangle pattern (1 star, 2 stars, ..., n stars)
number = int(input())
i=1 

while i<=number:
    pattern = "*"*i 
    i = i+1 
    print(pattern)

m = int(input())
n = int(input())
i=1 


# Exercise 12: Print m rows with n stars per row (horizontal)
m = int(input())
n = int(input())
i=1 

while i<=m:
    pattern = "*"*n 
    print(pattern)
    i=i+1

# Exercise 13: Print each character of a word on separate line
word = input()

i = 0

while i<len(word):
    print(word[i])
    i = i+1 


# Exercise 14: Print digit pattern (each digit repeated number times)
number = int(input())

i = 1 

while i<=number:
    pattern = str(i)*number
    print(pattern)
    i = i+1 

# Exercise 15: Print first character of word n times
word = input()
n = len(word)
i = 0

while i<n: 
    print(word[0])
    i = i+1
    
# Exercise 16: Print digit repeated by its value (1 once, 2 twice, etc.)
n = int(input())

i = 1
while i<=n:
    print(str(i)*i)
    i = i + 1

# Exercise 17: Duplicate - print digit repeated by its value
i = 1
while i<=n:
    print(str(i)*i)
    i = i + 1
    
# Exercise 18: Print m rows with pattern repeated n times
m = int(input())
n = int(input())

i = 1 

while i<=m:
    pattern = str(i)+" "
    print(pattern*n)
    i = i + 1 

# Exercise 19: Print numbers from 0 to n-1
n = int(input())
i = 0

while i<n:
    print(i)
    i = i+1 

# Exercise 20: Calculate sum of n input numbers and average
n = int(input())
i = 1 #initialization
sum = 0

while i<=n: #condition
    sum = sum + int(input())
    i = i+1 #increment
print(sum/n)

# Exercise 21: Print nested triangle pattern (repeat pattern twice)
n = int(input())

j = 1 
while j<=2:
    i = 1 #initialization
    while i<=n: #condition
        pattern = "* "*i 
        i = i + 1 #increment
        print(pattern)
    j = j+1
    
# Exercise 22: Calculate product of (x+1), (x+2), ..., (x+n)
x = int(input())
n = int(input())
i = 1 
product = 1 
while i<=n:
    product = product*(x+i)
    i = i + 1
print(product)

# Exercise 23: Calculate sum of squares from 1 to n
n = int(input())

i = 1 
sum_of_squares = 0
while i<=n:
    sum_of_squares = sum_of_squares+(i**2)
    i = i+1 
print(sum_of_squares)

# Exercise 24: Print numbers from n down to 1
n=int(input())

while n>0:
    print(n)
    n = n-1

# Exercise 25: Print numbers from 1 to n using for loop
number = int(input())

for num in range(1,number+1):
    print(num)
    
# Exercise 26: Print cubes from 1^3 to n^3
number = int(input())

for num in range(1, number+1):
    print(num**3)

# Exercise 27: Calculate sum from 0 to n
number = int(input())
sum = 0

for num in range(number+1):
    sum = sum + num 
print(sum)


# Exercise 28: Calculate average from 1 to n
number = int(input())

sum = 0
for num in range(1,number+1):
    sum = sum + num 
print(sum/number)

# Exercise 29: Print first character n times
word = input()

for num in range(len(word)):
    print(word[0])

# Exercise 30: Calculate product of n input numbers
numbers_count = int(input())

product = 1
for num in range(numbers_count):
    product = product*int(input())
print(product)

# Exercise 31: Print n input numbers
numbers_count = int(input())

for num in range(numbers_count):
    print(int(input()))

# Exercise 32: Join characters of string with dashes
a = input()
len_of_a = len(a)
b = ""
for i in range(len_of_a):
    if i == 0:
        b = b + a[i]
    else:
        b = b + "-" + a[i]
print(b)

# Exercise 33: Print triangle pattern (1 star, 2 stars, ..., n stars)
number = int(input())

for num in range(1, number+1):
    pattern = "*"*num
    print(pattern)

# Exercise 34: Print inverted pyramid pattern
number = int(input())

for num in range(1, number+1):
    pattern = "* "*(number-1)+"*"
    print(pattern)

# Exercise 35: Print digits with pattern repeated
number = int(input())


for num in range(1, number+1):
    pattern = str(num)+" "
    print(pattern*num)

# Exercise 36: Print each digit repeated n times
number = int(input())

for num in range(1, number+1):
    print(str(num)*number)

# Exercise 37: Sum numbers from m to n
m = int(input())
n = int(input())

sum = 0
for num in range(m, n+1):
    sum = sum+num
print(sum)

# Exercise 38: Print pattern with + at end
number = int(input())


for num in range(1, number):
    pattern = "* "
    print(pattern*num)
print("+ "*number)

# Exercise 39: Print nested digit pattern (repeat twice)
number = int(input())

for iter in range(2):
    for num in range(1,number+1):
        print(str(num)*num)

# Exercise 40: Print m rows with pattern repeated n times
m = int(input())
n = int(input())

for num in range(1, m+1):
    pattern = str(num)+" "
    print(pattern*n)

# Exercise 41: Print numbers from 0 to n
number = int(input())

for num in range(number+1):
    print(num)


# Exercise 42: Calculate average of n input numbers
number = int(input())

sum = 0
for num in range(number):
    sum = sum + int(input())
print(sum/number)

# Exercise 43: Print nested triangle pattern (repeat twice)
number = int(input())

for nu in range(2):
    for num in range(1,number+1):
        pattern = "* "*num
        print(pattern)

# Exercise 44: Calculate product of numbers from m to n
m = int(input())
n = int(input())
product = 1 

for num in range(m, n+1):
    product = product*num
print(product)


# Exercise 45: Calculate sum of squares from 1 to n
number = int(input())

sum = 0

for num in range(1, number+1):
    sum = sum + num**2
print(sum)


# Exercise 46: Print numbers from n down to 1
number = int(input())


for num in range(number):
    print(number-num)


# Exercise 47: Print m rows with + pattern
m = int(input())
n = int(input())

for num in range(1, m+1):
    pattern = "+ "*n 
    print(pattern)

# Exercise 48: Print nested triangle pattern (repeat twice)
number = int(input())


for nu in range(2):
    for num in range(1,number+1):
        pattern = "* "*num 
        print(pattern)

# Exercise 49: Calculate sum of squares from m to n
m = int(input())
n = int(input())

sum = 0
for num in range(m, n+1):
    sum = sum + num**2
print(sum)

# Exercise 50: Sum of even numbers from m to n
m = int(input())

n = int(input())

sum = 0
for num in range(m, n+1):
    if num%2 == 0:
        sum = sum + num

print(sum)

# Exercise 51: Product of odd numbers from m to n
m = int(input())
n = int(input())

product = 1

for num in range(m, n+1):
    if num%2 == 1:
        product = product*num 
    
print(product)

# Exercise 52: Calculate factorial of n
n = int(input())

fact = 1
for num in range(n):
    fact = fact * (n-num)
print(fact)


# Exercise 53: Calculate sum of digits of a number
n = int(input())

sum = 0
for digit in str(n):
    sum = sum + int(digit)
print(sum)

# Exercise 54: Print odd numbers from m to n
m = int(input())
n = int(input())

sum = ""
for num in range(m, n+1):
    if num%2==1:
        sum = sum+str(num)+" "

print(sum)


# Exercise 55: Sum and average of 10 input numbers
sum = 0
for num in range(10):
    sum = sum + int(input())
print(sum)
print(sum/10)

# Exercise 56: Print digits with spaces
number = int(input())

digit_str = ""
for digit in str(number):
    digit_str = digit_str + digit + " "
print(digit_str)


# Exercise 57: Print multiples of t from 1 to n
n = int(input())
t = int(input())

for num in range(1,n+1):
    if num%t == 0:
        print(num)

# Exercise 58: Print inverted triangle pattern (n stars down to 0)
n = int(input())

for num in range(n+1):
    pattern = "* "*(n-num)
    print(pattern)

# Exercise 59: Print characters that are 'a' or 'z'
word = input()

for char in word:
    if char == "z" or char == "a":
        print(char)

# Exercise 60: Count numbers divisible by both 2 and 3 (from 1 to n)
n = int(input())

count = 0
for num in range(1, n+1):
    if num%2==0 and num%3==0:
        count = count + 1 
print(count)

# Exercise 61: Print vowels from a word
word = input()

for char in word:
    if char == "a" or char == "e" or char == "i" or char == "o" or char == "u":
        print(char)

# Exercise 62: Print numbers from n down to m (reverse order)
m = int(input())
n = int(input())

for num in range(n, m-1, -1):
            print(num)

# Exercise 63: Print pattern with decreasing digits
n = int(input())


for digit in range(n+1):
    pattern = str((n-digit))+" " 
    print(pattern*(n-digit))

# Exercise 64: Print word in reverse
word = input()

for index in range(len(word)-1, -1, -1):
    print(word[index])

# Exercise 65: Print odd numbers from n down to m (reverse order)
m = int(input())
n = int(input())

print_pattern = ""

for num in range(n, m-1, -1):
    if num%2==1:
        print_pattern = print_pattern + str(num) +" "
print(print_pattern)

# Exercise 66: Product of numbers divisible by 3 from m to n
m = int(input())
n = int(input())

product = 1 
for num in range(m, n+1):
    if num%3==0:
        product = product*num 
print(product)

# Exercise 67: Calculate sum of k-th powers (0^k + 1^k + ... + n^k)
n = int(input())
k = int(input())

sum = 0

for num in range(n+1):
    sum = sum + num**k 
print(sum)

# Exercise 68: Count numbers divisible by both 6 and 8 from 1 to n
n = int(input())

count = 0

for num in range(1,n+1):
    if num%6==0 and num%8==0:
        count = count+1
print(count)   
     
# Exercise 69: Print diamond-like pattern with stars and plus signsn = int(input())
n = int(input())
first_pattern = "* "*n
print(first_pattern)
for num in range(1,n):
    print_pattern = "+ "*(n-num)
    print(print_pattern)

# Exercise 70: Print triangle then inverted triangle
n = int(input())

for num in range(1, n+1):
    first_pattern = "* "*num
    print(first_pattern)
for num in range(0, n+1):
    first_pattern = "* "*(n-num)
    print(first_pattern)

# Exercise 71: Calculate n to the power of m (n^m)
n = int(input())
m = int(input())

product = 1
for num in range(m):
    product = product * n
print(product)

# Exercise 72: Duplicate - product of numbers from m to n
m = int(input())
n = int(input())

product = 1 

for num in range(m, n+1):
    product = product*num 
print(product)

