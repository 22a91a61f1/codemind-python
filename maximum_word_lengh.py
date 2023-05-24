s=input()
l=s.split()
c=0
for i in l:
    if len(i)>c:
        c=len(i)
print(c)