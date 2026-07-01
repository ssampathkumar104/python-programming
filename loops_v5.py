n = int(input())

for i in range(1, n+1):
    pattern = "* "
    print(pattern*i)
for i in range(n-1, 0, -1):
    pattern = "* "
    print(pattern*i)


n = int(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

alphabets_series = alphabets[:n]

for i in range(0, n):
    series = ""
    for j in alphabets_series:
        series = series+ j + " "
    print(series)

n = int(input())

for i in range(1, n+1):
    leading_zeros = "0 "*(n-i)
    trailing_zeros = "0 "*(n-i)
    number_series = "1 "*(2*i-1)
    print(leading_zeros+number_series+trailing_zeros)


n = int(input())

for i in range(1, n+1):
    star_pattern=""
    if i == 1 or i == n:
        star_pattern = "* "*n
    else:
        star_pattern = "  "*(n-1)+"* "
    print(star_pattern)
for j in range(1, n):
    star_pattern = ""
    if j == n-1:
        star_pattern = "* "*n
    else:
        star_pattern = "* "+"  "*(n-1)
    print(star_pattern)


n = int(input())

for i in range(1, n+1):
    star_pattern = ""
    if i == 1 or i == n:
        star_pattern = "* "*n
    else:
        star_pattern = "* "+"  "*(n-1)
    print(star_pattern)
for j in range(1, n):
    star_pattern = ""
    if j == n-1:
        star_pattern = "* "*n
    else:
        star_pattern = "* "+"  "*(n-2)+"* "
    print(star_pattern)
        

n = int(input())

star_pattern = "* "
space_pattern = "  "
for i in range(1, n+1):
    print(star_pattern*i+space_pattern*(2*(n-i))+star_pattern*i)
for j in range(n, 0, -1):
    print(star_pattern*j+space_pattern*(2*(n-j))+star_pattern*j)


n = int(input())

for i in range(1, (2*n+2)):
    if i%n==1:
        print("* "*n)
    else:
        print("* "+"  "*(n-2)+"* ")


n = int(input())

for i in range(1, n+1):
    side_pattern = ". "
    zero_pattern = "0 "
    print(side_pattern*(n-i)+zero_pattern*((2*i)-1)+side_pattern*(n-i))


n = int(input())

for i in range(1, 2*n):
    if i == 1 or i==n or i==2*n-1:
        print("* "*n)
    elif i<n:
        print("* "+"  "*(n-1))
    else:
        print("  "*(n-1)+"* ")


n = int(input())

for i in range(n-1, 0, -1):
    if n%i==0:
        print(i)
        break


m = int(input())
n = int(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

count = 0
for i in range(1, m+1):
    
    if i==1:
        series = ""
        for j in range(0,n):
            series = series +alphabets[count]+" "
            count = count+1
        print(series)
    elif i==m:
        series = ""
        for k in range(0,n):
            series = series +alphabets[count]+" "
            count = count+1
        print(series)
    else:
        series = ""
        for p in range(0, n):
            if p == 0 or p==n-1:
                series = series + alphabets[count]+" "
            else:
                series = series + "  "
            count = count+1
        print(series)


n = int(input())

for i in range(0, n):
    number = int(input())
    if number<0:
        print(number)
        break

n = int(input())

for i in range(0,n):
    number = int(input())
    
    if number %2==0:
        print(number)
        break

sentence = input()

sentence_index = 0
first_word = ""
for char in sentence:
    if char == " ":
        break 
    first_word = first_word + char
    sentence_index = sentence_index + 1 
print(first_word.upper()+sentence[sentence_index:])

word = input()

for char in word:
    if char.isupper():
        print(char)
        break

m = int(input())
n = int(input())
number = max(m,n)
while True:
    if number%m == 0:
        if number%n == 0:
            print(number)
            break
    number  = number+max(m,n)

m = int(input())
n = int(input())

for i in range(min(m,n),0,-1):
    if m%i ==0 and n%i==0:
        print(i)
        break

m = int(input())
n = int(input())

found = False

for num in range(m, n+1):
    if num<2:
        continue
    is_prime = True
    for i in range(2, int(num**0.5)+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        print(num)
        found = True
        break
if not found:
    print("No prime numbers in the given range")


n = int(input())
k = int(input())
count = 0
for i in range(n, 0, -1):
    if n%i==0:
        count = count + 1 
        if count == k:
            print(i)
            break


sentence = input()

sentence_index = 0 
first_word = ""
for char in sentence:
    if char == " ":
        break 
    first_word = first_word+char
print(first_word)

n = int(input())
k = int(input())

count = 0

for i in range(n, 0, -1):
    if n%i == 0:
        count = count + 1 
        if count == k:
            print(i)
            break
else:
    print(1)
        

n = int(input())

# is_prime = False
count = 0

for _ in range(n):
    number = int(input())
    
    if number<2:
        continue
    is_prime = True
    
    for j in range(2, number):
        if number%j==0:
            is_prime=False
            break
    if is_prime:
        print(number)
        break
        

n = int(input())

for _ in range(n):
    number = int(input())
    if number%5!=0:
        print(number)
    else:
        break

n = int(input())

for _ in range(n):
    number = int(input())
    if number%3==0:
        print(number)
        continue

n = int(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(1, n+1):
    series =""
    for j in range(0,i):
        series = series+alphabets[j]+" "
    print("  "*(n-i)+series)
    
m = int(input())
n = int(input())

count_odd = 0
count_even = 0

for i in range(m, n+1):
    if i%2==0:
        count_even = count_even + 1 
    else:
        count_odd = count_odd + 1 
print(count_odd)
print(count_even)

word = input()

count_vowels = 0 
count_consonants = 0
for char in word:
    if char.lower()=="a" or char.lower()=="e" or char.lower()=="i" or char.lower()=="o" or char.lower()=="u":
        count_vowels = count_vowels + 1 
    elif char != " ":
        count_consonants = count_consonants + 1 
print(count_vowels)
print(count_consonants)
        
    
word = input()

count_R=0
count_G=0

for char in word:
    if char=="R":
        count_R = count_R + 1 
    else:
        count_G = count_G + 1 
        
if count_R<count_G:
    print(count_R)
else:
    print(count_G)


n = int(input())

alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

for i in range(1, n+1):
    series = ""
    for j in range(0, i):
        series = series + alphabets[j]+" "
    print(series)


n = int(input())

for i in range(1, n+1):
    series = ""
    for j in range(1, i+1):
        series = series +str(j)
    if i!=1:
        for k in range(i-1, 0, -1):
            series = series + str(k)
    print(series)


word = input()
count_caps = 0
snake_case_word = ""
for char in word:
    if char.isupper() and count_caps==0:
        # char = char.lower()
        snake_case_word = snake_case_word + char.lower()
        count_caps = count_caps + 1
    elif char.isupper() and count_caps>0:
        snake_case_word = snake_case_word + "_" +char.lower() 
    else:
        snake_case_word = snake_case_word + char
print(snake_case_word)
        

n = int(input())
sum_non_primes = 0
for i in range(n):
    number = int(input())
    
    if number<2:
        sum_non_primes = sum_non_primes + number
        continue
    
    for j in range(2, number):
        if number%j==0:
            sum_non_primes = sum_non_primes + number
            break
            
print(sum_non_primes)


n = int(input())

for i in range(0, (2*n)):
    if i<n:
        space_pattern = " "*(i)
        star_pattern = "* "*(n-i)
        print(space_pattern+star_pattern)
    elif i>n:
        star_pattern = "* "*((i-n)+1) # 6
        space_pattern = " "*(n-((i-n)+1))
        print(space_pattern+star_pattern)
