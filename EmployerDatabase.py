import mysql.connector

#  create connector with name db


class Manager:
    def __init__(self):
        pass

    @staticmethod
    def add_value(value):
        print(value)
        if all(value):
            addCursor.execute('''INSERT INTO contacts (name, surname, addhar, phone_number, catagory, state) VALUES( %s, %s, %s, %s, %s, %s);''', value)
            db.commit()
        else:
            print('all values are not filled properly')

    @staticmethod
    def delete_value():
        pass

    @staticmethod
    def create_table(table_name):
        addCursor.execute('''
            CREATE TABLE contacts(
            id INT AUTO_INCREMENT PRIMARY KEY, 
            name varchar(10) NOT NULL, 
            surname varchar(20) NOT NULL, 
            addhar char(12) NOT NULL UNIQUE, 
            phone_number char(10) NOT NUll UNIQUE, 
            catagory varchar(50) NOT NULL,
            state varchar(50) NOT NULL 
            ); ''')

    @staticmethod
    def drop_table():
        addCursor.execute('''DROP TABLE contacts''')

    @staticmethod
    def load_data():
        retriveCursor.execute('select name, surname, addhar, phone_number, catagory, state from contacts ;')
        data = retriveCursor.fetchall()
        return data
