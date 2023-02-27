import sqlite3

# create a connection object that represents our database
# the first argument can be the file where we want to store our data
# if the file exists, it just connects. if not, it craetes it and then connects
conn = sqlite3.connect('employee.db')
# employee.db is not something I will understand, ut is gibberish

# Next we craeate a cursor (to be able to run sql commands, using execute method)
c = conn.cursor()

# Here comes the SQL command we wanna run
# three quotes on each side, and ' for strings, make it easy to write command that extend to multiple lines
# c.execute("""CREATE TABLE employees(
#             first text,
#             last text,
#             pay integer
#             )""")


# this will fit on one line, hence the single quotes:
# c.execute("INSERT INTO employees VALUES ('Majid', 'Benam', 50900)")

c.execute("SELECT * FROM employees")
print(c.fetchone())

conn.commit()
conn.close()
