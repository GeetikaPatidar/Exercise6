a = int(input("enter number:"))

print(type(a))
if a%3==0:
    print("ais divisible by 3:" + a)
elif a%5==0:
    print("divisible by 5:" +a)
elif a%3==0 and a%5==0:
    print("divisible by both", +a)
else:
    print("not divisible by both")
