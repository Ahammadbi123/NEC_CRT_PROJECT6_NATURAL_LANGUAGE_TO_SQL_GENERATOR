import sqlite3

def create_database():
    connection = sqlite3.connect("retail_data.db")
    cursor = connection.cursor()

    # 1. Products Table
    cursor.execute('DROP TABLE IF EXISTS Products')
    cursor.execute('''CREATE TABLE Products (id INTEGER PRIMARY KEY, name TEXT, category TEXT, price REAL, stock INTEGER)''')

    # 2. Members Table (దీనివల్లే నీ క్వరీస్ కి రిజల్ట్స్ వస్తాయి)
    cursor.execute('DROP TABLE IF EXISTS Members')
    cursor.execute('''CREATE TABLE Members (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city TEXT, joins_count INTEGER)''')

    # Sample Data for Products
    products = [(1, 'Laptop', 'Electronics', 50000, 10), (2, 'Mouse', 'Electronics', 500, 50)]
    cursor.executemany("INSERT INTO Products VALUES (?,?,?,?,?)", products)

    # Sample Data for Members (20 మందిని యాడ్ చేస్తున్నా)
    members = [(i, f"Member_{i}", 20 + (i % 10), "Hyderabad", i + 5) for i in range(1, 21)]
    cursor.executemany("INSERT INTO Members VALUES (?,?,?,?,?)", members)

    connection.commit()
    connection.close()
    print("Database Updated with Members Table!")

if __name__ == "__main__":
    create_database()