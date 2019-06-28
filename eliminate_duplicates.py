names = ["Alex", "John", "Mary", "Steve", "John", "Steve"]
no_duplicates = []

# get value from name

# get value from no_duplicates

# compare names value to values in no_duplicates

# append no_duplicates with name

def delete_duplicates():
  for i in names:
    dups_contains_i = False
    for f in no_duplicates:
      if i == f:
        dups_contains_i = True
    if not dups_contains_i:
      no_duplicates.append(i)
  print(no_duplicates)

delete_duplicates()
