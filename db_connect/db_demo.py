from utilities.configuration import get_connection
import mysql.connector as my_sql

'''conn = my_sql.connect(
    host= 'localhost',
    user= 'root',
    password = 'root',
    database= 'APIDevelop'
)

#print(conn.is_connected())'''
conn = get_connection()
print(conn)
cur = conn.cursor()
cur.execute('Select Sum(Amount) from CustomerInfo')

row = cur.fetchall()
print(f'Sum of Amounts is {float(row[0][0])}')
