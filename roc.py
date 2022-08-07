i = 1
d = 0
#generates a list of numbers.
while i < 1000:
    i = i + 1
    a = 0
    x = 0
    #generates a list of numbers less than i. 
    while x < i:
        x=x+1
        #this will check for divisors. 
        if (i/x)-int(i/x) == 0:
            a=a+1
    if a==2:
        #if it finds a prime number it will add it.
        d=d+i
print(d) 