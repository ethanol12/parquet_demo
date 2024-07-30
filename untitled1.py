import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Create a sample dataset
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'date_of_birth': pd.to_datetime(['1990-01-01', '1985-05-15', '1992-07-30', '1988-03-22', '1995-12-10'])
}

df = pd.DataFrame(data)

# Convert the Pandas DataFrame to an Arrow Table
table = pa.Table.from_pandas(df)

# Write the table to a Parquet file
pq.write_table(table, 'sample_dataset.parquet')

# Read the Parquet file back into a Pandas DataFrame
df_read = pd.read_parquet('sample_dataset.parquet')

# Query the date_of_birth column
result = df_read[df_read['date_of_birth'] > '1990-01-01']

print("Parquet file written and queried successfully.")
print(result)
