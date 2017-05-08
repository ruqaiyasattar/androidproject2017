#example 4.1
pizzas=['Fajita','Chicken Tikka','Chicken Golden Delight']
print("my favorite pizza flavors are: \n".title())
for pizza in pizzas:
    print("i like ".title()+pizza.title()+" flavor of pizza.".title())
print("i like pizza soo much".title()+"\nits' cheesy flavor is yummiest thing".title()+"\ni really love pizza".title())

#example 4.2
animal=['tiger','bear','lion']
print("\nThese are the animals who have common characteristics")
for animals in animal:
    print("A "+animals.title()+" is a brave"+" animal".title())
print("\nall of these are carnivores".title())

#example 4.11
print("copy of pizza's")
friend_pizza=pizzas[:]
print(friend_pizza)
pizzas.append('Extra Cheese')
friend_pizza.append('pineapple pizza')
print(pizzas)
print("\nmy favorite pizzas are:".title())
for fav in pizzas:
    print(fav)

print("\nmy favorite pizzas are:".title())
for myfri_fav in friend_pizza:
    print(myfri_fav)

#example 4.14
food=('green tea','eggs','peanut butter','choclate cake','chicken soap')
print("\n")
for simple_food in food:
    print(simple_food)

##food.append('new data')
##print(food)


food=('green tea','eggs','peanut butter','pineapple cake','pizza')
print("\n")
for modified_food in food:
    print(modified_food)
