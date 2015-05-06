num1=raw_input()
num2=raw_input()
if(num1>num2):
    gcd=num2
    while((num1%num2)!=0):
        gcd=num1/num2
        num1=num2
        num2=gcd
print num2
