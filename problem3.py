#sum of Even number (1 to 100)
Total=0
for num in range(1,101):
    if num % 2==0:
        Total+=num
print("sum of Even numbers from 1 to 100 is :", Total)