a = int(input())
if (a%4)<1 and (a%100)>1 or (a%400)<1:
    print("YES")
else:
    print("NO")
