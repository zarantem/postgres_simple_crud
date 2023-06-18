import psycopg2

connection = psycopg2.connect(database='test_db', user='root', host='localhost', port='5433', password='postgres')
cur = connection.cursor()
cur.execute(
    """CREATE TABLE users(
    id serial,
    name varchar(50) NOT NULL,
    age integer NOT NULL);""")
cur.execute("INSERT INTO users(id, name, age) VALUES ('1', 'John', '25');")
print("DONE")
cur.execute("INSERT INTO users(id, name, age) VALUES ('2', 'Jane', '30');")
print("DONE")
cur.execute("INSERT INTO users(id, name, age) VALUES ('3', 'Alex', '17');")
print("DONE")
cur.execute("SELECT name FROM users WHERE name LIKE '%a%' OR name LIKE 'A%';")
print(cur.fetchall())

