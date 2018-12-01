import datetime
import os
path = (r'D:\Users\jong\PyProjects\Stocks\PSE screener')
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.linear_model import LinearRegression


end_date = ('11292018')
What_Stock1 = 'AC'
What_Stock2 = 'ALI'
What_Stock3 = '^PSEi'

os.chdir(path)
df = pd.read_csv('conso' + end_date + '.csv')
df['DATE'] = pd.to_datetime(df.DATE)
df.set_index('DATE', inplace=True)
df2 = df[df['TICKER'] == What_Stock1]
df3 = df[df['TICKER'] == What_Stock2]
df4 = df[df['TICKER'] == What_Stock3]

y = df2.CLOSE
x1 = df3.CLOSE
x2 = df4.CLOSE

reg = LinearRegression()
reg.fit(list(zip(x1, x2)), y)
b1, b2 = reg.coef_[0], reg.coef_[1]
b0 = reg.intercept_
print(f'y = {b0:.{3}} + {b1:.{3}}x1 + {b2:.{3}}x2')
yline = -1.4e+03 + 4.5*(x1) + 5.2*(x2)

#fig, ax = plt.subplot(4, 1, 1)
#scat = ax.scatter(x1, x2, c=yline, s=20, marker='o')

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(111, projection='3d')
scat = ax.scatter(x1, x2, c=yline, s=75, alpha=.5)
fig.colorbar(scat)
plt.show()
