import sqlite3

conn = sqlite3.connect('experiment.db')

create_states_table = '''CREATE TABLE IF NOT EXISTS States
         (ID INT PRIMARY KEY NOT NULL,
         INITIAL_STATE TEXT NOT NULL);'''

create_Astar_table = '''CREATE TABLE IF NOT EXISTS Astar
         (ID INT PRIMARY KEY NOT NULL,
         INITIAL_STATE TEXT NOT NULL);'''

create_IDA_table = '''CREATE TABLE IF NOT EXISTS IDA
         (ID INT PRIMARY KEY NOT NULL,
         INITIAL_STATE TEXT NOT NULL);'''

conn.execute(create_states_table)
conn.execute(create_Astar_table)
conn.execute(create_IDA_table)
