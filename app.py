class Car:
    def __init__(self, name:str, color:str, type:str, price:float)->None:
        self.name = name
        self.color = color
        self.type = type
        self.price = price
        
        print(f"{self.color} {self.type} worth #{self.price} with name {self.name}") 
    
if __name__ == "__main__":
    
    car1 = Car('Benz', 'red', 'convertible', 600000 )
    print(car1)
    car2 = Car('Toyota', 'blue', 'van', 1000000 )
    print(car2)
    
    