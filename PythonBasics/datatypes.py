# dynamic binding of variables to objects of different data types, unlike static binding in some other languages ex: C#
a = 10          # 'a' is bound to an integer object
b = 3.14        # 'b' is bound to a float object
c = "Hello"     # 'c' is bound to a string object
d = [1, 2, 3]   # 'd' is bound to

a= d
d="anish"
print(f"a={a}, type={type(a)}")  # Output: a=[1, 2, 3], type=<class 'list'>
print(f"b={b}, type={type(b)}") 


a,b,c,d = 20, 6.28, "World", [4, 5, 6]  # Assigning multiple variables in a single line
print(f"a={a}, b= {b}, c= {c}, d={d}")  # Output: a=20