from operator import itemgetter

import requests
from plotly.graph_objs import bar
from plotly import offline

# Make an API call to Hacker News to store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []

# Top 10 submission on HackerNews. 
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# Lists for data plot.
submission_labels = []
submission_links = []
comments = []

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion Link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

    # Clickable link for x-axis and title.
    title = submission_dict['title']
    url = submission_dict['hn_link']
    submission_link = f"<a href='{url}'>{title}</a>"
    submission_links.append(submission_link)

    label = submission_dict['title']
    submission_labels.append(label)
    comments.append(submission_dict['comments'])

# Make visualization for most active discussion posts.
data = [{
    'type': 'bar',
    'x': submission_links,
    'y': comments,
    'marker': {
        'color': 'orange',
        'line': {'width': 1.5, 'color': 'black'}
    },
    'opacity': 0.5,
    'text': comments,
    'textposition': 'auto',
}]
 

my_layout = {
     'title': 'Top 10 Active HackerNews Articles',
     'titlefont': {'size': 24},
     'xaxis': {
         'title': 'Article',
         'titlefont': {'size': 20},
         'tickfont': {'size': 14},
     },
     'yaxis': {
         'title': 'Comments',
         'titlefont': {'size': 20},
         'tickfont': {'size': 14},
     },
 }

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='Projects/DataVisualization/WorkingAPIs/Exercises/hn_discussions.html')