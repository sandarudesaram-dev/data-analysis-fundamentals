import pandas as pd

# DataFrame = A tabular data structure with rows and colums. (2 Dimensional). Similar to an Excel spreadsheet.

data = {
	"Name": ["Spongebob", "Patrick", "Squidward"],
	"Age": [30, 35, 50]
	}

df = pd.DataFrame(data)

print(df)