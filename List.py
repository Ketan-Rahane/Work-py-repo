my_list=[10,20,30,40,50]
print("my_list:",my_list)

my_list.pop()
print("list after poped():",my_list)

my_list.remove(20)
print("list after remove(30):",my_list)

print(my_list[25]) 


#Output:
my_list: [10, 20, 30, 40, 50]
list after poped(): [10, 20, 30, 40]
list after remove(20): [10, 30, 40]
Traceback (most recent call last):
  File "d:\Python\List.py", line 10, in <module>
    print(my_list[25])
          ~~~~~~~^^^^
IndexError: list index out of range.
