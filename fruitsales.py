import pandas as pd

data = pd.DataFrame({"Apples": [35, 21], "Bananas": [41, 34]}, index=["2017 Sales", "2018 Sales"])

data.to_csv("fruit.csv", sep=",", encoding="utf-8")
