from config import host, user, password, db_name                                                                                                
import mysql.connector
from mysql.connector import Error
class Mydb():
    def __init__(self, host=host, user=user, password=password, db_name=db_name):
        self.host = host
        self.user = user
        self.password = password
        self.db_name = db_name

    def create_connection(self):
        connection = None
        try:
            connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                passwd=self.password,
                db=self.db_name

                )
            print('Connection is successful')
        except Error as e:
            print(f'The error is - {e}')
      
        return connection if connection != None else "Connection is not successful"

    def create_table(self, table_name:str = 'test'):
        connection = self.create_connection()
        cursor = connection.cursor()
        try:
            #cursor.execute(f'USE {self.db_name}')
            cursor.execute(f'CREATE TABLE IF NOT EXISTS ( \
                          {table_name})')
                          #need to implement many variables to create
            connection.commit() 
            print('Table created successfully')
            #cursor.execute('flush tables')
            print('Tables flushed')
            connection.close()
        except Error as e:
            print(f'Error - {e}')
        finally:
            connection.close()

'''
>>> line = 'Kong Panda'
>>> index = line.find('Panda')
>>> output_line = line[:index] + 'Fu ' + line[index:]
>>> output_line
'Kong Fu Panda'

'''


query_test = """
CREATE TABLE IF NOT EXISTS tasks (
    task_id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    start_date DATE,
    due_date DATE,
    status TINYINT NOT NULL,
    priority TINYINT NOT NULL,
    description TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)  """



test_db = Mydb()
test_db.create_connection()
test_db.create_table(query)

