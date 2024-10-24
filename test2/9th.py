x=["Hello","Student","of","invertis","yes!"]
# a=[]
# b=0
# for i in range(len(x)):
#     if len(x[i])>b:
#         b=len(x[i])
#         a.append(i)
# print(x[a[-1]])
lenth_max=x[0]
for i in x:
    if len(i)>len(lenth_max):
        lenth_max=i
print(lenth_max)