from config import host, user, password, db_name                                                                                                
import mysql.connector
from mysql.connector import Error
def create_connection(host_name, user_name, password, db='flask_solo', autocommit=True):
    connection = None
    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            passwd = password
            )
        print('Connection is successful')
    except Error as e:
        print(f'The error is - {e}')
  
    return connection
  
connection = create_connection(host, user, password)
create_users_table = """
CREATE TABLE IF NOT EXISTS sasuke (
id INT AUTO_INCREMENT, 
name TEXT NOT NULL, 
age INT, 
gender TEXT, 
nationality TEXT, 
PRIMARY KEY (id)
)"""

def create_table(connection, query, flag=False):
	if flag:
		cursor = connection.cursor()
		try:
			cursor.execute(f'USE {db_name}')
			cursor.execute(query)
			#connection.commit() 
			print('Table created successfully')
			#cursor.execute('flush tables')
			print('Tables flushed')
			#connection.close()
		except Error as e:
			print(f'Error - {e}')

			
  
create_table(connection, create_users_table, flag=True)
        
