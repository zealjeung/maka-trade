import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
path = (r'D:\Users\jong\PyProjects\HelloWorld')
os.chdir(path)
CALhousing = pd.read_csv('housing.csv')
print(CALhousing.head())
print(CALhousing.info())
del CALhousing['longitude']
del CALhousing['latitude']
del CALhousing['ocean_proximity']
print(CALhousing.columns)
CALhousing.dropna(inplace=True)
CAL = CALhousing.loc[CALhousing['median_house_value']!=CALhousing['median_house_value'].max()]
print(CAL.describe())
sns.pairplot(CAL)
plt.tight_layout()
plt.show()
sns.distplot(CAL['median_house_value'])
plt.tight_layout()
plt.show()
sns.heatmap(CAL.corr())
plt.tight_layout()
plt.show()

X = CAL[['housing_median_age', 'total_rooms', 'total_bedrooms', 'population',
               'households', 'median_income']]
y = CAL['median_house_value']
sns.set_palette("GnBu_d")
sns.set_style('whitegrid')
sns.jointplot(x='median_house_value',y='median_income',data=CAL, kind='hex')
plt.tight_layout()
plt.show()
sns.lmplot(x='total_bedrooms',y='households',data=CAL)
plt.tight_layout()
plt.show()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)
from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(X_train,y_train)
# print the intercept
print(lm.intercept_)
predictions = lm.predict(X_test)
plt.scatter(y_test,predictions)
plt.xlabel('actual')
plt.ylabel('predictions')
plt.tight_layout()
plt.show()
sns.distplot((y_test-predictions),bins=35)
plt.tight_layout()
plt.show()

from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))

coeffecients = pd.DataFrame(lm.coef_,X.columns)
coeffecients.columns = ['Coeffecient']
print(coeffecients)
