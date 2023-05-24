s=input()
l=s.split()
c=len(s)
for i in l:
    if len(i)<c:
        c=len(i)
print(c)