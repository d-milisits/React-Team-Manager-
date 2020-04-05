import sqlite3 

class Coach:

  dbpath = "data.db"

  def __init__(self, **kwargs):
    self.pk = kwargs.get("pk")
    self.name = kwargs.get("name")
  
  def insert(self):
    with sqlite3.connect(self.dbpath) as conn:
      cur = conn.cursor()
      sql = """INSERT INTO coaches(
            name
      ) VALUES (?);"""
      cur.execute(sql, (self.name,))
      # Inserts new Coach into database.

# if __name__ == "__main__":
#   Kris = Coach(name="Kris")
#   Kris.insert()
#   Christ = Coach(name="Christ")
#   Christ.insert()