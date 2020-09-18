import pandas as pd
df = pd.read_csv('forestfires.csv')
df.set_index('month',inplace=True)
print("DC and ISI values of aug, sep, jun month :\n",df.loc[['aug','sep','jun'],['DC','ISI']])