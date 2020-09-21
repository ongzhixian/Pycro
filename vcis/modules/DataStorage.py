################################################################################
# Modules and functions import statements
################################################################################

from sqlite3 import connect
from os import path

################################################################################
# Classes
################################################################################

class DataStore:
    """Base class for all data stores"""
    def __init__(self):
        self.data = []
        pass


class SqliteDataStore(DataStore):
    """Data store class for Sqlite3 databases"""
    
    def __init__(self, connection_string):
        self.connection_string = connection_string
        if not path.exists(self.connection_string):
            self.initialize_db()
            

    def initialize_db(self):
        self.connection = connect(self.connection_string)
        with connect(self.connection_string) as conn:
            c = conn.cursor()
            c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
            conn.commit()

    

    def exec(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()

        # Create table
        c.execute('''CREATE TABLE stocks
                    (date text, trans text, symbol text, qty real, price real)''')

        # Insert a row of data
        c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

        # Save (commit) the changes
        conn.commit()

        # We can also close the connection if we are done with it.
        # Just be sure any changes have been committed or they will be lost.
        conn.close()

    def query(self):
        conn = sqlite3.connect('example.db')
        c = conn.cursor()



class MongoDbDataStore(DataStore):
    """Data store class for MongoDB databases"""
    def __init__(self):
        pass

class MySqlDataStore(DataStore):
    """Data store class for MySql databases"""
    def __init__(self):
        pass

class SqlServerDataStore(DataStore):
    """Data store class for SqlServer databases"""
    def __init__(self):
        pass

class Db2DataStore(DataStore):
    """Data store class for DB2 databases"""
    def __init__(self):
        pass

class OracleDataStore(DataStore):
    """Data store class for Oracle databases"""
    def __init__(self):
        pass

        