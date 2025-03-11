import pandas as pd
import sqlite3 as sql3


# Create truncated mutations table called "ccle" in ccle_truncated db sqlite3
df = pd.read_csv("ccle_mutations.csv")
truncated_df = df.loc[0:9999, ["Entrez_Gene_Id", "DepMap_ID", "isTCGAhotspot"]] # get 10000 rows of data
print('==========================')
print('truncated_df created.')
print('======= HEAD =============')
print(truncated_df.head())
print(f'Row Count: {len(truncated_df)}')
print('==========================')

# Sqlite3
database = "ccle.sqlite"
conn = sql3.connect(database)
truncated_df.to_sql(name='ccle', con=conn)
conn.close()
print('ccle db created')
print('==========================')


