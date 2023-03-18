import sqlite3
import csv

'''
This is a test to learn the syntax for creating local databases. I am using 
TABLE_VENDOR.csv and TABLE_ITEM.csv as samples. I have already completed 
creating tables and inserting data into these tables, as well as activating
a foreign key. However, that was in four different files, I want to create 
both tables and insert the data in one file. 

The main issue I believe I will encounter is importing both .csv files 
into one python file. However, this may not be an issue since python reads 
line for line going down. 

So to solve this issue, I believe I will have to import, read, create, and 
insert data for one table first, and then repeat the process for the second
table. This is how I imagine it. 
    read table_vendor.csv 
        ...
        ...
        ...
    read table_item.csv
        ...
        ...
        ...

Another issue I thought of is having it all under main(). I am worried 
something will snag since it is under one function. Hopefully this 
doesn't present a large problem. 
'''

def main(db_name):
    db_conn = sqlite3.connect(db_name)
    db_cursor = db_conn.cursor

    sql_statement = '''
    CREATE TABLE VENDOR (
    VendorCode TEXT PRIMARY KEY NOT NULL 
    VendorName TEXT 
    VendorPhone TEXT); 
    '''
    db_cursor.execute(sql_statement)


