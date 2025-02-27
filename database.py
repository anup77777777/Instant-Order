import sqlite3
#Database
# Connect to the database
database = sqlite3.connect('project.db')
cursor = database.cursor()

# Create owner table 
# cursor.execute("""
#     CREATE TABLE owners_information (
#         owner_name TEXT,
#         owner_number INTEGER,
#         username TEXT,
#         password TEXT
#     )
# """)

#Create Customer table
# cursor.execute("""
#     CREATE TABLE customer_information (
#         full_name TEXT,
#         number INTEGER,
#         username TEXT,
#         password TEXT
#     )
# """)

#Table Login
# cursor.execute("""
#     CREATE TABLE login_information (
#         username TEXT,
#         password TEXT
#     )
# """)


# Commit and close connection
database.commit()
database.close()