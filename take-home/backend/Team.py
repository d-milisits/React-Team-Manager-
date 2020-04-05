import sqlite3 

class Team:

  dbpath = "data.db"

  def __init__(self, **kwargs):
    self.pk = kwargs.get("pk")
    self.name = kwargs.get("name")
    self.coach_id = kwargs.get("coach_id")
  
  def insert(self):
    with sqlite3.connect(self.dbpath) as conn:
      cur = conn.cursor()
      sql = """INSERT INTO teams(
            name, coach_id
      ) VALUES (?, ?);"""
      values = (self.name, self.coach_id)
      cur.execute(sql, values)
      # Inserts new Team into database. Assumes there is a coach object already created for team.
  
  @classmethod
  def view_teams(cls):
    with sqlite3.connect(cls.dbpath) as conn:
      cur = conn.cursor()
      sql = """SELECT name FROM teams;"""
      cur.execute(sql)
      teams = cur.fetchall()
      return teams
      # View list of all teams existing in database. 
  
  @classmethod
  def pk_by_name(cls, name):
    with sqlite3.connect(cls.dbpath) as conn:
      cur = conn.cursor()
      sql = """SELECT pk FROM teams WHERE name=?;"""
      cur.execute(sql, (name,))
      team = cur.fetchone()
      return team
      # Retrieves team ID (pk) by name-- used in other SQL methods (in Player).

# if __name__ == "__main__":
#   titans = Team(name="Titans", coach_id=1)
#   titans.insert()
#   ducks = Team(name="Ducks", coach_id=2)
#   ducks.insert()