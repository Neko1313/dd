import sqlite3
con1 = sqlite3.connect("/home/dd/strashoeDelo.db")

cur1 = con1.cursor()

ad = []

for row in cur1.execute("SELECT * FROM `us`"):
    row = list(row)
    if row[2] == None:
        row[2] = "-1"
    row.append(row[1])
    row = tuple(row)
    ad.append(row)

con2 = sqlite3.connect("/home/HelloDjang/db.sqlite3")

cur2 = con2.cursor()

for row in ad:
    con2.execute("INSERT INTO `user_SD_usersd` (`id`,`userid`, `refid`,`souls`,`ref`,`name_user`) VALUES (?,?,?,?,?,?)",row)

for row in cur2.execute("SELECT * FROM `user_SD_usersd`"):
    print(row)
