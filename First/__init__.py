

def power(num ,times=2):
    s = 1
    while times > 0:
        times -= 1
        s *= num
    return s


print(63/(1.68*1.68))
sum = 0
for x in range(101):
    sum += x
print(sum)
print(power(5))



