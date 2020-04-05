import sqlite3 

class Player:

  dbpath = "data.db"

  def __init__(self, **kwargs):
    self.pk = kwargs.get("pk")
    self.name = kwargs.get("name")
    self.team_id = kwargs.get("team_id")
  
  def insert(self):
    with sqlite3.connect(self.dbpath) as conn:
      cur = conn.cursor()
      sql = """INSERT INTO players(
            name, team_id
      ) VALUES (?, ?);"""
      values = (self.name, self.team_id)
      cur.execute(sql, values)
      # Inserts new players into database (requires team ID (pk))
  
  @classmethod
  def view_players(cls, team_id):
    with sqlite3.connect(cls.dbpath) as conn:
      cur = conn.cursor()
      sql = """SELECT name FROM players WHERE team_id = ?;"""
      cur.execute(sql, (team_id,))
      names = cur.fetchall()
      return names
      # View list of players from given team (requires team ID (pk))

  @classmethod
  def remove_player(cls, name):
    with sqlite3.connect(cls.dbpath) as conn:
      cur = conn.cursor()
      sql = """DELETE FROM players WHERE name=?;"""
      cur.execute(sql, (name,))
      # Removes player from database. 

# if __name__ == "__main__":
#   dan = Player(name="Dan", team_id=1)
#   dan.insert()
#   chris = Player(name="Chris", team_id=1)
#   chris.insert()
#   jim = Player(name="Jim", team_id=1)
#   jim.insert()
#   rick = Player(name="Ricky", team_id=1)
#   rick.insert()
#   don = Player(name="Don", team_id=2)
#   don.insert()
#   justin = Player(name="Justin", team_id=2)
#   justin.insert()
#   amanda = Player(name="Amanda", team_id=2)
#   amanda.insert()
#   chops = Player(name="Chops", team_id=2)
#   chops.insert()

  