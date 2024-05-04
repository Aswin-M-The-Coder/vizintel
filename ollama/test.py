import pandas as pd

# Read the CSV file
df = pd.read_csv("data.csv")

first_10_rows = df.head(10)
columns = df.columns

formatted_data = ",".join(columns) + "\n"  # Add column names
formatted_data += "\n".join([",".join(map(str, row)) for row in first_10_rows.values])


print(formatted_data)

x=input("")
with open("answer.txt", "w") as file:
    file.write(str(formatted_data))