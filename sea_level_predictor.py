import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')
  print(df.head())
  x = df['Year']
  y = df['CSIRO Adjusted Sea Level']

  # Create scatter plot
  fig, ax = plt.subplots()
  plt.scatter(x, y)

  # Add labels and title
  plt.xlabel('Year')
  plt.ylabel('Sea Level (inches)')
  plt.title('Rise in Sea Level')

  # Create first line of best fit
  res = linregress(x, y)

  x_future = pd.Series(range(1880, 2051))
  plt.plot(x_future,
           res.slope * x_future + res.intercept,
           color='orange',
           label='Line of Best Fit (Overall Data)')

  # Create second line of best fit
  recent_data = df[df['Year'] >= 2000]
  x_recent = recent_data['Year']
  y_recent = recent_data['CSIRO Adjusted Sea Level']
  slope_recent, intercept_recent, rvalue_recent, pvalue_recent, stderr_recent = linregress(
    x_recent, y_recent)

  x_future2 = pd.Series(range(2000, 2051))

  plt.plot(x_future2,
           slope_recent * x_future2 + intercept_recent,
           color='red',
           label='Line of Best Fit (Data from 2000 onwards)')
  plt.legend()
  # plt.show()

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
