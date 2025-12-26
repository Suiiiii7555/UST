class Product:
    def __init__(self,  item_name , quantity ):
        self.item_name = item_name
        self.quantity = quantity

    def __str__(self):
        return f"Product {self.item_name} of quantity is {self.quantity}"
    
    def change_quantity(self, new_quantity):
        self.quantity = new_quantity

class ShoppingList:
    def __init__(self, item_name):
        self.item_name = item_name
        self.items = []

    def __str__(self):
        return f"Shopping list {self.item_name} and number of items are {len(self.items)}"
    
    def add(self , new_item ):
        if isinstance(new_item, Product):
            self.items.append(new_item)
            print(f"{new_item} added to item list")
        else:
            print("New item is not a product")

    def show(self):
        print(f"Number of items in the list are {len(self.items)}")
        for item in self.items:
            print(item.item_name, item.quantity)