# import pypyodbc as podbc
# import pandas as pd

# conn2 = podbc.connect("Driver={SQL Server Native Client 11.0};"
#                        "Server=DESKTOP-TE993MT\MICROSOFTSQLSV;"
#                        "Database=AdventureWorks;"
#                        "Trusted_Connection=yes;"
#                        )
# # running the SQL query
# SQL_Query = pd.read_sql_query('''SELECT * FROM [dbo].[HumanResources.Department]''', conn2)

# SQL_Query.head()
import pyodbc
import pandas as pd

conx = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-TE993MT\MICROSOFTSQLSV; Database=AdventureWorks; Trusted_Connection=yes;')
pyodbc.drivers()
conx_string = "driver={SQL Server}; server=DESKTOP-TE993MT\MICROSOFTSQLSV; database=AdventureWorks; Trusted_Connection=yes;"

query = "SELECT Name, CreditRating FROM Purchasing.Vendor WHERE CreditRating < 3"

conx = pyodbc.connect(conx_string);
cursor = conx.cursor();
cursor.execute(query);
data = cursor.fetchall();

print(data[:5])
df = pd.read_sql_query(query,conx)

print(df)
conx.close()
