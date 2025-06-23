import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# --- CONFIGURATION ---
# Set your data directory here or via environment variable
DATA_DIR = os.environ.get("MAKA_TRADE_DATA_PATH", os.path.abspath(os.path.dirname(__file__)))
CSV_FILENAME = 'housing.csv'  # Change as needed

# --- LOAD DATA ---
housing_csv = os.path.join(DATA_DIR, CSV_FILENAME)
if not os.path.isfile(housing_csv):
    raise FileNotFoundError(f"Data file not found: {housing_csv}")

CALhousing = pd.read_csv(housing_csv)
print(CALhousing.head())
print(CALhousing.info())

# --- DATA CLEANING ---
# Drop unnecessary columns if they exist
for col in ['longitude', 'latitude', 'ocean_proximity']:
    if col in CALhousing.columns:
        del CALhousing[col]

print(CALhousing.columns)
CALhousing.dropna(inplace=True)
CAL = CALhousing.loc[CALhousing['median_house_value'] != CALhousing['median_house_value'].max()]
print(CAL.describe())

# --- VISUALIZATION ---
sns.pairplot(CAL)
plt.tight_layout()
plt.show()

sns.histplot(CAL['median_house_value'], kde=True)
plt.tight_layout()
plt.show()

sns.heatmap(CAL.corr(), annot=True, fmt=".2f", cmap="coolwarm")
plt.tight_layout()
plt.show()

# --- PREP DATA FOR REGRESSION ---
feature_cols = ['housing_median_age', 'total_rooms', 'total_bedrooms', 'population',
                'households', 'median_income']
X = CAL[feature_cols]
y = CAL['median_house_value']

sns.set_palette("GnBu_d")
sns.set_style('whitegrid')

# --- JOINTPLOT & LMPLOT EXAMPLES ---
sns.jointplot(x='median_house_value', y='median_income', data=CAL, kind='hex')
plt.tight_layout()
plt.show()

sns.lmplot(x='total_bedrooms', y='households', data=CAL)
plt.tight_layout()
plt.show()

# --- LINEAR REGRESSION ---
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=101)

lm = LinearRegression()
lm.fit(X_train, y_train)

# Print the intercept
print("Intercept:", lm.intercept_)

# Predictions
predictions = lm.predict(X_test)
plt.scatter(y_test, predictions)
plt.xlabel('Actual')
plt.ylabel('Predictions')
plt.title('Actual vs. Predictions')
plt.tight_layout()
plt.show()

sns.histplot(y_test - predictions, bins=35, kde=True)
plt.title('Residuals Distribution')
plt.tight_layout()
plt.show()

# --- METRICS ---
from sklearn import metrics
print('MAE:', metrics.mean_absolute_error(y_test, predictions))
print('MSE:', metrics.mean_squared_error(y_test, predictions))
print('RMSE:', np.sqrt(metrics.mean_squared_error(y_test, predictions)))
