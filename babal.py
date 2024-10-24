arr=[1,2,3,4,5,6]
for n in range(1,len(arr)):
    arr=arr[-1:]+arr[:-1]
    leth=len(arr)
    print(leth)
    print(arr)
    if leth<n:
        arr.pop(0)
    else:
        arr.pop(leth-n)
    print(arr)
x={1,2}
y={3,4}
x.symmetric_difference
