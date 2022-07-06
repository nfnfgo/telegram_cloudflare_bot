import sqlite3
from r_path import r_path

# connect local db and set a cursor
db=sqlite3.connect(r_path+'/data/bot_data.sqlite')
cs=db.cursor() # cs means cursor here

# create database


db.close()