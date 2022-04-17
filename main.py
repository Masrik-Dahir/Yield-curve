from pandas_datareader.data import DataReader as dr
import quandl
import matplotlib.pyplot as plt


syms = ['DGS10', 'DGS5', 'DGS2', 'DGS1MO', 'DGS3MO']
yc = dr(syms, 'fred') # could specify start date with start param here
names = dict(zip(syms, ['10yr', '5yr', '2yr', '1m', '3m']))
yc = yc.rename(columns=names)
yc = yc[['1m', '3m', '2yr', '5yr', '10yr']]

print(yc)

# yc.loc['2016-06-01'].plot(label='Jun 1')
# yc.loc['2016-06-02'].plot(label='Jun 2')
# plt.legend(loc=0)