a=[2,3,5,7]
for i in range(2,200):
    if i%2!=0:
        if i%3!=0:
            if i%5!=0:
                if i%7!=0:
                    a.append(i)
print('set of prime numbers : ')
print(*a,sep=', ')