# import cx_Oracle
import mysql.connector


def create_oracle_conn():
    connection = mysql.connector.connect(host='localhost', database='web_data', user='root', password='root')

    # connection = cx_Oracle.connect(
    #     user="demopython",
    #     password="XXXXX",
    #     dsn="localhost/xepdb1")
    print("Successfully connected to Mysql Database")

    return connection
