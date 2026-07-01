# Exercise 1: Check if a number is divisible by 7
number = int(input())

remainer = number % 7

if remainer==0:
    print("Divisible by Seven")
else:
    print("Not Divisible by Seven")


# Exercise 2: Check if number is special for eleven (remainder 0 or 1)
number = int(input())

remainder = number % 11

if remainder==0 or remainder==1:
    print("Special Eleven")
else:
    print("Normal Number")


# Exercise 3: Compare remainders when dividing by 4 and 5, print the larger
number = int(input())

remainer1 = number%4
remainer2 = number%5

if remainer1>=remainer2:
    print(remainer1)
else:
    print(remainer2)

# Exercise 4: Calculate and print quotient and remainder of two numbers
a = int(input())
b = int(input())
quotient = int(a/b)
remainder = a%b

print(quotient)
print(remainder)

# Exercise 5: Check if both numbers divisible by 3 and at least one divisible by 12
a = int(input())
b = int(input())

if ((a%3)==0 and (b%3)==0) and ((a%12)==0 or (b%12)==0):
    print("Pair")
else:
    print("Not a Pair")

# Exercise 6: Duplicate of Exercise 5
a = int(input())
b = int(input())

if ((a%3)==0 and (b%3)==0) and ((a%12)==0 or (b%12)==0):
    print("Pair")
else:
    print("Not a Pair")

# Exercise 7: Check if string starts with 'NXT' and remaining digits divisible by 2 or 7
word = input()


if word[0:3]=="NXT" and ( int(word[3:])%2==0 or int(word[3:])%7==0 ):
    print("Special String")
else:
    print("Not a Special String")

# Exercise 8: Check if number divisible by both its digits, multiply by 2 if yes
number = int(input())

if number%int(str(number)[0])==0 and number%int(str(number)[1])==0:
    print(number*2)
else:
    print(number)

# Exercise 9: Calculate power of two numbers
number = int(input())
exponent = int(input())

print(number**exponent)
      
# Exercise 10: Calculate square root of a number
number = int(input())

print(number**0.5)

# Exercise 11: Duplicate - calculate square root of a number
number = int(input())

print(number**0.5)

# Exercise 12: Compare a^b and b^a, print the larger value
a = int(input())
b = int(input())

if a**b>b**a:
    print(a**b)
else:
    print(b**a)

# Exercise 13: Duplicate - compare a^b and b^a
a = int(input())
b = int(input())

if a**b>b**a:
    print(a**b)
else:
    print(b**a)

# Exercise 14: Duplicate - compare a^b and b^a
a = int(input())
b = int(input())
a = int(input())
b = int(input())

if a**b>b**a:
    print(a**b)
else:
    print(b**a)
# Exercise 15: Check if sum of squares of two numbers >= 60
number1 = int(input())
number2 = int(input())

if number1**2+number2**2>=60:
    print("Greater than or Equal to 60")
else:
    print("Less than 60")

# Exercise 16: Check if last digit equals last digit of its square
number = int(input())

last_digit_number = int(str(number)[len(str(number))-1])
square_last_digit_number = int(str(number**2)[len(str(number**2))-1])

if last_digit_number==square_last_digit_number:
    print("Equal")
else:
    print("Not Equal")

# Exercise 17: Check if number is an Armstrong number (sum of cubes of digits)
number = int(input())
sum = int(str(number)[0])**3+int(str(number)[1])**3+int(str(number)[2])**3

if number==sum:
    print("True")
else:
    print("False")

# Exercise 18: Multiply by 3 if divisible by 3, else multiply by 2
number = int(input())

if number%3==0:
    print(number*3)
else:
    print(number*2)

# Exercise 19: Print the smaller remainder between two numbers
number1 = int(input())
number2 = int(input())

if number1%number2 <= number2%number1:
    print(number1%number2)
else:
    print(number2%number1)

# Exercise 20: Check if number not divisible by 2, 3, 5, or 7
number = int(input())


if number%2!=0 and number%3!=0 and number%5!=0 and number%7!=0:
    print("True")
else:
    print("False")

# Exercise 21: Print number if divisible by both 5 and 7 or less than 7, else print remainders
number = int(input())

if (number%5==0 and number%7==0) or number<7:
    print(number)
else:
    print(number%5)
    print(number%7)

# Exercise 22: Calculate hypotenuse (distance) using Pythagorean theorem
a = int(input())
b = int(input())

print(int((a**2+b**2)**0.5))

# Exercise 23: Check if square root of A equals B
a = int(input())
b = int(input())

if int(a**0.5)==b:
    print("Square root of A is equal to B")
else:
    print("Square root of A is not equal to B")

# Exercise 24: Check if 4-digit number is an Armstrong number
number = int(input())

armstrong = int(str(number)[0])**4+int(str(number)[1])**4+int(str(number)[2])**4+int(str(number)[3])**4

if armstrong==number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")

# Exercise 25: Convert days into years, weeks, and remaining days
number = int(input())

print(number//365)
print((number%365)//7)
print(int(((number%365)%7)))

# Exercise 26: Check divisibility by 10 or 5
number = int(input())

is_divisible_by_10 = number%10==0
is_divisible_by_5 = number%5==0

if is_divisible_by_10:
    print("Divisible by 10")
else:
    if is_divisible_by_5:
        print("Divisible by 5")
    else:
        print("Not Divisible by 10 or 5")

# Exercise 27: Identify polygon by number of sides
number = int(input())

if number<3:
    print("Not Polygon")
elif number==3:
    print("Triangle")
elif number==4:
    print("Quadrilateral")
elif number==5:
    print("Pentagon")
else:
    print("Big Polygon")


# Exercise 28: Find the greatest among three numbers
a = int(input())
b = int(input())
c = int(input())

is_a_greatest = (a>b) and (b>c)
is_b_greatest = (b>c) and (b>a)

if is_a_greatest:
    print(a)
elif is_b_greatest:
    print(b)
else:
    print(c)

# Exercise 29: Assign grade based on marks
marks = float(input())

if marks>85:
    print("A")
elif 85>=marks>70:
    print("B")
elif 70>=marks>=60:
    print("C")
else:
    print("F")

# Exercise 30: Categorize rank as top 3 or top 10
rank = int(input())

if rank<=3:
    print("One of Top 3")
elif 3<rank<=10:
    print("Not Top 3 but One of Top 10")

# Exercise 31: Check exam eligibility by hall ticket or ID
h = input()
i = input()

if h=="Y":
    print("Allowed to Exam - Has Hall ticket")
elif i=="Y":
    print("Allowed to Exam - Has Identification Card")

# Exercise 32: Print greeting based on time of day
time = int(input())

if 12>time>=4:
    print("Good Morning")
elif 16>time>=12:
    print("Good Afternoon")
elif 20>time>=16:
    print("Good Evening")
elif time>=20 or time<4:
    print("Good Night")

# Exercise 33: Check if number is greater than 30 and/or 50 (nested)
number = int(input())

if number>30:
    print("X is Greater than 30")
    if number>50:
        print("X is Greater than 50")

# Exercise 34: Calculate electricity bill with tiered pricing and 20% tax
units = int(input())

bill = 0.0

if units<=50:
    bill = (units*2)
elif units<=150:
    bill = (50*2)+((units-50)*3)
elif units<=250:
    bill = (50*2)+(100*3)+((units-150)*5)
elif units>250:
    bill = (50*2)+(100*3)+(100*5)+((units-250)*8)

total_bill = bill+(bill*0.2)
print(total_bill)

# Exercise 35: Check if number is positive or negative
number = float(input())

if number>=0:
    print("Positive")
else:
    print("Negative")

# Exercise 36: Determine profit or loss based on cost price and selling price
cp = float(input())
sp = float(input())

if sp>cp:
    print("Profit")
elif cp==sp:
    print("No Profit - No Loss")
else:
    print("Loss")

# Exercise 37: Determine season based on month number
number = int(input())

if number==1 or number==11 or number==12:
    print("Winter")
elif number==2 or number==3:
    print("Spring")
elif number==4 or number==5 or number==6:
    print("Summer")
elif number==7 or number==8:
    print("Rainy")
else:
    print("Autumn")

# Exercise 38: Find the smallest among three numbers
a = int(input())
b = int(input())
c = int(input())

is_a_smallest = a<b and a<c
is_b_smallest = b<a and b<c 
is_c_smallest = c<a and c<b

if is_a_smallest:
    print(a)
elif is_b_smallest:
    print(b)
elif is_c_smallest:
    print(c)
else:
    print(a)
    
# Exercise 39: Classify weather based on temperature
T = float(input())

if T<0:
    print("Freezing weather")
elif 0<=T<10:
    print("Very Cold weather")
elif 10<=T<20:
    print("Cold weather")
elif 20<=T<30:
    print("Normal")
elif 30<=T<40:
    print("Hot")
if T>=40:
    print("Very Hot")

# Exercise 40: Compare two numbers and print relationship
A = int(input())
B = int(input())

if A>B:
    print("A > B")
elif A<B:
    print("A < B")
else:
    print("A == B")

# Exercise 41: Simple calculator for basic operations
O = input()
A = int(input())
B = int(input())

if O=="/":
    print(A/B)
elif O=="%":
    print(A%B)
elif O=="*":
    print(A*B)
elif O=="-":
    print(A-B)
elif O=="+":
    print(A+B)


# Exercise 42: Parse expression with suffix (T=10x, H=100x, K=1000x)
expr = input()

if expr[len(expr)-1]=="T":
    print(int(expr[:len(expr)-1])*10)
elif expr[len(expr)-1]=="H":
    print(int(expr[:len(expr)-1])*100)
elif expr[len(expr)-1]=="K":
    print(int(expr[:len(expr)-1])*1000)

# Exercise 43: Calculate score based on distance with tiered multipliers
D = int(input())

score = 0.0

if D<=40:
    score = D*2
elif D<=60:
    score = 40*2+((D-40)*4)
elif D<=120:
    score = 40*2+20*4+((D-60)*6)
elif D>120:
    score = 40*2+20*4+60*6+((D-120)*8)
total_score = score+50
print(total_score)

# Exercise 44: Check exam eligibility by attendance percentage or teacher approval
A = input()
M = input()

if (int(A[:len(A)-1]))>=75 or M=="Y":
    print("Allowed to write exam")
else:
    print("Cannot write exam")

# Exercise 45: Calculate sum of digits of a 4-digit number
n = int(input())

sum = 0

if n>=0:
    sum = sum+(n%10)
    n = n // 10
if n>0:
    sum = sum+(n%10)
    n = n // 10
if n>0:
    sum = sum+(n%10)
    n = n // 10
if n>0:
     sum = sum+(n%10)

print(sum)
    
# Exercise 46: Assign number to group 1-6 based on modulo 6 pattern
n = int(input())

if n==1 or (n-1)%6==0:
    print("Group 1")
elif n==2 or (n-2)%6==0:
    print("Group 2")
elif n==3 or (n-3)%6==0:
    print("Group 3")
elif n==4 or (n-4)%6==0:
    print("Group 4")
elif n==5 or (n-5)%6==0:
    print("Group 5")
elif n==6 or (n-6)%6==0:
    print("Group 6")

# Exercise 47: Break down amount into 500, 50, 10, and 1 notes
number = int(input())

count_500 = int(number/500) 
amount = number-(500*count_500)
count_50 = int(amount/50) 
amount = amount-(50*count_50)
count_10 = int(amount/10) 
amount = amount-(10*count_10)
count_1 = int(amount/1)
print(f"500: {count_500} 50: {count_50} 10: {count_10} 1: {count_1}")

# Exercise 48: Break down amount into 5 and 1 notes
number = int(input())


count_5 = number//5 
count_1 = number-(5*count_5)

print("5:"+str(count_5))
print("1:"+str(count_1))

# Exercise 49: Break down amount into 100, 50, 10, and 1 notes
number = int(input())

count_100 = number//100 
amount = number-(100*count_100)
count_50 = amount//50 
amount = amount-(50*count_50)
count_10 = amount//10 
amount = amount-(10*count_10)
count_1 = amount
print("100:"+str(count_100))
print("50:"+str(count_50))
print("10:"+str(count_10))
print("1:"+str(count_1))

# Exercise 50: Categorize day of week as start, midweek, or weekend
week_number = int(input())


if week_number==1 or week_number==2:
    print("Week Start")
elif week_number==3 or week_number==4 or week_number==5:
    print("Midweek")
elif week_number==6 or week_number==7:
    print("Weekend")


# Exercise 51: Calculate score based on distance with tiered rates and bonus
dist = int(input())

bonus = 100
basic_score=0

if dist<=50:
    basic_score = dist*3
elif 50<dist<=100:
    basic_score = (50*3)+((dist-50)*5)
elif 100<dist<=200:
    basic_score = (50*3)+(50*5)+((dist-100)*6)
elif dist>200:
    basic_score = (50*3)+(50*5)+(100*6)+((dist-200)*10)
print(basic_score+bonus)

# Exercise 52: Break down amount into 100, 50, 20, and 10 notes
amount = int(input())

count_100 = amount//100 
amount = amount-(100*count_100)
count_50 = amount//50 
amount = amount-(50*count_50)
count_20 = amount//20 
amount = amount-(20*count_20)
count_10 = amount//10 

print("100 Notes: "+str(count_100))
print("50 Notes: "+str(count_50))
print("20 Notes: "+str(count_20))
print("10 Notes: "+str(count_10))

# Exercise 53: Break down amount into all Indian currency denominations (2000, 500, 200, 50, 20, 5, 2, 1)
amount = int(input())

count_2000 = amount//2000 
amount = amount - (2000*count_2000)
count_500 = amount//500 
amount = amount - (500*count_500)
count_200 = amount//200 
amount = amount - (200*count_200)
count_50 = amount//50 
amount = amount - (50*count_50)
count_20 = amount//20 
amount = amount - (20*count_20)
count_5 = amount//5 
amount = amount - (5*count_5)
count_2 = amount//2 
amount = amount - (2*count_2)
count_1 = amount//1 

print(f"2000:{count_2000} 500:{count_500} 200:{count_200} 50:{count_50} 20:{count_20} 5:{count_5} 2:{count_2} 1:{count_1}")

# Exercise 54: Find day of week based on starting day and date offset
day = input()
date = int(input())

count = (date-1)%7

if day == "Monday":
     if count==0:
         print("Monday")
     if count==1:
         print("Tuesday")
     if count==2:
         print("Wednesday")
     if count==3:
         print("Thursday")
     if count==4:
         print("Friday")
     if count==5:
         print("Saturday")
     if count==6:
         print("Sunday")
if day == "Tuesday":
     if count==6:
         print("Monday")
     if count==0:
         print("Tuesday")
     if count==1:
         print("Wednesday")
     if count==2:
         print("Thursday")
     if count==3:
         print("Friday")
     if count==4:
         print("Saturday")
     if count==5:
         print("Sunday")
if day == "Wednesday":
     if count==5:
         print("Monday")
     if count==6:
         print("Tuesday")
     if count==0:
         print("Wednesday")
     if count==1:
         print("Thursday")
     if count==2:
         print("Friday")
     if count==3:
         print("Saturday")
     if count==4:
         print("Sunday")
if day == "Thursday":
     if count==4:
         print("Monday")
     if count==5:
         print("Tuesday")
     if count==6:
         print("Wednesday")
     if count==0:
         print("Thursday")
     if count==1:
         print("Friday")
     if count==2:
         print("Saturday")
     if count==3:
         print("Sunday")
if day == "Friday":
     if count==3:
         print("Monday")
     if count==4:
         print("Tuesday")
     if count==5:
         print("Wednesday")
     if count==6:
         print("Thursday")
     if count==0:
         print("Friday")
     if count==1:
         print("Saturday")
     if count==2:
         print("Sunday")
if day == "Saturday":
     if count==2:
         print("Monday")
     if count==3:
         print("Tuesday")
     if count==4:
         print("Wednesday")
     if count==5:
         print("Thursday")
     if count==6:
         print("Friday")
     if count==0:
         print("Saturday")
     if count==1:
         print("Sunday")
if day == "Sunday":
     if count==1:
         print("Monday")
     if count==2:
         print("Tuesday")
     if count==3:
         print("Wednesday")
     if count==4:
         print("Thursday")
     if count==5:
         print("Friday")
     if count==6:
         print("Saturday")
     if count==0:
         print("Sunday")

# Exercise 55: Calculate number of handshakes for n people
n = int(input())

if n>=0:
    handshakes = (n*(n-1))//2
    print(handshakes)

# Exercise 56: Repeat a word n times
word = input()+" "
number = int(input())

print(word*number)

# Exercise 57: Print the last digit of a number
number = int(input())

print(str(number)[len(str(number))-1])

# Exercise 58: Convert days to years, weeks, and remaining days
number = int(input())

count_y = number//365
number = number-(count_y*365)
count_w = number//7
number = number-(count_w*7)
count_d = number

print(f"{count_y} years {count_w} weeks {count_d} days")

# Exercise 59: Calculate absolute difference between two numbers
number1 = int(input())
number2 = int(input())

print(abs(number1-number2))

# Exercise 60: Rock-Paper-Scissors game between Abhinav and Anjali
abhinav_shape = input()
anjali_shape = input()

if abhinav_shape==anjali_shape:
    print("Tie")
if abhinav_shape=="Rock" and anjali_shape=="Scissors":
    print("Abhinav Wins")
if abhinav_shape=="Scissors" and anjali_shape=="Rock":
    print("Anjali Wins")
if abhinav_shape=="Paper" and anjali_shape=="Rock":
    print("Abhinav Wins")
if abhinav_shape=="Rock" and anjali_shape=="Paper":
    print("Anjali Wins")
if abhinav_shape=="Scissors" and anjali_shape=="Paper":
    print("Abhinav Wins")
if abhinav_shape=="Paper" and anjali_shape=="Scissors":
    print("Anjali Wins")
    
# Exercise 61: Map month number to month name (1-12)
number = int(input())

if number==1:
    print("January")
elif number==2:
    print("February")
elif number==3:
    print("March")
elif number==4:
    print("April")
elif number==5:
    print("May")
elif number==6:
    print("June")
elif number==7:
    print("July")
elif number==8:
    print("August")
elif number==9:
    print("September")
elif number==10:
    print("October")
elif number==11:
    print("November")
elif number==12:
    print("December")
else:
    print("Invalid Month Number")

# Exercise 62: Classify triangle as Equilateral, Isosceles, or Scalene
side_a = int(input())
side_b = int(input())
side_c = int(input())

if side_a==side_b==side_c:
    print("Equilateral")
elif (side_a==side_b or side_a==side_c or side_b==side_c) and (side_b!=side_c or side_a!=side_c):
    print("Isosceles")
else:
    print("Scalene")

# Exercise 63: Break down amount into Indian notes (1000, 500, 100, 50, 20, 5, 1)
amount = int(input())

count_1000 = amount//1000 
amount = amount - (count_1000*1000)
count_500 = amount//500 
amount = amount - (count_500*500)
count_100 = amount//100 
amount = amount -(count_100*100)
count_50 = amount//50 
amount = amount-(count_50*50)
count_20 = amount//20 
amount = amount-(count_20*20)
count_5 = amount//5 
amount = amount-(count_5*5)
count_1 = amount

print(f"1000:{count_1000}")
print(f"500:{count_500}")
print(f"100:{count_100}")
print(f"50:{count_50}")
print(f"20:{count_20}")
print(f"5:{count_5}")
print(f"1:{count_1}")

