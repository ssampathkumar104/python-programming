m = int(input())
n = int(input())


for uni_code in range(m , n+1):
    print(chr(uni_code))


word  = input()

for char in word:
    print(ord(char))


number = int(input())

word = ""

for _ in range(number):
    char = int(input())
    word = word + str(chr(char))
print(word)


s = input()
n = int(input())

count_of_letters=0

for i in s:
    if ord(i)==n:
        count_of_letters = count_of_letters + 1 
        
print(count_of_letters)


s = input()

for char in s:
    if char.isupper():
        print(ord(char))
        break


s = input()

for char in s:
    print(chr(ord(char)+1))



s = input()
is_valid = False

for char in s:
    if char.isupper() or char.islower() or char.isdigit():
        is_valid = True
    else:
        is_valid = False
        break
print(is_valid)


s = input()

current_word = ""
first_word = ""
first=True

for ch in s + " ":
    if ch!=" ":
        current_word = current_word +ch 
    else:
        if first:
            first_word = current_word
            first = False
        elif current_word.lower()<first_word.lower():
            first_word = current_word
        current_word = ""
print(first_word)
            

s = input()

current_word = ""
first_word = ""
last_word = ""
first = True

for ch in s +" ":
    if ch!=" ":
        current_word = current_word + ch 
    else:
        if first:
            first_word = current_word
            last_word = current_word
            first = False
        else:
            if current_word.lower() < first_word.lower():
                first_word = current_word
            if current_word.lower() > last_word.lower():
                last_word = current_word
                
        current_word = ""
print(first_word, last_word)


s = input()
m = int(input())
n = int(input())

series = ""
for char in s:
    if m<=ord(char)<=n:
        series = series+str(char)+" "
print(series)


s = input()

for char in s:
    if char.isdigit():
        print(ord(char))
        break


s = input()

sent_series = ""
for char in s:
    
    if char!=" ":
        sent_series = sent_series+str(chr(ord(char)+1))
    else:
        sent_series = sent_series + char
print(sent_series)


s = input()

new_sentence = ""
new_word = True

for ch in s:
    if new_word and ch != " ":
        new_sentence = new_sentence + chr(ord(ch)+1)
        new_word = False
    else:
        new_sentence = new_sentence + ch 
    if ch == " ":
        new_word = True
print(new_sentence)


s = input()

least = s[0]
highest = s[0]

for ch in s:
    if ord(ch)<ord(least):
        least = ch 
    
    if ord(ch) > ord(highest):
        highest = ch 
print(least, highest)

