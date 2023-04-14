'''
Operators:

a+b

a, b: operand
+ : operator

1. Arithmetic Operator: +  - * / % // **
2. Logical Operator: and or not
3. Relational Operator: < > <= >= == !=
4. Assignment Operator:  = += -= *= /= %= ....
5. Bitwise Operator: & | ^ ~ << >>
6. Membership Operator: in , not in
7. Identity Operator: is , is not



and

A   B   A and B

F   F   F
F   T   F
T   F   F
T   T   T



Or

A   B   A or B

F   F   F
F   T   T
T   F   T
T   T   T


not

A   not A

T   F
F   T

'''

# 1. Arithmetic Operator: +  - * / % // **

# a=int(input('Enter a no:'))
# b=int(input('Enter a no:'))


# print("sum: ",a+b)
# print("mul: ",a*b)
# print("sub: ",a-b)
# print("div: ",a/b)
# print("mod: ",a%b)
# print("floor division: ",a//b)
# print("Exponant: ",a**b)

# print(3**4)


# 2. Relational Operator

a=45
b=2
c=67

print(a<b)
print(b>c)
print(b<=c)
print(a==c)


# 3. Logical Operator

print(a>b and b<c)
print(b<c or c>a)
print(not b<c)

# 4. Assignment Operator:  = += -= *= /= %= ....

x=5
# x=x+3
x+=3
print(x)

y=6
y*=2
print(y)


# 5. Bitwise Operator: & | ^ ~ << >>

'''
binary: 0 1 (2)
decimal : 0 to 9 (10)

0101 -> 0*2^3 + 1*2^2 + 0*2^1 + 1*2^0  = 0+4+0+1 = 5
1110 -> 1*8 + 1*4 +1* 2 + 0 = 8+4+2 = 14

11101 -> 16+8+4+0+1 = 29

        256      128   64    32    16       8    4    2    1

10101 - 21


decimal to binary:

12 - 1100
34 - 10 0010
56 - 111000
84 - 101 0100
157- 
569- 
896-


13 - 1101
5 -  0101

---------------
&    0101 (5)
|    1101(13)

13: 0000 1101
<<1: 0001 1010 (26)
<<2: 0011 0100 (52)
<<3: 0110 1000 (104)

>>1: 0000 0110(6)
>>2: 0000 0011(3)
>>3: 0000 0001(1)
>>4: 0000 0000 (0)


'''

print(13 & 5)
print(13| 5)
print(13<<1)
print(13<<2)
print(13<<3)

print(13>>1)
print(13>>2)
print(13>>3)
print(13>>40)