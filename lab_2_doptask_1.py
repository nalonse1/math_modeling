a = float(input())
b = float(input())
c = float(input())
if b**2-4*a*c>0:
    print((-b+(b**2-4*a*c)**0.5)/2*a,(-b-(b**2-4*a*c)**0.5)/2*a)
elif b**2-4*a*c==0:
    print(-b/2/a)
else:
    print("нет корней")

