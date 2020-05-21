import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:javascript&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store there API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
  repo_name = repo_dict['name']
  repo_url = repo_dict['html_url']
  repo_link = f"<a href='{repo_url}' style='color:#bf00ff'>{repo_name}</a>"
  repo_links.append(repo_link)
  stars.append(repo_dict['stargazers_count'])
  owner = repo_dict['owner']['login']
  description = repo_dict['description']
  label = f"{owner}<br /v>{description}"
  labels.append(label)

# Make visualization.
data = [{
  'type': 'bar',
  'x': repo_links,
  'y': stars,
  'hovertext': labels,
  'marker': {
    'color': '#5533FF',
    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
  },
  'opacity': 0.5,
}]

my_layout = {
  'title': 'Most-Starred Javascript Projects on GitHub',
  'titlefont': {'size': 28},
  'xaxis': {
    'title': 'Repository',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14,},
  },
  'yaxis': {
    'title': 'Stars',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Projects/DataVisualization/WorkingAPIs/Exercises/javascript_repos.html')