import sqlite3
akbar = sqlite3.connect("python410.db")
asghar = akbar.cursor()
sql = """
CREATE TABLE IF NOT EXISTS user (
userId INTEGER ,
name VARCHAR (60),
family VARCHAR (60),
email VARCHAR (60)
);
"""

sql = """
CREATE TABLE IF NOT EXISTS product (
productId INTEGER ,
name VARCHAR (60),
price INTEGER
);
"""

asghar.execute(sql)
akbar.commit()
akbar.close()
