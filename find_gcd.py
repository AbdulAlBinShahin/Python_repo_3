def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
 
a=int(input("enter: "))
b=int(input("enter: "))
gcd1=gcd(a,b)
print(f"GCD of {a} & {b} is  {gcd1}")
