from functools import reduce
l1=["Raj","Kumar","Verma"]
result=reduce(lambda x,y:x+" "+y,l1)
print(result)