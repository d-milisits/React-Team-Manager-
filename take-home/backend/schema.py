import sqlite3 

def schema(dbpath="data.db"):
  with sqlite3.connect(dbpath) as conn:
    cursor = conn.cursor()

    sql = """CREATE TABLE coaches(
          pk INTEGER PRIMARY KEY AUTOINCREMENT,
          name VARCHAR(50)
    );"""
    cursor.execute(sql)

    sql2 = """CREATE TABLE teams(
          pk INTEGER PRIMARY KEY AUTOINCREMENT,
          name VARCHAR(50),
          coach_id INTEGER,
          FOREIGN KEY (coach_id) REFERENCES coach(pk)
    );"""
    cursor.execute(sql2)

    sql3 = """CREATE TABLE players(
          pk INTEGER PRIMARY KEY AUTOINCREMENT,
          name VARCHAR(100),
          team_id INTEGER,
          FOREIGN KEY (team_id) REFERENCES teams(pk)
    );"""
    cursor.execute(sql3)

if __name__ == "__main__":
  schema()



