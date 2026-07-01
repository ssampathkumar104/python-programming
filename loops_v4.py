number = int(input())
square = number**2


start_number = 1
for i in range(1, number+1):
    series = ""
    while start_number <= (i*number):
        series = series + str(start_number)+" "
        start_number = start_number + 1 
    print(series)

m = int(input())
n = int(input())

number_start = m*n
for i in range(m):
    series = ""
    for j in range(n):
        series = series + str(number_start) + " "
        number_start = number_start-1
    print(series)

n = int(input())

count = 0
for a in range(1, n):
    for b in range(2, n+1):
        if a+b == n  and a<b:
            count = count+1
            
print(count)

n = int(input())

count = 0

for a in range(1, n-1):
    for b in range(2, n):
        for c in range(3, n+1):
            if a+b+c ==n and a<b<c:
                count = count+1
print(count)

s = int(input())
n = int(input())


for i in range(1, n+1):
    series = ""
    for j in range(2*i):
        series = series + str(s)+" "
        s = s+1
    print(series)


n = int(input())

for i in range(1, n+1):
    series = ""
    for j in range(1,i+1):
        series = series + str(j)+" "
    for k in range(1, i):
        series = series+str(k)+" "
    print(series)

n = int(input())

sum = 0

for i in range(n, 0, -1):
    sum = sum + i 

iterable = 0
for j in range(n):
    spaces = "  "*iterable
    series = spaces
    for k in range(n-iterable):
        series = series + str(sum)+" "
        sum = sum -1
    iterable = iterable + 1 
    print(series)
    
s = int(input())
n = int(input())

k = 0
for i in range(n, 0, -1):
    k = k + i

new_number = k + s -1

for j in range(1, n+1):
    series = ""
    for _ in range(j):
        series = series + str(new_number) + " "
        new_number = new_number - 1 
    print(series)
        

n = int(input())
count = 0
for a in range(1, n-1):
    for b in range(2, n):
        for c  in range(3, n+1):
            if a**2+b**2 == c**2 and a<b<c:
                count = count + 1 
print(count)
                

s = int(input())
n = int(input())

k = s
for i in range(n, 1, -1):
    k = k + i 
    
for j in range(n, 0, -1):
    series = ""
    for _ in range(j):
        series = series + str(k) + " "
        k = k - 1
    print(series)

n = int(input())

for i in range(n, 0, -1):
    series = " "*(n-i)
    for j in range(1, i+1):
        series = series + str(j) + " "
    print(series)

n = int(input())

for i in range(1, n+1):
    series = " "*(n-i)
    for j in range(1, i+1):
        series = series + str(j)+" "
    print(series)
for i in range(n-1, 0, -1):
    series = " "*(n-i)
    for j in range(1, i+1):
        series = series + str(j)+" "
    print(series)

n = int(input())

count = 0
for i in range(1, n+1):
    if i%2!=0 and i%3!=0 and i%4!=0 and i%5!=0 and i%6!=0 and i%7!=0 and i%8!=0 and i%9!=0 and i%10!=0:
        count = count + 1 
print(count)


m = int(input())
n = int(input())

for i in range(m, n+1):
    count = 0
    for j in range(1, n+1):
        if i%j==0:
            count = count + 1
    if count >= 3:
        print(i)

m = int(input())
n = int(input())

series = ""
for i in range(m, n+1):
    arm_sum = 0
    for j in range(0, len(str(i))):
        arm_sum = arm_sum + int(str(i)[j])**len(str(i))
    if arm_sum == i:
        series = series + str(i) + " "
if len(series)!=0:
    print(series)
else:
    print("-1")

n = int(input())
k = int(input())

sum = 0
for a in range(k, 0, -1):
    sum = sum + a
    
m = sum+n-1

for i in range(1, k+1):
    series = ""
    for j in range(1, i+1):
        series = series + str(m)+" "
        m = m-1
    print(series)

n = int(input())

for i in range(1, n+1):
    if i ==1 or i == n:
        series = ""
        for j in range(1, n+1):
            series = series + str(j) + " "
        print(series)
    else:
        # series = ""
        print(str(1)+"  "*(n-2)+" "+str(n))
        # print(series)

n = int(input())

for i in range(1, n+1):
    series = " "*(n-i)
    for j in range(1, i+1):
        series = series + str(j) + " "
    print(series)


n = int(input())

for i in range(1, n+1):
    if i == 1 or i==n:
        series = ""
        for j in range(1, i+1):
            series = series + str(j) + " "
        print(series)
    else:
        series = ""
        for k in range(2, i+1):
            spaces = " "*(2*(k-1)-1)
            series = str(1)+spaces+str(k)
        print(series)
        
            
n = int(input())

for i in range(1, n+1):
    if i == 1 or i == n:
        series = " "*(n-i)
        for j in range(1, i+1):
            series = series + str(j) + " "
        print(series)
    else:
        front_space = " "*(n-i)
        mid_space = " "*((2*(i-1))-1)
        print(front_space+str(1)+mid_space+str(i))
        

n = int(input())

for i in range(n, 0, -1):
    if i == 1 or i == n:
        series = ""
        for j in range(1, i+1):
            series = series + str(j) + " "
        print(series)
    else:
        print(str(1)+" "*((2*(i-1))-1)+str(i))

n = int(input())

starting_number = 5


for i in range(n):
    leading_spaces = " "*(n-i-1)
    
    #First row
    if i ==0:
        print(leading_spaces+str(starting_number))
    #Last row
    elif i == n-1:
        series = ""
        for j in range(n):
            series = series + str(starting_number+j)+" "
        print(series)
    else:
        middle_spaces = " "*(2*i-1)
        print(leading_spaces+str(starting_number)+middle_spaces+str(starting_number+i))

        
n = int(input())

for i in range(1, n+1):
    leading_spaces = "  "*(n-i)
    if i ==1:
        print(leading_spaces+str(i))
    elif i == n:
        series = ""
        for j in range(i, 0, -1):
            series = series + str(j) + " "
        print(series)
    else:
        print(leading_spaces+str(i)+" "*(2*(i-1)-1)+str(1))

m = int(input())
n = int(input())

for i in range(1, m+1):
    if i == 1 or i== m :
        series = ""
        for j in range(7, 7+n):
            series = series + str(j) + " "
        print(series)
    else:
        print(str(7)+" "*(2*(n-1)-1)+str(7+n-1))


n = int(input())
s = int(input())

for i in range(n):
    leading_spaces = " "* i 
    count = n - i
    
    if i ==0:
        series = ""
        for j in range(count):
            series = series + str(s+j)+" "
        print(series)
    
    elif i == n-1:
        print(leading_spaces+str(s))
    else:
        middle_spaces = " "*(2*count-3)
        print(leading_spaces+str(s)+middle_spaces+str(s+count-1))

m = int(input())
n = int(input())


starting_number = 1
for i in range(1, m+1):
    if i == 1 or i == m:
        series = ""
        for j in range(n):
            series = series + str(starting_number)+ " "
            starting_number = starting_number + 1
        print(series)
    else:
        print(str(starting_number)+" "*(2*(n-2)+1)+str(i*n))
        starting_number = (i*n)+1
           
n = int(input())

for i in range(1, n+1):
    number = int(input())
    new_number = 0
    for j in range(0, len(str(number))):
        new_number = new_number+ int(str(number)[j])**len(str(number))
    if new_number == number:
        print(number)
        

m = int(input())
n = int(input())

k = m*n 


for i in range(1, m+1):
    if i == 1 or i == m:
        series = ""
        for j in range(1, n+1):
            series = series + str(k) + " "
            k = k -1
        print(series)
    else:
        series = ""
        print(str(k)+ " "*((2*(n-2))+1)+str(k-(n-1)))
        k = k-(n-1)-1

s = int(input())
n = int(input())

k = s+(n*n)-1

for i in range(1, n+1):
    if i == 1 or i == n:
        series = ""
        for j in range(1, n+1):
            series = series + str(s) + " "
            s = s+1 
        print(series)
    else:
        print(str(s)+" "*(2*(n-2)+1)+str(s+(n-1)))
        s = s+n 

s = int(input())
n = int(input())

for i in range(1, n+1):
    if i == 1 or i == n:
        series = ""
        for j in range(1, i+1):
            series = series + str(s)+ " "
            s = s+1
        print(series)
    else:
        print(str(s)+" "*(2*(i-1)-1)+str(s+1))
        s = s+2 

n = int(input())

starting_number = 1 

for i in range(1, n+1):
    if i == 1:
        series = ""
        for j in range(1, n+1):
            series = series + str(starting_number) + " "
            starting_number = starting_number + 1 
        print(series)
    elif i == n:
        print(starting_number)
    else:
        print(str(starting_number)+" "*(2*(n-i)-1)+str(starting_number+(n-i))+" "*(i-1))
        starting_number = starting_number + (n-i+1)

s = int(input())
n = int(input())

for i in range(1, n+1):
    if i==1:
        series = ""
        for j in range(1, n+1):
            series = series + str(s) + " "
            s = s+1
        print(series)
    elif i==n:
        leading_spaces = " "*(2*(i-1))
        print(leading_spaces+str(s))
    else:
        leading_spaces = " "*(2*(i-1))
        middle_space = " "*(2*(n-i)-1)
        print(leading_spaces+str(s)+middle_space+str(s+1))
        s = s+2

s = int(input())
n = int(input())

for i in range(n):
    series = ""
    
    first_number =  s + (n-i)*(n-i+1)//2-1
    for j in range(n):
        if i ==0:
            series = series + str(first_number-j)+" "
        elif j ==i:
            series = series + str(first_number)+" "
        elif j == n-1:
            last_number = s + ((n-i-1)*(n-i))//2
            series = series + str(last_number)
        else:
            series = series + "  "
    print(series)


s = int(input())
n = int(input())

for i in range(1, n+1):
    if i == 1:
        series = ""
        for j in range(1, n+1):
            series = series + str(s)+ " "
            s = s+1 
        print(series)
    elif i ==n:
        print(" "*((i-1))+str(s))
        # print(" "*(2*(i-1)-1)+str(s))
    else:
        series = ""
        # leading_spaces = " "*(2*(i-1)-1)
        leading_spaces = " "*(i-1)
        middle_spaces = " "*(2*(n-i)-1)
        print(leading_spaces+str(s)+middle_spaces+str(s+(n-i)))
        s = s + (n-i)+ 1

n = int(input())

total_rows = 2*n - 1 

for i in range(total_rows):
    series = ""
    
    distance = abs(n-1-i)
    
    left_position = distance 
    right_position = total_rows -1 - distance
    
    for j in range(total_rows):
        if j == left_position:
            series = series + "1"
        elif j == right_position and left_position != right_position:
            series = series + str(n-distance)
        else:
            series = series + " "
    print(series)


n = int(input())

total = 0

for i in range(n):
    number = int(input())
    
    if number>1:
        is_prime = True
        
        for j in range(2, number):
            if number % j == 0:
                is_prime = False 
                break
        if is_prime:
            total = total + number
print(total)