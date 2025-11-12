'''Write a program that creates two tables, one for meals and one for ingredients, using these SQL queries:

CREATE TABLE IF NOT EXISTS meals (name TEXT) STRICT
CREATE TABLE IF NOT EXISTS ingredients (name TEXT,
meal_id INTEGER, FOREIGN KEY(meal_id) REFERENCES meals
(rowid)) STRICT
Then, write a program that prompts the user for input. If the user enters 'quit', the program should exit. The user can also enter a new meal name, followed by a colon and a comma-delimited list of ingredients: 'meal:ingredient1,ingredient2'. Save the meal and its ingredients in the meals and ingredients tables.

Finally, the user can enter the name of a meal or ingredient. If the name appears in the meals table, the program should list the meal’s ingredients. If the name appears in the ingredients table, the program should list every meal that uses this ingredient. For example, the output of the program could look like this:

> onigiri:rice,nori,salt,sesame seeds
Meal added: onigiri
> chicken and rice:chicken,rice,cream of chicken soup
Meal added: chicken and rice
> onigiri
Ingredients of onigiri:
  rice
  nori
  salt
  sesame seeds
> chicken
Meals that use chicken:
  chicken and rice
> rice
Meals that use rice:
  onigiri
chicken and rice
> quit'''

import sqlite3
import pprint
import sys
#decompose


#creation
conn = sqlite3.connect('mealplanner.db', isolation_level=None)
def creation():
  
  conn.execute('''
CREATE TABLE IF NOT EXISTS meals (
    meal_id INTEGER PRIMARY KEY AUTOINCREMENT,
    mealname TEXT
);
''')
  conn.execute('''
  
CREATE TABLE IF NOT EXISTS ingredients (
    ingredient_id INTEGER PRIMARY KEY AUTOINCREMENT,
    ingredient TEXT,
    meal_id INTEGER,
    FOREIGN KEY(meal_id) REFERENCES meals(meal_id)
);''')
  conn.commit()


#mealadder
def mealadder(meal,ingredients):
  
  cursor = conn.execute("SELECT meal_id FROM meals ORDER BY meal_id DESC LIMIT 1")
  last_id = cursor.fetchone() 
  
  cursor = conn.execute("INSERT INTO meals (mealname) VALUES (?)", (meal,))
  meal_id = cursor.lastrowid  # this is the ID for the new meal
  conn.execute('BEGIN')
  for i in ingredients:
      conn.execute("INSERT INTO ingredients (ingredient, meal_id) VALUES (?, ?)", (i, meal_id))
    
  conn.commit()


#ingredient searcherx
def searcher(item):
    # Check if it's a meal
  resultmeals = conn.execute("SELECT meal_id FROM meals WHERE mealname = ?", (item,)).fetchall()

  # If meal exists, list ingredients
  if resultmeals:
      meal_id = resultmeals[0][0]
      ingredients = conn.execute("SELECT ingredient FROM ingredients WHERE meal_id = ?", (meal_id,)).fetchall()
      print(f"Ingredients of {item}:")
      for ing in ingredients:
          print(f"  {ing[0]}")

  # Otherwise, check if it's an ingredient
  else:
      meals_with_ing = conn.execute("""
          SELECT meals.mealname
          FROM meals JOIN ingredients ON meals.meal_id = ingredients.meal_id
          WHERE ingredients.ingredient = ?
      """, (item,)).fetchall()
      
      if meals_with_ing:
          print(f"Meals that use {item}:")
          for m in meals_with_ing:
              print(f"  {m[0]}")
      else:
          print(f"No meal or ingredient found for '{item}'")
    
  



while True:
  print("input meal name, colon, then items in it")
  meal = input()
  if meal == 'Quit':
    break
  if ':' in meal:
    #separate into items and meal
    mealnamelength = 0
    for idx in range(1,len(meal)):
      if meal[idx] == ':':
        mealnamelength = idx
    mealname = meal[0:mealnamelength]
    items = [items.strip() for item in items.split(',')]
    mealadder(mealname,items)
    
  
  print("input meal or ingredient")
  item = input()
  searcher(item)
  
  
  
        
        
    
  #
    




#user inputs meal and ingredients which is added to database
#only addds if user inputted a colon
#next they enter meal or item, if meal, output meal name and all items in the meal, if item, print all things its in






