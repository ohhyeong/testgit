import sys
sys.path.append('C:\\Users\\ohs87\\AppData\\Local\\Packages\\PythonSoftwareFoundation.Python.3.13_qbz5n2kfra8p0\\LocalCache\\local-packages\\Python313\\site-packages')
#print(sys.path)

import duckdb
#con=duckdb.connect(database=':memory:')
con=duckdb.connect(database='testddb.ddb')

#duckdb.sql("DESCRIBE SELECT * FROM 'yellow_tripdata_2024-01.parquet'").show() # Describe the schema of the Parquet file
duckdb.sql("SELECT * FROM 'yellow_tripdata_2024-01.parquet' LIMIT 3").show()