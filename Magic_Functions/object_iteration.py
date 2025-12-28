class ShoppingList:
    def __init__(self):
        self.items = ["Apple","Banana","Cherry","Milk","Carrot"]

    def __getitem__(self, index):
        return self.items[index]

    def __len__(self):
        return len(self.items)

shoppingList = ShoppingList()

print(shoppingList[0])
print("<---------------------------------------------------------------------------------------->")

print("<---------------------------------------------------------------------------------------->")
for item in shoppingList:
    print(item)
print("<---------------------------------------------------------------------------------------->")
if "Milk" in shoppingList:
    print("Yes")
print("<---------------------------------------------------------------------------------------->")
print(len(shoppingList))