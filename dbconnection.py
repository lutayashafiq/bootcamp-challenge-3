import psycopg2
from pprint import pprint

#TODO: create new user, login user,
#TODO: Create new request, fetch all requests, fetch user requests, fetch a single request

class dbConnection:
    def __init__(self):
        try:
            self.connection = psycopg2.connect("dbname = demo user=postgres password=Bamela@20 host=localhost port =5432")
            self.connection.autocommit = True
            self.cursor = self.connection.cursor()
            pprint("made connection")
        except:
            pprint("can connect to the database")

    def create_new_user(self, user_id, name, email, password, is_admin):
        create_new_user_command = ("INSERT INTO USER_TABLE VALUES ('{}', '{}', '{}', '{}', '{}')" .format(user_id, name, email, password, is_admin))
        self.cursor.execute(create_new_user_command)

    def get_user_name(self, name):        
        pass





   