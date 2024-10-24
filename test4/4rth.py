l=[[1,2],[3,4,5],[6,7,8]]
# output [1,2,3,4,5,6,7,8]
result=[]
for i in l:
    for j in i:
        result.append(j)
print(result)
