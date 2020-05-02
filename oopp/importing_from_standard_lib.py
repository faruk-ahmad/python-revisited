from collections import OrderedDict

favourite_foods = OrderedDict()

favourite_foods['faruk'] = 'Burger'
favourite_foods['ahmad'] = 'Noodles'
favourite_foods['apple'] = 'Apples'
favourite_foods['khan'] = 'Orranges'

for person, food in favourite_foods.items():
    print(f"{person}'s favorite food is: {food}")