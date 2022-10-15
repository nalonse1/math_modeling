a = int(input())
b = int(input())
if b == 0:
    print("нельзя на 0")
    exit(0)
if a%b==0:
    print("Yes",a//b)
else:
    print("no",a%b)