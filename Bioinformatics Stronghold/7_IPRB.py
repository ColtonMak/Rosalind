# Mendel's First Law

# homo dom
k = int(input())
# hetero
m = int(input())
# homo rec
n = int(input())
t = k + m + n

kk = (k/t)*((k-1)/(t-1))*1
km = (k/t)*(m/(t-1))*1
kn = (k/t)*(n/(t-1))*1

mk = (m/t)*(k/(t-1))*1
mm = (m/t)*((m-1)/(t-1))*(3/4)
mn = (m/t)*(n/(t-1))*(2/4)

nk = (n/t)*(k/(t-1))*1
nm = (n/t)*(m/(t-1))*(2/4)
nn = (n/t)*((n-1)/(t-1))*0

print (kk+km+kn+mk+mm+mn+nk+nm+nn)