text=input("enter text:")
print("char-count:",len(text.replace(" ","")))
print("word-count:",len(text.split()))
print("sentence-count:",text.count("."))
s=""
for char in text :
    if char.isalpha()and "a"<=char<="z" or "A"<=char<="Z":
        s=s+char
print("English-letter-count:",len(s))
max_count=0
max_char=""
for char in text:
    c=text.count(char)
    if c>max_count:
        max_count=c
        max_char=char
print("max-char:{}".format(max_char))
max_count1=0
max_word=""
for char in text.split():
    d=text.count(char)
    if d>max_count1:
        max_count1=d
        max_word=char
print("max-word:{}".format(max_word))
print("reverse-text:",text[::-1])
n=""
for char in text :
    if char.isalpha():
        n=n+char
m=n[::-1]
if n==m:
    print("this is palindrome")
else:
    print("this isnot palindrome")
print("replce bad to good and hate to love:",text.replace("bad","good").replace("hate","love"))
