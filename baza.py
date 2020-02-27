import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="user",
    passwd="haslo",
    database="baza"
)

cursor = mydb.cursor()

cursor.execute("select * from t_sklep")

result = cursor.fetchall()

for x in result:
    print(x)


cursor.close()
mydb.close

#print(mydb)
