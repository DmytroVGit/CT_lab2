import requests
import json

res = []
NBU_url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json&date=20210101'
s = NBU_url[:-4]
l = ['01', '01']

for i in range(1,13):
	if i < 10:
		i = '0' + str(i)
	for j in (1,17):
		if j == 1:
			j = '0' + str(1)
		l[0] = str(i)
		l[1] = str(j)
		#print(l)
		#print(s + ''.join(l))
		response = requests.get(s + ''.join(l))
		for r in response.json():
			if r['cc'] == 'USD' or r['cc'] == 'EUR':
				#print(r)
				d = {}
				for k in r.keys():
					if k in ('cc','rate', 'exchangedate'):
						d[k] = r[k]
				res.append(d)

#print(res)
#jsonString = json.dumps(res)
with open("exchange.json", "w") as writer:
    json.dump(res, writer)
#print('-'*50 + ' jsonString ' + '-'*50)
#print(jsonString)