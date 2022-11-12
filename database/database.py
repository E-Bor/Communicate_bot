import sqlite3
import os
import platform

class UserData:

    def __init__(self):
        self.path_to_database = os.path.abspath(os.path.dirname(__file__)) + "\\UserData.db" if platform.system() \
            == "Windows" else os.path.abspath(os.path.dirname(__file__)) + "//UserData.db"
        self.create_database()

    def create_database(self):
        try:
            sqlite_connection = sqlite3.connect(self.path_to_database)
            cursor = sqlite_connection.cursor()
            sqlite_create = """CREATE TABLE Userdata (
                                userid    INTEGER UNIQUE,
                                tgnick    TEXT,
                                userphone INTEGER,
                                username  TEXT,
                                userban   BOOLEAN DEFAULT (FALSE) 
                                );
                                """
            cursor.execute(sqlite_create)
            sqlite_connection.commit()
            cursor.close()
        except sqlite3.Error as error:
            print("Error in DB", error)
        finally:
            if (sqlite_connection):
                sqlite_connection.close()

    def create_connection(self):
        try:
            sqlite_connection = sqlite3.connect(str(self.path_to_database))
            cursor = sqlite_connection.cursor()
            return cursor, sqlite_connection
        except sqlite3.Error as error:
            print("Error in DB", error)

    # stop connection with database
    def stop_connection(self, sqlite_connection):
        if sqlite_connection:
            sqlite_connection.close()

    # read data from database
    def read_data(self, category):
        cur, con = self.create_connection()
        sql_request = "select * from Userdata where userid=:category"
        data = cur.execute(sql_request, {"category": category}).fetchall()
        self.stop_connection(con)
        return data

    def get_all_id(self):
        cur, con = self.create_connection()
        sql_request = "select userid from Userdata "
        data = cur.execute(sql_request).fetchall()
        self.stop_connection(con)
        return data

    # add position to database
    def add_position(self, *args):
        cur, con = self.create_connection()
        sql_request = "insert or ignore into Userdata values (?,?,?,?,?)"
        cur.execute(sql_request, args)
        con.commit()
        self.stop_connection(con)

    # edit position in database
    def edit_position(self, category, item, value):
        cur, con = self.create_connection()
        if len(self.read_data(category)) == 0:
            print(f"Not correct category '{category}' ")
        else:
            try:
                sql_request = f"update Userdata set {item} = ? where userid= ?"
                cur.execute(sql_request, (value, category,))
                con.commit()
            except sqlite3.OperationalError:
                print(f" no such collumn with name {item}")
        self.stop_connection(con)

    # delete position in database
    def delete_position(self, category):
        cur, con = self.create_connection()
        sql_request = "DELETE FROM Userdata where category like ?"
        cur.execute(sql_request, ("{}%".format(category),))
        con.commit()

    def check_ban(self, category):
        cur, con = self.create_connection()
        sql_request = "select userban from Userdata where category=:category"
        data = cur.execute(sql_request, {"category": category}).fetchall()
        self.stop_connection(con)
        return data

    def check_user(self, user_id):
        a = self.read_data(user_id)
        print(a)
        if not a:
            return 0
        if a[0][-1] == "TRUE":
            return "Ban"
        else:
            return 1

    def get_info_about_user(self, userid):
        if "@" not in userid:
            info = self.read_data(userid)
            return info[0]
        else:
            userid = userid.replace("@", "")
            cur, con = self.create_connection()
            sql_request = "select * from Userdata where tgnick=:category"
            data = cur.execute(sql_request, {"category": userid}).fetchall()
            self.stop_connection(con)
            return data[0]

