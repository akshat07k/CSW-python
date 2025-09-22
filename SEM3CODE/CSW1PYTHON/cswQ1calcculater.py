a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
op = input("Enter operator (+, -, *, /,%,ceiling,**,//): ")
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0 :
        print("error")
    else :
        return a/b
def percentage(a,b):
    return (b/a)*100
def integer_division(a,b):
    return a//b
def power(a,b):
    return a**b
def ceiling(result):
    if result == int(result):
        return result
    else:
        return int(result)+1
def binary(c):
      d=""
      while c>0:
          d=str(c%2)+d
          c=c//2
      return d
def hexadecimal(c):
    hex_digit="0123456789ABCDEF"
    hex_result=""
    while c>0:
        hex_result=hex_digit[c%16]+hex_result
        c=c//16
    return hex_result
if op=="+":
    r=add(a,b)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
        print(c)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
if op=="-":
    r=subtract(a,b)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
        print(c)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
         print(hexadecimal(c))
if op=="*":
    r=multiply(a,b)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
if op=="/":
    r=divide(a,b)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
if op=="//":
    r=integer_division(a,b)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
if op=="**":
    r=power(a,b)
    print(r)
    user=input("Do you want to convert it to ceiling value(y/n): ")
    if user=="y":
        c=ceiling(r)
    user2=input("Do you want to convert it to binary or hexadecimal(bin/hex): ")
    if user2=="bin":
        print(binary(c))
    if user2=="hex":
        print(hexadecimal(c))
