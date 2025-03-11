import pandas as pd
import matplotlib as plt

mydataset = {
    'cars':["BMW", "Honda", "Toyota"],
    'passing':[3, 8, 2],
}

print(pd.DataFrame(mydataset))
print(pd.__version__)
print(pd.Series([1,2,3], index=['A','B','C']))

calories = {
    'day1': 2000,
    'day2': 1000,
    'day3': 3000,
}

print(pd.Series(calories))
print(pd.Series(calories, index=['DAY_A','DAY_B']))
print(pd.Series(calories, index=['day1','day3']))
print(pd.read_json('test.json'))

import pandas as pd

data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.read_csv('test.csv')
df.plot()
plt.show()
df["Date"] = pd.to_datetime(df["Date"])

print(df.to_string())
