def sum_nm(start,n):
    sum=0
    for i in range(start,n+1):
        sum+=i
    return sum
 
start=int(input("enter: "))
num=int(input("enter :"))
 
if(start>=0 and num>=start):
    sum1=sum_nm(start,num)
    print(f"Sum of n natural nu  is {sum1}")
else:
    print("Enter valid num")
