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

def query_generator(**kwargs):
	for key, value in kwargs.items():
		print(type(key))
		print(value)

query_generator(name='sasuke', age='12', sex='male')