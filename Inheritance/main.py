from shape import Circle

circle_1 = Circle(10,"Blue","3mm","Center")

print("Initial circle created : ")
print(circle_1)

# circle_1.change_border_color("Black")
# circle_1.change_border_thickness("10mm")
# print("New updated circle is : \n",circle_1)
area_of_circle = circle_1.Area()
print(area_of_circle)