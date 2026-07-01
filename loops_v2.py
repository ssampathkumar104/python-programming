# Exercise 1: Sum of all factors of a given number
number = int(input())

sum_of_factors = 0

for num in range(1, number+1):
    if number%num == 0:
        sum_of_factors = sum_of_factors + num
print(sum_of_factors)

# Exercise 2: Reverse a string
word = input()

reverse_str = ""
for index in range(len(word)-1, -1, -1):
    reverse_str = reverse_str + word[index]
    
print(reverse_str)

# Exercise 3: Print multiplication table for a number (1 to 10)
number = int(input())

for num in range(1, 11):
    pattern = str(number)+" x "+str(num)+" = "+str(number*num)
    print(pattern)

# Exercise 4: Check if a number is an Armstrong number (n-digit)
number = int(input())

sum = 0

for num in range(len(str(number))):
    sum = sum + int(str(number)[num])**len(str(number))
if sum==number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Exercise 5: Read `number` inputs and print the greatest
number = int(input())

greatest_number = 0

for iter in range(number):
    num = int(input())
    if num>greatest_number:
        greatest_number = num
print(greatest_number)

# Exercise 6: Print all factors of a number in a single line
number = int(input())

factors_pattern = ""
for num in range(1, number+1):
    if number%num == 0:
        factors_pattern = factors_pattern+str(num)+" "
print(factors_pattern)

# Exercise 7: Check if a number is a perfect number (sum of proper factors equals number)
number = int(input())

factors_sum = 0
for num in range(1, number):
    if number%num == 0:
        factors_sum = factors_sum + num
if factors_sum == number:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
    
# Exercise 8: Print repeated '2' pattern ("2", "22", "222", ...)
number = int(input())

for num in range(1, number+1):
    pattern = "2"*num
    print(pattern)

number = int(input())
# Exercise 11: Print numbers in groups of 10 per line up to `number` (space-separated)
number = int(input())

hundred_pattern = ""
for num in range(1, number+1):
    hundred_pattern = hundred_pattern + str(num) + " "
    if num%10 == 0:
        print(hundred_pattern)
        hundred_pattern = ""
        
# Exercise 12: Count digits in a number
number = int(input())

count = 0
while number>0:
    count = count + 1
    number = number//10
print(count)

word = input()
count = 0

for char in word:
    if char=="a" or char=="e" or char=="i" or char=="o" or char=="u":
        count = count + 1 
if count>2:
    print("String has more than two vowels")
else:
    print("String doesn't have more than two vowels")

number = int(input())

count = 0
for num in range(2, 10):
    if number%num == 0:
        count=count+1
if count>0:
    print("Divisible Number")
else:
    print("Indivisible Number")

number = int(input())

smallest_number = 0

for num in range(number):
    if num == 0:
        smallest_number = int(input())
    else:
        second_number = int(input())
        if smallest_number>=second_number:
            smallest_number = second_number
print(smallest_number)

m = int(input())
n = int(input())

count = 0
pattern_str = ""
for num in range(m, n+1):
    if num%6 == 0:
        count = count+ 1
        pattern_str = pattern_str+str(num)+" "

if count>0:
    print(pattern_str)
else:
    print("No Numbers Found")

m = int(input())
n = int(input())

single_digit_count = 0
double_digit_count = 0
for num in range(m, n+1):
    if num<=9:
        single_digit_count = single_digit_count+1 
    if num>=10:
        double_digit_count = double_digit_count+len(str(num))
print(single_digit_count+double_digit_count)

x = int(input())
numbers = int(input())
sum = 0
for num in range(1, numbers+1):
    if num%2!=0:
        sum = sum + (x)**(2*num)
    else:
        sum = sum - (x)**(2*num)
print(sum)

number = int(input())

for num in range(number, 0, -1):
    pattern = " "*(num-1)+"*"*(number-(num-1))
    print(pattern)

number = int(input())

for num in range(number, 0, -1):
    pattern = "  "*(num-1)+"* "*(number-(num-1))
    print(pattern)

number = int(input())

for num in range(0, number):
    pattern = " "*num+str(number-num)*(number-num)
    print(pattern)

number = int(input())

for num in range(0, number+1):
    pattern = "  "*num + str(str(number-num)+" ")*(number-num)
    print(pattern)

number = int(input())

for num in range(1, number+1):
    pattern = "  "*(number-num)+"* "*(2*num-1) 
    print(pattern)

number = int(input())

for num in range(1, number+1):
    pattern = " "*(num-1)+"*"*(2*(number-num)+1)+" "*(num-1)
    print(pattern)

number = int(input())

for num in range(1, number+1):
    pattern = "  "*(number-num)+str(str(num)+" ")*(2*num-1)
    print(pattern)


number = int(input())

for num in range(1, number+1):
    pattern = " "*(number-num)+str(str(num)+" ")*num
    print(pattern)

number = int(input())

for i in range(1, number+1):
    spaces = " "*(number-i)
    stars = "* "*i 
    print(spaces+stars)

for i in range(number-1, 0, -1):
    spaces = " "*(number-i)
    stars = "* "*i
    print(spaces+stars)


number = int(input())

for i in range(1, number+1):
    pattern = "* "
    print(pattern*i)
for i in range(number-1, 0, -1):
    pattern = "* "
    print(pattern*i)

number = int(input())

initial_pattern = "+ "
print(initial_pattern*number)

for i in range(1, number):
    spaces = " "*i 
    stars = "* "*(number-i)
    print(spaces+stars)

number = int(input())

for i in range(1, number+1):
    spaces = "  "*(2*(number-i))
    stars = "* "*i 
    print(stars+spaces+stars)

number = int(input())

for i in range(1, number+1):
    spaces = " "*(number-i)
    stars = "* "*i 
    print(spaces+stars+(2*spaces)+stars)

number = int(input())


for i in range(1, number+1):
    stars = "* "*i 
    spaces = "  "*(2*(number-i))
    print(stars+spaces+stars)
for i in range(number-1, 0, -1):
    stars = "* "*i 
    spaces = "  "*(number-i)
    print(stars+2*spaces+stars)

number = int(input())
og_pattern = "  "*(number-1)+"#"
print(og_pattern)
for i in range(1, number):
    default_pattern = "#"
    space_pattern = "  "*((number-1)-i)
    plus_pattern = "+ "*i 
    print(space_pattern+plus_pattern+default_pattern)

for i in range(number-2, 0,-1):
    default_pattern = "#"
    space_pattern = "  "*((number-1)-i)
    plus_pattern = "+ "*i 
    print(space_pattern+plus_pattern+default_pattern)
print(og_pattern)

# Exercise 9: Print pattern where each line i contains the digit i repeated i times
number = int(input())

for num in range(1, number+1):
    print(str(num)*num)

# Exercise 10: Count how many of the next `number` inputs are positive
number = int(input())

count = 0
for num in range(number):
    if int(input())>0:
        count = count + 1
print(count)
count = 0

for i in range(1, number+1):
    count = count + len(str(i))
print(count)

x = int(input())
n = int(input())

sum = 0
term = 0
for i in range(1,n+1):
    if i%2==1:
        term = x**(1+(2*(i-1)))
    else:
        term = -(x**((2*i)-1))
    sum = sum+term
print(sum)

number = int(input())
factors = 2

for i in range(1,number+1):
    if number%i==0:
        factors = factors + 1

if factors>2:
    print("Number has more than 2 factors")
else:
    print("Number doesn't have more than 2 factors")

number = int(input())

for i in range(1, number+1):
    pattern = "* "*i 
    print(pattern)
for i in range(1, number+1):
    pattern = "* "*i 
    print(pattern)

number = int(input())

for i in range(1, number+1):
    spaces = " "*(number-i)
    number_pattern = str(str(i)+" ")*i
    print(spaces+number_pattern)
for i in range(number-1, 0,-1):
    spaces = " "*(number-i)
    number_pattern = str(str(i)+" ")*i
    print(spaces+number_pattern)
    

number = int(input())

for i in range(number, 0, -1):
    star_pattern = "* "*i
    spaces = "  "*(number-i)
    print(spaces+star_pattern)

number = int(input())

for i in range(number, 0, -1):
    star_pattern = "* "
    if i == number:
        print(star_pattern*((2*number)-1))
    else:
        side_space_pattern = " "*(number-i)
        mid_space_pattern = " "*(2*(number-1-i))
        print(side_space_pattern+star_pattern*i+mid_space_pattern+star_pattern*i+side_space_pattern)
        
number = int(input())

for i in range(1, number+1):
    if i==1 or i==number:
        star_pattern = "* "*number
        print(star_pattern)
    else:
        star_pattern = "* "
        spaces_pattern = "  "*(number-2)
        print(star_pattern+spaces_pattern+star_pattern)

m = int(input()) #rows
n = int(input()) #columns

for i in range(1,m+1):
    if i == 1 or i==m:
        star_pattern = "* "*n
        print(star_pattern)
    else:
        spaces_pattern = "0 "*(n-2)
        star_pattern = "* "
        print(star_pattern+spaces_pattern+star_pattern)

number = int(input())

for i in range(1, number+1):
    star_pattern = "* "
    if i == 1 or i==2:
        print(star_pattern*i)
    elif i==number:
        print(star_pattern*number)
    else:
        space_pattern = "  "*(i-2)
        print(star_pattern+space_pattern+star_pattern)
        
number = int(input())

for i in range(1, number+1):
    sign_pattern = ". "
    if i == 1 or i==2:
        print(sign_pattern*i)
    elif i == number:
        print(sign_pattern*number)
    else:
        digit_pattern = "0 "*(i-2)
        print(sign_pattern+digit_pattern+sign_pattern)
        
number = int(input())

minus_pattern = "_"
pipe_pattern = "|"
fwd_slash_pattern = "/"

print(minus_pattern*(number+1))
for i in range(number, 0, -1):
    print(pipe_pattern+" "*(i-1)+fwd_slash_pattern)

number = int(input())
star_pattern = "* "
space_pattern = "  "
for i in range(1, number+1):
    if i == 1 or i == 2:
        print(space_pattern*(number-i)+star_pattern*i)
    elif i == number:
        print(star_pattern*number)
    else:
        print(space_pattern*(number-i)+star_pattern+space_pattern*(i-2)+star_pattern)


number = int(input())

for i in range(1, number):
    space_pattern = " "*(number-i)
    mid_space = " "*(2*(i-1)-1)
    star_pattern = "*"
    if i == 1:
        print(space_pattern+star_pattern+space_pattern)
    else:
        print(space_pattern+star_pattern+mid_space+star_pattern+space_pattern)
print("* "*number)

number = int(input())

print("# "*number)

for i in range(number-1, 0, -1):
    plus_pattern = "+ "
    space_pattern = "  "
    if i==1:
        print(plus_pattern)
    else:
        print(plus_pattern+space_pattern*(i-2)+plus_pattern)

number = int(input())

for i in range(number, 0, -1):
    if i==1:
        print("  "*(number-1)+"* ")
    elif i==number:
        print("* "*number)
    else:
        print("  "*(number-i)+"* "+"  "*(i-2)+"* ")

number = int(input())

for i in range(1, number+1):
    if i == 1:
        print(str(i)*i)
    else:
        print(str(i)+" "*(2*(i-1)-1)+str(i))

for i in range(number-1, 0, -1):
     if i == 1:
        print(str(i)*i)
     else:
         print(str(i)+" "*(2*(i-1)-1)+str(i))


number = int(input())

for i in range(1, number+1):
    space_pattern = " "*(number-i)
    star_pattern = "*"
    mid_space_pattern = " "*((2*(i-1))-1)
    if i==1:
        print(space_pattern+star_pattern+space_pattern)
    else:
        print(space_pattern+star_pattern+mid_space_pattern+star_pattern+space_pattern)
for i in range(number-1, 0,-1):
    space_pattern = " "*(number-i)
    star_pattern = "*"
    mid_space_pattern = " "*((2*(i-1))-1)
    if i==1:
        print(space_pattern+star_pattern+space_pattern)
    else:
        print(space_pattern+star_pattern+mid_space_pattern+star_pattern+space_pattern)


number = int(input())

for i in range(1, number+1):
    if i==1:
        print(" "*(2*(number-i))+str(i))
    else:
        front_space_pattern = " "*(2*(number-i))
        mid_spaces_pattern = " "*(2*(i-1)-1)
        print(front_space_pattern+str(i)+mid_spaces_pattern+str(i))
for i in range(number-1, 0,-1):
    if i==1:
        print(" "*(2*(number-i))+str(i))
    else:
        front_space_pattern = " "*(2*(number-i))
        mid_spaces_pattern = " "*(2*(i-1)-1)
        print(front_space_pattern+str(i)+mid_spaces_pattern+str(i))
        
number = int(input())

for i in range(1, number+1):
    
    top_mid_space = "  "*(2*(number-i))
    side_mid_space = "  "*(i-2)
    if i==1:
        print("* "+top_mid_space+"*")
    elif i == number:
        print("* "*(2*number))
    else:
        print("* "+side_mid_space+"* "+top_mid_space+"* "+side_mid_space+"*")


number = int(input())

for i in range(1, number+1):
    mid_space = "  "*(2*(number-i))
    side_space = " "*(2*(i-2))
    if i == 1:
        print("* "+mid_space+"*")
    else:
        print("* "+side_space+"* "+mid_space+"*"+side_space+" *")

for i in range(number, 0,-1):
    mid_space = "  "*(2*(number-i))
    side_space = " "*(2*(i-2))
    if i == 1:
        print("* "+mid_space+"*")
    else:
        print("* "+side_space+"* "+mid_space+"*"+side_space+" *")

a = int(input())
b = int(input())

root_a = int(a**0.5)
root_b = int(b**0.5)
count = 0
for i in range(root_a, root_b+1):
    if a<=i**2<=b:
        count = count+1 
print(count)
# Exercise: Count perfect squares between `a` and `b` (inclusive)
# Reads `a` and `b`, computes sqrt range and counts integer squares in range

number = int(input())

for i in range(1, number+1):
    space_pattern = " "*(number-i)
    if i == 1:
        print(space_pattern+"*")
    else:
        print(space_pattern+"* "*(i-1)+"*")
for i in range(number-1, 0, -1):
    space_pattern = " "*(number-i)
    if i == 1:
         print(space_pattern+"*")
    else:
        print(space_pattern+"*"+" "*((2*(i-1))-1)+"*")
        
# Exercise: Hollow pyramid (up then down)
# Prints a hollow pyramid of '*' characters, then mirrors it

number = int(input())


for i in range(1, number+1):
    space_pattern = " "*(number-i)
    if i == 1:
        print(space_pattern+"*")
    else:
        print(space_pattern+"* "*(i-1)+"*")
for i in range(number-1, 0, -1):
    space_pattern = " "*(number-i)
    if i == 1:
         print(space_pattern+"*")
    else:
        print(space_pattern+"*"+" "*((2*(i-1))-1)+"*")
        
# Exercise: Wide spaced pyramid (centered vertically)
# Prints a pyramid with doubled leading spaces to create a wider vertical spacing

number = int(input())


for i in range(1, number+1):
    space_pattern = " "*(2*(number-i))
    if i == 1:
        print(space_pattern+"*")
    else:
        print(space_pattern+"* "*(i-1)+"*")