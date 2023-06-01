import mysql.connector 

dataBase = mysql.connector.connect(
    host = 'localhost', 
    user = 'root', 
    passwd = 'Top0987!' 
)

# preaper a cursor object 
cursorObject = dataBase.cursor() 

# create a database 
cursorObject.execute("CREATE DATABASE westerroyco") 

print("All done!!") 

