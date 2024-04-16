import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], edgecolors='black')

    # Create first line of best fit
    res = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], res.intercept + res.slope*df['Year'], 'r', label='Linear Regression Line')

    # Create second line of best fit
    recent_years_df = df.loc[df['Year'] >= 2000]
    res_recent = linregress(recent_years_df['Year'], recent_years_df['CSIRO Adjusted Sea Level'])
    plt.plot(df['Year'], res_recent.intercept + res_recent.slope*df['Year'], 'g', label='Linear Regression Line - Recent')

    # Add labels and title
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    plt.title('Rise in Sea Level')
    plt.legend()

    # Set x ticks every 25 years
    plt.xticks(range(1850, 2100, 25))

    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()
