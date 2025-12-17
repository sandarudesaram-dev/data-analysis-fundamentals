import pandas as pd

data = {
	"Name": ["Spongebob", "Patrick", "Squidward"],
	"Age": [30, 35, 50]
	}

df = pd.DataFrame(data, index=["Employee 1", "Employee 2", "Employee 3"])

print(df)

print()

# Add a new column
df["Job"] = ["Cook", "N/A", "Cashier"]

print(df)

print()

# Add a new row
new_row = pd.DataFrame([{"Name": "Sandy", "Age": 28, "Job": "Engineer"}], index=["Employee 4"])

df = pd.concat([df, new_row])

print(df)

print()

# Add new rows
new_rows = pd.DataFrame([{"Name": "Eugene", "Age": 60, "Job": "Manager"}, 			 {"Name": "Mr.Krabs", "Age": 65, "Job": "Owner"}],
index=["Employee 5", "Employee 6"])

df = pd.concat([df, new_rows])

print(df)