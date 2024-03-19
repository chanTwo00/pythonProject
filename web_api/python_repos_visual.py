import requests

from plotly import offline
from plotly.graph_objs import Bar

# 执行API调用并储存相应
url = 'https://api.github.com/search/repositories?q=languange:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f'Status code: {r.status_code}')

# 处理结果
response_dict = r.json()
repo_dicts = response_dict['items']
# repo_names, stars, lables = [], [], []
repo_links, stars, lables = [], [], []
for repo_dict in repo_dicts:
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    stars.append(repo_dict['stargazers_count'])

    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    lable = f"{owner}<br />{description}"
    lables.append(lable)

# 可视化
data = [{
    'type': 'bar',
    'x': repo_links,
    'y': stars,
    'hovertext': lables,
    'marker': {
        'color': 'rgb(60, 100, 150)',
        'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
    },
    'opacity': 0.6,
}]
my_layout = {
    'title': 'GitHub上最受欢迎的python项目',
    'title_font': {'size': 28},
    'xaxis': {'title': 'Repository',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
    },
    'yaxis': {'title': 'Stars',
              'titlefont': {'size': 24},
              'tickfont': {'size': 14},
    },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')

