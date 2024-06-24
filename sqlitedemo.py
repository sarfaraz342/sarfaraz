import sqlite3
con = sqlite3.connect("mydatabase.db")
cur = con.cursor()
#cur.execute(
     #"CREATE TABLE IF NOT EXISTS student ("
    # "name CHAR(20), "
   #  "email CHAR(30), "
  #   "password CHAR(10)"
 #    ")"
#)
cur.execute("INSERT INTO student (name, email, password) VALUES (?, ?, ?)", ("harish", "harish@gmail.com", "12345"))
cur.execute("INSERT INTO student (name, email, password) VALUES (?, ?, ?)", ("masthan", "masthan@gmail.com", "23456"))
cur.execute("INSERT INTO student (name, email, password) VALUES (?, ?, ?)", ("vishnu", "vishnu@gmail.com", "34567"))
cur.execute('delete from student where name ="harish"  ')
cur.execute('update student set name  ="harish" where password="23456"')
cur.execute("SELECT * FROM STUDENT")
tables = cur.fetchall()
print(tables)