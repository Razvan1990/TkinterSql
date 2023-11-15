import os.path
import sqlite3
import constants


class CheckThings:

    def check_if_table_exists(self, table_name):
        # connecting to database
        database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
        connection = sqlite3.connect(database)
        my_cursor = connection.cursor()
        # sql statement to check
        my_cursor.execute(
            """SELECT count(*) from sqlite_master  WHERE type ="table" AND name =?"""
            ,(table_name,))
        # check the results
        if my_cursor.fetchone()[0] == 1:
            result = True
        else:
            result = False
        my_cursor.close()
        connection.close()
        return result

    def check_for_id(self, table_name, id):
        database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
        connection = sqlite3.connect(database)
        my_cursor = connection.cursor()
        my_cursor.execute("SELECT count(oid) from " + table_name + " WHERE oid = " + id)
        if my_cursor.fetchone()[0] == 1:
            result = True
        else:
            result = False
        my_cursor.close()
        connection.close()
        return result

    def get_original_list(self, table_name, id):
        database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
        connection = sqlite3.connect(database)
        my_cursor = connection.cursor()
        my_cursor.execute("SELECT * from " + table_name + " WHERE oid = " + id)
        result = my_cursor.fetchall()
        my_cursor.close()
        connection.close()
        return result

    def create_table(self, table_name):
        database = os.path.join(constants.DATABASE_FOLDER, constants.DATABASE)
        connection = sqlite3.connect(database)
        my_cursor = connection.cursor()
        # sql query to create table
        my_cursor.execute(
            "CREATE TABLE " + table_name + " (first_name text, second_name text, club text, nationality text, age integer);")
        connection.commit()
        connection.close()



