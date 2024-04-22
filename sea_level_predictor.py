import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv('epa-sea-level.csv')

# Creating scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue', label='Data')
#plt.show()

# Performing linear regression on all data
slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
plt.plot(df['Year'], slope*df['Year'] + intercept, color='red', label='Best Fit Line (1880-2013)')
plt.show()

# Performing linear regression from year 2000 onwards
df_recent = df[df['Year'] >= 2000]
slope_recent, intercept_recent, _, _, _ = linregress(df_recent['Year'], df_recent['CSIRO Adjusted Sea Level'])
plt.plot(df_recent['Year'], slope_recent*df_recent['Year'] + intercept_recent, color='green', label='Best Fit Line (2000-Present)')

# Predicting sea level rise in 2050
plt.plot([df['Year'].iloc[-1], 2050], [df['CSIRO Adjusted Sea Level'].iloc[-1], slope*2050 + intercept], 'r--', label='Prediction (1880-2050)')
plt.plot([df_recent['Year'].iloc[-1], 2050], [df_recent['CSIRO Adjusted Sea Level'].iloc[-1], slope_recent*2050 + intercept_recent], 'g--', label='Prediction (2000-2050)')

# Adding labels and title
plt.xlabel('Year')
plt.ylabel('Sea Level (inches)')
plt.title('Rise in Sea Level')
plt.legend()

# Save and show plot
plt.savefig('sea_level_rise.png')
plt.show()
