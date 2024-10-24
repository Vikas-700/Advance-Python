num=int(input("Enter Number:"))
prime_is=lambda x:x>1 and all(x%i!=0 for i in range(2,int(x**0.5)+1))
print(f"{num} is prime {prime_is(num)}")