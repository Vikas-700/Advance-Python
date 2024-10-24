s="A man,a plan,a canal,Panama"
s=s.replace(",","")
s=s.replace(" ","")
s=s.lower()
x=s[::-1]
if x==s:
    print("Palidrone.")
else:
    print("Not A Palidrone")