import sys
from recipes import recipes
from ingredients import ingredients
for i in range(len(ingredients)):
  while True:
    try:
      amount = input('How many oz or number of {} do you have? return "conversion" for conversion: '.format(ingredients[i]))
      if amount.lower() == 'conversion':
        print("""1 US tablespoon = 0.5 US oz
1 US teaspoon = 0.166667 US oz
1 US cup = 8.11537 US oz
1 US pint = 16 US oz
1 US quart = 32 US oz
1 US gallon = 128 US oz""")
      else:
        amount = float(amount)
        break
    except:
      print('please return a number.')
  for m in range(len(recipes)):
    for l in range(len(recipes)):
      if recipes[l][i + 1] > amount:
        del recipes[l]
        break
for i in range(len(recipes)):
  print(recipes[i][0])
while True:
  found = False
  current_recipe = input('recipe (return "cancel" to cancel): ')
  if current_recipe.lower() == 'cancel':
    sys.exit()
  for i in range(len(recipes)):
    if recipes[i][0].lower() == current_recipe.lower():
      recipe_number = i
      found = True
  if found:
    break
  else:
    print('"{}" is not a recipe'.format(current_recipe))
print('{}: '.format(recipes[recipe_number][0]))
for i in range(len(recipes[recipe_number]) - 1):
  try:
    print('{}: {}'.format(ingredients[i], recipes[recipe_number][i + 1]))
  except:
    print(recipes[recipe_number][i + 1])
