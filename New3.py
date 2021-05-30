import pandas as pd


a = list(i*10 for i in range(10))
print(type(a))
df = pd.DataFrame({'A': a,
                   'B': [12, 22, 32],
                   'C': [13, 23, 33]},
                  index=['ONE', 'TWO', 'THREE'])

print(df)