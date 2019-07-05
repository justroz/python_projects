class Table:
  def __init__(self, table_id, status):
    self.table_id = table_id
    self.status = status
    self.timeout = " "
    self.timein = " "
    self.totaltime = 0
    self.price = 0.0

  def check_out_table():
    table_to_check_out = int(input("Table to check out: "))

    x = datetime.datetime.now()

    if pool_tables[table_to_check_out - 1].status == "occupied":
      print("This table is already checked out.")

    else:  
      pool_tables[table_to_check_out - 1].status = "occupied"
      pool_tables[table_to_check_out - 1].timeout = x
      print(f"{pool_tables[table_to_check_out].table_id} | {pool_tables[table_to_check_out - 1].status} {x}")


  def check_in_table():
    table_to_check_out = int(input("Table to check in: "))

    x = datetime.datetime.now()

    if pool_tables[table_to_check_out - 1].status == "unoccupied":
      print("This table is already checked in.")

    else:  
      pool_tables[table_to_check_out - 1].status = "unoccupied"
      pool_tables[table_to_check_out - 1].timein = x
      print(f"{pool_tables[table_to_check_out].table_id} | {pool_tables[table_to_check_out - 1].status} {x}")

