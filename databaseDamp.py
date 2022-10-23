import sqlite3

con = sqlite3.connect("drom.sqlite")

f_damp = open('drom.db','r', encoding ='utf-8-sig')
damp = f_damp.read()
f_damp.close()

con.executescript(damp)
con.commit()

con.close()
