import random
def randomfloat(a,b):
    return random.uniform(a,b)
a=float(input("enter: "))
b=float(input("enter: "))
ran_num=randomfloat(a,b)
print(f"Random number is {ran_num}")
