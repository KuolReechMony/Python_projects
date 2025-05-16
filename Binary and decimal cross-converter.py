"""
x = '10010101011101'
y = 0

for i in range(len(x)):
    if x[i] == '1':
        # We are using the difference between the length of the input value and the current iteration and one to find the power to which the value of 2 should be raised to
        y += (2 ** (len(x)-i-1))
"""

















y = 157
x = 1
while y > (2 ** x):
    if y >= x:
        pass
        x += 1

count = x + 1
for i in range(1,count):
    if i == 1:
        pass
