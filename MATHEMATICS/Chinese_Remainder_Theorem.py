length = 3
a = [2,3,5]
n = [5,11,17]

Ntot= n[0] * n[1] * n[2]

N = [ n[1]*n[2] , n[0]*n[2], n[0]*n[1] ]

y = [pow(N[i],n[i]-2,n[i]) for i in range(length)]

mysterious_a = 0
for i in range(length):
        mysterious_a += a[i]*N[i]*y[i]
mysterious_a %= Ntot
print(mysterious_a)
