x=[1,3,4,5,2,7]
y=[3,2,1,4,5,9]
result=[]
for i in x:
    if i in y:
        result.append(i)
print(result)