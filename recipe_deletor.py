from recipes import recipes
for i in range(len(recipes)):
  print(recipes[i][0])
len_recipes = len(recipes)
while True:
  deletor = input('What recipe do you want to delete?: ')
  for m in range(len(recipes)):
    for i in range(len(recipes)):
      if recipes[i][0].lower() == deletor.lower():
        del recipes[i]
        break
  if len_recipes > len(recipes):
    break
  else:
    print('"{}" is not a recipe.'.format(deletor))
f = open('recipes.py', 'w')
f.write('recipes = {}'.format(recipes))
f.close()
