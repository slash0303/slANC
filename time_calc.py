lis = []

while True:
    a = float(input())
    if a == 345:        # exit code
        break
    else:
        lis.append(a)

avg = 0

for x in lis:
    avg += x

avg /= len(lis)     # 0.030118869332706227
print(avg)
