from ShoppingList import ShoppingList, Product

list_1 = ShoppingList("Groceries")
print(list_1)
list_1.show()

print("Adding products")
product_1 = Product("Tomato","2Kg")
product_2 = Product("Milk", "3Lt")
product_3 = Product("Potato", "4 Kg")

list_1.add(product_1)
list_1.add(product_2)
list_1.add(product_3)

print(list_1)
list_1.show()       