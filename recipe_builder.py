import sys
from ingredients import ingredients
from recipes import recipes
recipe_name = input('Recipe name: ')
recipe_ingredients = []
for i in range(len(ingredients)):
  ingredient = ''
  intager = False
  while intager == False:
    try:
      ingredient = input('How many oz or number of {} does this recipe take? return "conversion" for oz conversion: '.format(ingredients[i]))
      if ingredient.lower() == 'conversion':
        print("""1 US tablespoon = 0.5 US oz
1 US teaspoon = 0.166667 US oz
1 US cup = 8.11537 US oz
1 US pint = 16 US oz
1 US quart = 32 US oz
1 US gallon = 128 US oz""")
      else:
        ingredient = float(ingredient)
        recipe_ingredients.append(ingredient)
        intager = True
    except:
      print('Please type a number or "conversion".')
print('Are there any ingredients that have not been asked that are included?')
extra = input('(y/n): ')
if 'y' in extra.lower():
  while True:
    try:
      num_extra = int(input('How many extra ingredients are there?'))
      break
    except:
      print('Please return a whole value number')
else:
  num_extra = 0
extra_ingredients = []
for i in range(num_extra):
  ingredient_name = input("Ingredient Name: ")
  extra_ingredients.append(ingredient_name)
for i in range(len(extra_ingredients)):
  for recipe in range(len(recipes)):
    recipes[recipe].append(0)
for i in range(num_extra):
  ingredient = ''
  intager = False
  while intager == False:
    try:
      ingredient = input('How many oz or number of {} does this recipe take? return "conversion" for oz conversion.: '.format(extra_ingredients[i]))
      if ingredient.lower() == 'conversion':
        print("""1 US tablespoon = 0.5 US oz
1 US teaspoon = 0.166667 US oz
1 US cup = 8.11537 US oz
1 US pint = 16 US oz
1 US quart = 32 US oz
1 US gallon = 128 US oz""")
      else:
        ingredient = float(ingredient)
        recipe_ingredients.append(ingredient)
        intager = True
    except:
      print('Please type a number or "conversion".')
for i in range(len(extra_ingredients)):
  ingredients.append(extra_ingredients[i])
f = open('ingredients.py', 'w')
f.write('ingredients = {}'.format(ingredients))
f.close()
recipe = [recipe_name]
for i in range(len(recipe_ingredients)):
  recipe.append(recipe_ingredients[i])
print('Please write a description of how to make your recipe. Use "exit_builder" to go to end.')
while True:
  current_input = input()
  if current_input.lower() == 'exit_builder':
    recipes.append(recipe)
    f = open('recipes.py', 'w')
    f.write('recipes = {}'.format(recipes))
    f.close()
    sys.exit()
  recipe.append(current_input)
