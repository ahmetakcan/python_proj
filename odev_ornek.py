lower = 900
upper = 1000

print("Prime numbers between",lower,"and",upper,"are:")

for x in range(lower,upper + 1):

   if x > 1:
       for y in range(2,x):
           if (x % y) == 0:
               break
       else:
           print(x)