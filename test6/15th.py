from functools import reduce
l1=["vikas","Kumar","From","Invertis"]
largest_str=reduce(lambda x,y:x if len(str(x))>len(str(y)) else y,l1)
print(largest_str)