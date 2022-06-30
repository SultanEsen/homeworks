import sqlite3

def create_connection(db_file):
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except sqlite3.Error as e:
        print(e)
    return conn


def create_table(conn, create_table_sql):
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except sqlite3.Error as e:
        print(e)

def insert_product(conn, products):
    sql = '''
    INSERT INTO products (product_title, price, quantity)
    VALUES (?, ?, ?)
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_quant_of_product(conn, products):
    sql = '''
    UPDATE products SET quantity = ?
    where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def update_price_of_product(conn, products):
    sql = '''
    UPDATE products SET price = ?
    where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, products)
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def delete_product(conn, products_id):
    sql = '''
    DELETE FROM products where id = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (products_id,))
        conn.commit()
    except sqlite3.Error as e:
        print(e)

def select_all_products(conn):
    sql = '''
    SELECT * from products
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql)
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)

def select_products_by_price_and_quant(conn, price_lim, q_lim):
    sql = '''
    SELECT * from products where price < ? and quantity > ?
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (price_lim, q_lim))
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)

def select_products_by_name(conn, name):
    sql = f'''
    SELECT product_title, price from products where product_title LIKE ?
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql, (name))
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)

def select_distrs_of_products(conn):
    sql = f'''
    select products.product_title, distrs.distr_name from products 
    LEFT JOIN distrs on products.distr_id = distrs.id;
        '''
    try:
        cursor = conn.cursor()
        cursor.execute(sql,)
        rows = cursor.fetchall()

        for r in rows:
            print(r)

    except sqlite3.Error as e:
        print(e)

db_name = r'hw8_db'
create_products_table_sql = '''
CREATE TABLE products (
id INTEGER PRIMARY KEY AUTOINCREMENT,
product_title VARCHAR(200) NOT NULL,
price DOUBLE(10, 2) NOT NULL DEFAULT 0.0,
quantity INTEGER(5) NOT NULL DEFAULT 0
)'''


connection = create_connection(db_name)
if connection is not None:
    print('Successfully connected to DB ' + db_name)
    # create_table(connection, create_products_table_sql)

    # insert_product(connection, ('Изюм', 800.0, 10))
    # insert_product(connection, ('Мясо', 600.0, 50))
    # insert_product(connection, ('Картофель', 50.0, 30))
    # insert_product(connection, ('Томат', 70.0, 40))
    # insert_product(connection, ('Огурец', 40.0, 10))
    # insert_product(connection, ('Тыква', 25.0, 78))
    # insert_product(connection, ('Абрикос', 60.0, 12))
    # insert_product(connection, ('Яблоко', 100.0, 14))
    # insert_product(connection, ('Миндаль', 1000.0, 3))
    # insert_product(connection, ('Инжир', 1000.0, 2))
    # insert_product(connection, ('Мука', 50.0, 60))
    # insert_product(connection, ('Сахар', 100.0, 9))
    # insert_product(connection, ('Клубника', 150.0, 2))
    # insert_product(connection, ('Черешня', 250.0, 4))
    # insert_product(connection, ('Арбуз', 40.0, 22))
    # insert_product(connection, ('Шампунь детский', 200.0, 5))
    # insert_product(connection, ('Щампунь дягтерный', 150.0, 2))
    # insert_product(connection, ('Шампунь против перхоти', 300.0, 7))
    # insert_product(connection, ('Мыло детское', 40.0, 10))
    # insert_product(connection, ('Мыло дягтерное', 35.0, 3))

    # update_quant_of_product(connection, (12, 1))

    # update_price_of_product(connection, (650, 2))

    # delete_product(connection, 15)

    # select_all_products(connection)

    # select_products_by_price_and_quant(connection, 100, 5)

    # select_products_by_name(connection, ("%Мыло%",))
    select_distrs_of_products(connection)

    connection.close()
    print('Done')