def gcd(a,b):
    while b:
        a,b=b,a%b
    return a
def lcm(a,b):
    return abs(a*b)//gcd(a,b)
 
a=int(input("enter: "))
b=int(input("enter: "))
lcm1=lcm(a,b)
print(f"LCM of {a} & {b} is  {lcm1}")
