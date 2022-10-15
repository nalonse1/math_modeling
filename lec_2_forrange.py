a = "good"
for i in range(0,10,1):
    if i < len (a):
        print(a[i] + "- bad ")
    else:
        print(f"{i}" + " - good")
        