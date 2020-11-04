import requests

metric_id = 'METRIC_ID'

params = {
	'api_key':'PRIVATE_API_KEY'
}

url = 'https://a.klaviyo.com/api/v1/metric/'+metric_id+'/export'

headers = {
   'content-type': 'application/json',
   'cache-control': 'no-cache'
}

response = requests.request('GET', url, headers=headers, params=params).json()

vals = []

for i in response['results']:
	for x in i['data']:
		f = x['values']
		v = float(''.join(list(map(str,f))))
		vals.append(v)

print(sum(vals))