import requests
import matplotlib.pyplot as plt
import datetime

owner = 'tiangolo'
repo = 'fastapi'
url = 'https://api.github.com/repos/' + owner + '/' + repo + '/commits'
response = requests.get(url)
result = response.json()

year = []
for i in range(len(result)):
    t = result[i]['commit']['author']['date'].split('-')
    y, m, d = int(t[0]), int(t[1]), int(t[2][:2])
    date = datetime.datetime(y, m, d)
    if date.strftime('%d-%m-%y') not in year:
        year.append(date.strftime('%d-%m-%y'))


commits = {
    'name': list(set(
        [
            result[i]['commit']['author']['name'] for i in range( len(result) )
        ]
    )),
    'count': [1, 30]
}

fig, ax = plt.subplots()
ax.stackplot(year, commits['count'], labels=commits['name'])
ax.legend(loc='upper center')
ax.set_title('Commits of fastapi')
ax.set_xlabel('Date')
ax.set_ylabel('Number of commits')

plt.show()