import pandas as pd
# 1
pd.read_csv('input.txt', sep=" ", header=None).groupby([0]).sum().apply(lambda x: print((x[0] - x[2])  * x[1]))

# 2
outp = {'d': 0, 'a': 0}
for x in pd.read_csv('input.txt', sep=" ", header=None).replace({0: { "forward": 'f', "up": 'u', "down": 'd' }}).to_numpy():
    outp['d'] = outp['d'] + outp['a'] * x[1] if x[0] == 'f' else outp['d']
    outp['a'] = outp['a'] + (x[1] if x[0] == 'd' else 0) - (x[1] if x[0] == 'u' else 0)
print(outp['d'] * pd.read_csv('input.txt', sep=" ", header=None).groupby([0]).sum()[1][1])
