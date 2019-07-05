from tables import Table
from table_funct import add_tables, list_tables
import json
import datetime


def table_management():
  user_option = input("Add Tables: Press 1 \nList Tables: Press 2 \nCheck Table Out: Press 3 \nCheck Table In: Press 4 \nQuit System: Press q \n" )

  if user_option == "1":
    add_tables()

  elif user_option == "2":
    list_tables()

  elif user_option == "3":
    check_out_table()

  elif user_option == "4":
    check_in_table()

  elif user_option == "q":
    print("Pool Table Management System has QUIT")

  else:
    print("Press 1,2,3,4, or q")

# user_option = input("Add Tables: Press 1 \nList Tables: Press 2 \nCheck Table Out: Press 3 \nCheck Table In: Press 4 \nQuit System: Press q" )

table_management()