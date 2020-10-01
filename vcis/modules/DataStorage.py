################################################################################
# Modules and functions import statements
################################################################################

import logging
from sqlite3 import connect
from os import path

################################################################################
# Classes
################################################################################

class DataModel:
    """Base class for all data models"""
    def __init__(self):
        #self.data = []
        pass

class UserModel(DataModel):
    def __init__(self, data):
        self.id                 = data[0]
        self.username           = data[1]
        self.password_hash      = data[2]
        self.password_salt      = data[3]
        self.email              = data[4]
        self.email_confirmed    = data[5]
        self.cre_dt             = data[6]
        self.upd_dt             = data[7]
        
    def is_valid_credential(self, password):
        from Crypto.Random import get_random_bytes
        from binascii import hexlify as hex, unhexlify as unhex
        from Crypto.Hash import SHA256

        h = SHA256.new()
        h.update(password.encode('utf8'))
        compute_hash = self.password_salt + h.hexdigest()

        logging.debug("compute_hash is [{0}]".format(compute_hash))

        return self.password_hash == compute_hash

class DataStore:
    """Base class for all data stores"""
    def __init__(self, data_store_type):
        self.data = []
        if data_store_type.lower() == "sqlite":
            # TODO: Make this configurable
            self.data_store = SqliteDataStore("./data/cred_store.sqlite3")

    def get_user(self, username):
        record = self.data_store.get_user(username)
        if record is None:
            logging.info("Username (%s) not found.", username)
        else:
            logging.info("Username (%s) found. %s", username, record)
        return record

    def add_user(self, username, password_hash, password_salt, email):
        self.data_store.add_user(username, password_hash, password_salt, email)
        



class SqliteDataStore(DataStore):
    """Data store class for Sqlite3 databases"""

    def tableScripts(self):
        self.table_scripts = {}
        self.table_scripts["user"] = """
        CREATE TABLE IF NOT EXISTS "user" (
            "id"	INTEGER,
            "username"	TEXT NOT NULL UNIQUE,
            "password_hash"	TEXT NOT NULL,
            "password_salt"	TEXT NOT NULL,
            "email"	TEXT NOT NULL,
            "email_confirmed"	INTEGER DEFAULT 0,
            "cre_dt"	TEXT DEFAULT CURRENT_TIMESTAMP,
            "upd_dt"	TEXT DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY("id")
        );
        """
    
    def __init__(self, connection_string):
        self.tableScripts()
        self.connection_string = connection_string
        if not path.exists(self.connection_string):
            self.initialize_db()
            
    def initialize_db(self):
        self.connection = connect(self.connection_string)
        with connect(self.connection_string) as conn:
            c = conn.cursor()
            #c.execute('''CREATE TABLE stocks (date text, trans text, symbol text, qty real, price real)''')
            logging.info("run table_scripts user")
            c.execute(self.table_scripts["user"])
            conn.commit()

    def execute(self, sql, *args):
        logging.info("SQL %s %s", sql, args)
        #logging.info(args)
        with connect(self.connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, args)
            
            #     conn = sqlite3.connect('example.db')
            #     c = conn.cursor()

            #     # Create table
            #     c.execute('''CREATE TABLE stocks
            #                 (date text, trans text, symbol text, qty real, price real)''')

            #     # Insert a row of data
            #     c.execute("INSERT INTO stocks VALUES ('2006-01-05','BUY','RHAT',100,35.14)")

            #     # Save (commit) the changes
            #     conn.commit()

            #     # We can also close the connection if we are done with it.
            #     # Just be sure any changes have been committed or they will be lost.
            #     conn.close()

    def query(self, sql, *args):
        logging.info("SQL %s %s", sql, args)
        #logging.info(args)
        with connect(self.connection_string) as connection:
            cursor = connection.cursor()
            cursor.execute(sql, args)
            return cursor.fetchall()

    ########################################
    # Datastore methods
    ########################################

    def get_user(self, username):
        results = self.query('SELECT * FROM user WHERE username=?', username)
        if len(results) <= 0:
            return None
        return UserModel(results[0])
        
    def add_user(self, username, password_hash, password_salt, email):
        self.execute("INSERT INTO user (username, password_hash, password_salt, email) VALUES (?, ?, ?, ?);", username, password_hash, password_salt, email)
        


            
    


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

        