x=input("Enter a String:").lower()
vowel=['a','e','o','u','i']
result=0
for i in x:
    if i in vowel:
        result+=1
print(result)