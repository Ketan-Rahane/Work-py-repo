class Book:
    def __init__(self,price):
        
        self.price=price

    def __str__(self):
        return  str(self.price)
    
    def __add__(self,other):
        return Book(self.price + other.price)
    
    def __sub__(self,other):
        return Book(self.price - other.price)
    
    def __mul__(self,other):
        return Book(self.price * other.price)
    
    def __truediv__(self,other):
        return Book(self.price / other.price)
    
    def __floordiv__(self,other):
        return Book(self.price // other.price)
    
    def __mod__(self,other):
        return Book(self.price % other.price)
    
    #def __pow__(self,other):
     #   return Book(self.price ** other.price)
    
    def __eq__(self,other):
        return Book(self.price == other.price)
    
    def __ne__(self,other):
        return Book(self.price != other.price)
    
    def __lt__(self,other):
        return Book(self.price < other.price)
    
    def __gt__(self,other):
        return Book(self.price > other.price)
    
    def __le__(self,other):
        return Book(self.price <= other.price)
    
    def __ge__(self,other):
        return Book(self.price >= other.price)
 
B1=Book(200)
B2=Book(400)   

print("Price:",B1 + B2)
print("Price:",B1 - B2)
print("Price:",B1 * B2)
print("Price:",B1 / B2)       
print("Price:",B1 //B2)      
print("Price:",B1 % B2)       
#print("Price:",B1 **B2) 
print("Price:",B1 ==B2)
print("Price:",B1 !=B2)
print("Price:",B1 < B2)
print("Price:",B1 > B2)
print("Price:",B1 <=B2)
print("Price:",B1>= B2)

#Output:
Price: 600
Price: -200
Price: 80000
Price: 0.5
Price: 0
Price: 200
Price: False
Price: True
Price: True
Price: False
Price: True
Price: False
