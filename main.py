# Ty Robertson
# Application designed to check certain water quality (temperature per this dataset) and find whether
# the current numbers are suitable for user's wanted level.

from datetime import date
import pandas as pd
newHeaders = ['dataTime', 'timeInts', 'temps']
waterData = pd.read_csv('WaterQuality.csv', names=newHeaders, header=0, usecols=[0, 1, 2])

print(waterData)
