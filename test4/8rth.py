word="listen"
y=''.join(sorted(word))
l1=["enlist","google","inlets","banana"]
for i in l1:
    x=''.join(sorted(i))
    if x==y:
        print(i,end=" ")
