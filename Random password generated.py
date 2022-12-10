import random
n=int(input("Enter the length of password you want to make:"))
s=""
for i in range(1,n+2):
    a=chr(random.randint(65,90))
    b=chr(random.randint(97,122))
    c=str(int(random.random()*10))
    d=[a,b,c,"#","@","$","&",]
    s+=random.choice(d)
print(s)