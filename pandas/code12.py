# EXAMPLE: DataFrame #

import pandas as pd

data = {"Name": ["Jane", "Martin", "Jacob", "Holly"],
	"Semester": [1, "Pre Academic", 1, 3],
	"GPA": [3.98, 2.89, 4.00, 3.75]
	}

df = pd.DataFrame(data, index=["Student 001", "Student 002", "Student 003", "Student 004"])

print(df)