import dbm
db = dbm.open("dbm.db", 'r')
for k, v in db.items():
    print(k, v)
