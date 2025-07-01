class Book:
    def __init__(self,name,price):
        self.name=name
        self.price=price

    def __str__(self):
        return f"{self.name}: {self.price}"
    
    def __add__(self,other):
        return Book(f"{self.name} + {other.name}",self.price + other.price)

    def __sub__(self,other):
        return Book(f"{self.name} - {other.name}",self.price - other.price)
    
    def __mul__(self, other):
        return Book(f"{self.name} * {other.name}", self.price * other.price)
    
    def __truediv__(self,other):
        return Book(f"{self.name} / {other.name}",self.price / other.price)
    
    def __floordiv__(self,other):
        return Book(f"{self.name} // {other.name}",self.price // other.price)
    
    def __mod__(self,other):
        return Book(f"{self.name} %  {other.name}",self.price % other.price)
    
    #def __pow__(self,other):
       # return Book(f"{self.name} ** {other.name}",self.price ** other.price)
    
    def __et__(self,other):
        return Book(f"{self.name} == {other.name}",self.price == other.price)
    
    def __ne__(self,other):
        return Book(f"{self.name} != {other.name}",self.price != other.price)
    
    def __lt__(self,other):
        return Book(f"{self.name} < {other.name}",self.price < other.price)
    
    def __gt__(self,other):
        return Book(f"{self.name} > {other.name}",self.price > other.price)
    
    def __le__(self, other):
        return Book(f"{self.name} <= {other.name}", self.price <= other.price)
 
    def __ge__(self, other):
        return Book(f"{self.name} >= {other.name}", self.price >= other.price)
 
   
 
 
 
 
 
 
B1=Book("Core Python",200)
B2=Book("Advance Python",400)   


print( B1 + B2)
print(B1 - B2)
print(B1 * B2)
print(B1 / B2)       
print(B1 // B2)      
print(B1 % B2)       
#print(B1 ** B2) 
print(B1 == B2)
print(B1 != B2)
print(B1 < B2)
print(B1 > B2)
print(B1 <= B2)
print(B1>=B2)