__author__ = 'Deepak'
n,k=map(int,raw_input().split())
a=map(int,raw_input().split())
m=1
d=[]
while(m<=len(a)):
    for j in range(len(a)-m+1):
        d.append(sum(list(a[j:j+m])))
    m+=1
#print d
d.sort(reverse=True)
for i in range(k):
    print d[i],
