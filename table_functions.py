from tables import Table
import json
import datetime

pool_tables = []

def add_tables():

  tables_to_add = int(input("How many tables to add? "))
  
  counter = tables_to_add

  while counter > 0:
    pool_table = Table(counter, "unoccupied")
    pool_tables.append(pool_table.__dict__)
    counter = counter - 1
  

def list_tables():
  for i in range(0, len(pool_tables)):
    table_number = pool_tables[i]["table_id"]
    table_status = pool_tables[i]["status"]
    print(f"{i} {table_number} {table_status}")


def check_out_table():
  table_to_check_out = int(input("Table to check out: "))

  x = datetime.datetime.now()
  minutes = x.strftime("%H:%M:%S")

  if pool_tables[table_to_check_out - 1]["status"] == "occupied":
    print("This table is already checked out.")

  else:  
    table_number = pool_tables[table_to_check_out]["table_id"]
    table_status = pool_tables[table_to_check_out]["status"]

    pool_tables[table_to_check_out - 1]["status"] = "occupied"
    pool_tables[table_to_check_out - 1]["timeout"] = x
    print(f"{table_number} | {table_status} | {minutes}")


def check_in_table():
  list_tables()
  table_to_check_in = int(input("Table to check in: "))

  x = datetime.now()

  if pool_tables[table_to_check_in - 1].status == "unoccupied":
    print("This table is already checked in.")

  else:  
    table_number = pool_tables[table_to_check_out]["table_id"]
    table_status = pool_tables[table_to_check_out]["status"]

    pool_tables[table_to_check_in - 1]["status"] = "unoccupied"
    pool_tables[table_to_check_in - 1]["timein"] = x
    print(f"{table_number} | {table_status} | {x}")