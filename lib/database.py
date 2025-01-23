import sqlite3

CONNECTION = sqlite3.connect('school.db')

CURSOR = CONNECTION.cursor()

CURSOR.execute("PRAGMA foreign_keys = ON;")