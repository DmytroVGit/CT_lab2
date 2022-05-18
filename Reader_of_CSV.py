import pandas as pd
import matplotlib.pyplot as plt
import s3fs

f=pd.read_csv('s3://ec2-44-204-90-57.lab/currency_rate.csv')

f_USD = f[f["cc"] == 'USD']
f_EUR = f[f["cc"] == 'EUR']
#f_EUR.plot(x="exchangedate", y="rate", figsize=(16, 8), label='EUR', fontsize='x-large')
#f_USD.plot(x="exchangedate", y="rate", figsize=(16, 8), label='USD', fontsize='x-large')
plt.figure(figsize = (30,15))
plt.plot(f_EUR['exchangedate'], f_EUR['rate'], 'b', label='EUR')
plt.plot(f_USD['exchangedate'], f_USD['rate'], 'r', label='USD')
plt.title('Графіки', {'fontsize': 24, 'fontweight': 'bold', 'color': 'green'})
plt.xlabel('exchangedate', {'fontsize': 20, 'color': 'black'})
plt.ylabel('rate', {'fontsize': 20, 'color': 'black'})
plt.legend(fontsize='xx-large')
current_figure = plt.gcf()
current_figure.autofmt_xdate()
plt.savefig('Plot.png')
plt.show()