class Table:
  def __init__(self, table_id, status):
    self.table_id = table_id
    self.status = status
    self.timeout = " "
    self.timein = " "
    self.totaltime = 0
    self.price = 0.0