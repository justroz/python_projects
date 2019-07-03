
#create list of grocery stores
grocery_stores = []
user_input=input("Press 1 to add store; Press 2 view all stores; Press 3 to add items to list; Press q to quit: ")

class GroceryStore:
  def __init__(self, store, zip_code):
    self.store = store
    self.zip_code = zip_code
    self.items = []

class GroceryItem:
  def_init_(self, title, quantity):
    self.title = item
    self.price = 0
    self.quantity = quantity


while user_input != "q":
  
#adds store to list
  if user_input == "1":
    def add_store():
      store = input("Where would you like to shop? ")
      store_zip = input("What's the store's zip code? ")

      grocery_store = GroceryStore(store, store_zip)
      grocery_stores.append(grocery_store)

    add_store()


  #displays all_stores
  elif user_input == "2":
    def display_store_list():
      for index in range(0, len(grocery_stores)):
        print(f"{index+1}  {grocery_stores[index].store}  {grocery_stores[index].zip_code}")

    display_store_list()


  #add items to store list
  elif user_input == "3":
    def display_store_list():
      for index in range(0, len(grocery_stores)):
        print(f"{index+1}  {grocery_stores[index].store}  {grocery_stores[index].zip_code}")

    def add_grocery_item():
      shopping_list = int(input("Which grocery list? "))
      item = input("Grocery Item: ")
      quantity = int(input("How many? "))
      
      grocery_item = GroceryItem(item, quantity)
      grocery_stores.
    display_store_list()
    add_grocery_item()
  
  #view store's shopping cart


  user_input=input("Press 1 to add store; Press 2 view all stores; Press 3 to add items to list; Press q to quit: ")



