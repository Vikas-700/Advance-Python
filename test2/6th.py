x="I am vikas kumar"
new=x.split()
result=''
for i in reversed(new):
    result+=i+" "
print(result)
z=new[::-1]
re=' '.join(z)
print(re)