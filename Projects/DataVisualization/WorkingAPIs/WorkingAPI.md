# Working with APIs

## Overview

* Generate a visualization based on data retrieved.

* Make program use a web ***application programming interface*** (API) to automatically request specific information from a website's current data.

## Using a Web API

Web API is part of a website designed to interact with programs. These programs use specific URLs to request certain information called an ***API call***. The requested data will be returned in an processed format, such as JSON or CSV. Most apps that rely on external data sources, such as apps that integrate with social media sites, rely on API calls.

### Git and GitHub

We can use GitHub's API to request information about Python projects on the site, and then generate an interactive visualization of the popularity of these projects using Plotly. A place to help people mange their work on a project. We will write a program to automatically download information about the most-starred Python projects on GitHub, and then create informative visualization of these projects.

### Requesting Data Using an API Call

GitHub's API lets us request a wide range of information through API calls. An example of an API call:

<https://api.github.com/search/repositories?q=language:python&sort=stars>

The link returns the number of Python projects currently hosted on GitHub with information about the most popular Python repositories. It directs the search GitHub API call to search through all repositories for the query language of Python, sorting it by the number of stars.

The following snippet shows the first few lines of the response:

``` markdown
{
    "total_count": 3494012,
    "incomplete_results": false,
    "items": [
    {
        "id": 21289110,
        "node_id": "MDEwOlJlcG9zaXRvcnkyMTI4OTExMA==",
        "name": "awesome-python",
        "full_name": "vinta/awesome-python",
        --snip--
```

1. GitHub found an amount of Python projects.

2. The value "incomplete_results" is false meaning the request was successful.

3. The "items" returned are display in the list that follows containing details about the most popular Python projects on GitHub.

### Installing Requests

The Requests package allows a Python program to easily request information from a website and examine the response. Use pip to install Requests:

``` markdown
python -m pip install --user requests
```

### Processing an API Response

Now begin to automatically issue an API call and process the results by identifying the most starred Python projects on GitHub:

python_repos.py

``` python
import requests

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Store API response in a variable.
response_dict = r.json()

# Process results.
print(response_dict.keys())
```

1. Import the `requests` module.

2. Store the URL of the API call in the *url* variable.

3. GitHub is currently on the third version of its API, so the headers for the API call ask explicitly to use this version.

4. `get()` is called and passed it the URL and the header defined to the variable *r*.

5. Print the *status_code* to make sure the call went through successfully. (Status code 200 indicates a successful response.)

The API returns the information in JSON format, so we use `json()` method to convert the information to a Python dictionary, and store it in the *response_dict* dictionary.

``` markdown
Status code: 200
dict_keys(['total_count', 'incomplete_results', 'items'])
```

### Working with the Response Dictionary

With information from the API call stored as a dictionary, we can work with data stored.

python_repos.py

``` python
import requests

# Make an API call and store the response.
--snip--

# Store there API response in a variable.
response_dict = r.json()
print(f"Total repositories: {response_dict['total_count']}")

# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)
```

1. Print the value associated with 'total_count', which represents the total number of Python repositories on GitHub.

2. The value associated with 'items' is a list containing a number of dictionaries, each contains data about an individual Python repository and stored in *repo_dicts*.

3. For more detailed information about each repository, we pull out the first item from *repo_dicts* and store it in *repo_dict*.

4. We then print the number of keys in the dictionary to see how much information we have. Then finally print all the dictionary's keys to see what kind of information is included.

The results provide a clear picture of the data:

``` markdown
Status code: 200
Total repositories: 3494030
Repositories returned: 30

Keys: 73
archive_url
archived
assignees_url
--snip--
url
watchers
watchers_count
```

GitHub's API returns a lot of information about each repository. To understand the kind of information is available through an API is to read the documentation, or examine the information through code.

Now we pull the values for some of the keys in *repo_dict*:

python_repos.py

``` python
--snip--
# Explore information about the repositories.
repo_dicts = response-dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

# Examine the first repository.
repo_dict = repo_dicts[0]

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")
print(f"Created: {repo_dict['created_at']}")
print(f"Updated: {repo_dict['updated_at']}")
print(f"Description: {repo_dict['description']}")
```

1. Print the name of the project.

2. Use the key *owner* to access the dictionary, and then use key *login* to get the owner's login name.

3. Print how many stars the project has earned and the URL for the project's GitHub repository.

4. Then show when it was created and when it was last updated.

``` markdown
Selected information about first repository:
Name: system-design-primer
Owner: donnemartin
Stars: 84569
Repository: https://github.com/donnemartin/system-design-primer
Created: 2017-02-26T16:15:28Z
Updated: 2020-03-08T03:07:52Z
Description: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.
```

This is a summary of the current most-starred Python project on GitHub as of right now.

### Summarizing the Top Repositories

When making a visualization for the data, we want to include more than one repository. Let's write a loop to print selected information about each repository API call returns to include them in the visualization:

python_repos.py

``` python
--snip--
# Explore information about the repositories.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:
    print("\nSelected information about first repository:")
    print(f"\nName: {repo_dict['name']}")
    print(f"Owner: {repo_dict['owner']['login']}")
    print(f"Stars: {repo_dict['stargazers_count']}")
    print(f"Repository: {repo_dict['html_url']}")
    print(f"Created: {repo_dict['created_at']}")
    print(f"Updated: {repo_dict['updated_at']}")
    print(f"Description: {repo_dict['description']}")
```

1. Print an introductory message.

2. Loop through all the dictionaries in *repo_dicts*. Inside the loop, we print the name of each project, owner, how many stars, and URL on GitHub, and the project's description:

``` markdown
Selected information about each repository:

Name: system-design-primer
Owner: donnemartin
Stars: 85180
Repository: https://github.com/donnemartin/system-design-primer
Created: 2017-02-26T16:15:28Z
Updated: 2020-03-14T19:30:12Z
Description: Learn how to design large-scale systems. Prep for the system design interview.  Includes Anki flashcards.

Name: awesome-python
Owner: vinta
Stars: 80199
Repository: https://github.com/vinta/awesome-python
Created: 2014-06-27T21:00:06Z
Updated: 2020-03-14T19:33:07Z
Description: A curated list of awesome Python frameworks, libraries, software and resources

Name: public-apis
Owner: public-apis
Stars: 72148
Repository: https://github.com/public-apis/public-apis
Created: 2016-03-20T23:49:42Z
Updated: 2020-03-14T20:19:35Z
Description: A collective list of free APIs for use in software and web development.
```

### Monitoring API Rate Limits

Most APIs are rate limited, meaning there is a limit to how many requests is made in a certain amount of time. Go to <https://api.github.com/rate_limit> to check GitHub's limits.

``` markdown
{
  "resources": {
    "core": {
      "limit": 60,
      "remaining": 60,
      "reset": 1584221956
    },
    "search": {
      "limit": 10,
      "remaining": 10,
      "reset": 1584218416
    },
--snip--
```

1. The information we want is the rate limit for the search API at 10 requests per minute.

2. If we reach the quota, a short response notifies we reached the API limit. If the limit is reached, just wait until the quota resets.

***Many APIs require to register and obtain an API key to make API calls. Currently, GitHub has no requirement.***

## Visualizing Repositories Using Plotly

We can make an interactive bar chart with : the height of each bar will represent the number of stars the project has, and can click the bar's label to visit the GitHub project.

python_repos_visual.py

``` python
import requests

from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars = [], []
for repo_dict in repo_dicts:
  repo_names.append(repo_dict['name'])
  stars.append(repo_dict['stargazers_count'])

# Make visualization.
data = [{
  'type': 'bar',
  'x': repo_names,
  'y': stars,
}]

my_layout = {
  'title': 'Most-Starred Python Projects on GitHub',
  'xaxis': {'title': 'Repository'},
  'yaxis': {'title': 'Stars'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')
```

1. Import the `Bar` class and the `offline` module from `plotly`.

2. We don't import the `Layout` class since we use the dictionary to define the layout, similar to the `data` list in the earthquake map.

3. Create two empty lists to store the data to include in the initial chart for the name of each project to label the bars and number of stars to determine the height of the bars. In a loop, append the name of each project and the number of stars it has to the lists.

4. Inside the dictionary of the `data` list, we define the type of the plot and provides the data for the x- and y-values. The x-values are the names of the projects, and the y-values are the number of stars each project has been given.

5. We define the layout for the chart using the dictionary approach. Instead of the `Layout` class, we build a dictionary with the layout specifications we want to use by setting a title, and labels for each axis.

### Refining Plotly Charts

Here is a modified version of the `data` object for out chart that gives us a specific color and a clear border for each bar defining key-value pairs styling:

python_repos_visual.py

``` python
--snip--
data = [{
  'type': 'bar',
  'x': repo_names,
  'y': stars,
  'marker': {
    'color': 'rgb(60, 100, 150)',
    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
  },
  'opacity': 0.6,
}]
--snip--
```

The *marker* settings shown here affect the design of the bars. We set a custom blue color for the bars and specify that they be outlined with a dark gray line that 1.5 pixels wide and set the opacity of the bars to 0.6 to soften the appearance of the chart.

Next, we modified *my_layout*:

python_repos_visual.py

``` python
--snip--
my_layout = {
  'title': 'Most-Starred Python Projects on GitHub',
  'titlefont': {'size': 28},
  'xaxis': {
    'title': 'Repository',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
  'yaxis': {
    'title': 'Stars',
    'titlefont': {'size': 24},
    'tickfont': {'size': 14},
  },
}
--snip--
```

1. 'titlefont' key to define the font size of the overall chart title.

2. 'xaxis' dictionary to control the font size of the x-axis title ('titlefont') and the tick labels ('tickfont').

3. Define similar settings to the x-axis with the y-axis with individual nested dictionaries.

![python data](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/master/Projects/DataVisualization/WorkingAPIs/GitHub/1_python_projects.png "Most-starred Python projects with custom layout.")

### Adding Custom Tooltips

In Plotly, we can hover the cursor over an individual bar to show the information that the bar represents called a *tooltip*. In this case, our current visualization only shows the number of stars a project has. We can create a custom tooltip to show each project's description including the project's owner.

python_repos_visual.py

``` python
--snip--
# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_names, stars, labels = [], [], []
for repo_dict in repo_dicts:
  repo_names.append(repo_dict['name'])
  stars.append(repo_dict['stargazers_count'])

  owner = repo_dict['owner']['login']
  description = repo_dict['description']
  label = f"{owner}<br /v>{description}"
  labels.append(label)

# Make visualization.
data = [{
  'type': 'bar',
  'x': repo_names,
  'y': stars,
  'hovertext': labels,
  'marker': {
    'color': 'rgb(60, 100, 150)',
    'line': {'width': 1.5, 'color': 'rgb(25, 25, 25)'}
  },
  'opacity': 0.6,
}]
--snip--
```

1. Define a new empty list, *labels*, to hold the text we want to display for each project. In the loop to process the data, we pull the owner and the description for each project.

2. Plotly allows to use HTML code within text elements to generate a string for the label with a line break (`<br />`) between the project owner's username and the description. Then store the label in the list *labels*.

3. In the *data* dictionary, we add an entry with the key 'hovertext' and assign it the list we created. Plotly creates each bar to pull labels from the list and only display them when the mouse hovers a bar.

![custom tooltips](https://raw.githubusercontent.com/TysonNguyen/PythonCrashCourse_Notes/master/Projects/DataVisualization/WorkingAPIs/GitHub/2_python_projects.png "Most-starred Python projects with custom layout.")

### Adding Clickable Links to our Graph

Plotly allows to easily add HTML on text elements to a chart. We can use the x-axis labels as a way to let the viewer visit any project's home page on GitHub URL data.

python_repos_visual.py

``` python
--snip--
# Process results.
response_dict = r.json()
repo_dicts = response_dict['items']
repo_links, stars, labels = [], [], []
for repo_dict in repo_dicts:
  repo_name = repo_dict['name']
  repo_url = repo_dict['html_url']
  repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
  repo_links.append(repo_link)

  stars.append(repo_dict['stargazers_count'])
  --snip--

# Make visualization.
data = [{
  'type': 'bar',
  'x': repo_links,
  'y': stars,
  --snip--
}]
--snip--
```

1. Update the name of the list from *repo_names* to *repo_links* to more accurately communicate the kind of information put together.

2. Then pull the URL for the project from *repo_dict* and assign it to the temporary variable *repo_url*.

3. Generate a link to the project by HTML anchor tag, which as the form `<a href='URL'>link text</a>`. Then append the link to the list *repo_links*.

4. Use the *repo_links* list for the x-values in the chart. The result looks the same as before, but now the viewer can click any of the project names to visit the home page on GitHub.

We now have an interactive, informative visualization of data retrieved through an API.

## The Hacker News API

Let's take a look at Hacker News (<https://news.ycombinator.com/>) on how to use API calls on other websites. Hacker News is where people share articles about programming and technology, and engage in discussions about the articles. The Hacker News API provides access to data about all submissions and comments on the site, and API can be used without having to register for a key.

Here is a link to one article that returns information about it:

<https://hacker-news.firebaseio.com/v0/item/22834959.json>

When this URL is entered in a browser, the raw data is enclosed by braces, meaning a dictionary. We can run this URL through the `json.dump()` method for better formatting to examine the information.

hn_article.py

``` python
import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/item/22834959.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
response_dict = r.json()
readable_file = 'Projects/DataVisualization/WorkingAPIs/HackerNews/data/readable_hn_data.json'
with open(readable_file, 'w') as f:
    json.dump(response_dict, f, indent=4)
```

The output is a dictionary of information about the article with the ID 22834959:

``` markdown
{
    "by": "ikarandeep",
    "descendants": 449,
    "id": 22834959,
    "kids": [
        22835647,
        22836901,
        --snip--
    ],
    "score": 805,
    "time": 1586538301,
    "title": "Apple and Google partner on Covid-19 contact tracing technology",
    "type": "story",
    "url": "https://www.apple.com/newsroom/2020/04/apple-and-google-partner-on-covid-19-contact-tracing-technology/"
}
```

1. The key 'descendants' tells us the number of comments the article has received.

2. The key 'kids' provides the Ids of all comments made directly displayed in rank order.

3. There is also the title of the article, and a URL for the article.

The following URL returns a simple list of all the IDs of the current top articles on Hacker News:

<https://hacker-news.firebaseio.com/v0/topstories.json>

We can use this URL to find out which articles on the home page right now, and then generate a series of API calls. With this approach, we can print a summary of all the articles on the front page of Hacker News at the moment:

hn_submissions.py

``` python
from operator import itemgetter

import requests

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
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

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")
```

1. Make an API call, and then print the status of the response. IT returns a list containing the IDs of up to the 500 most popular articles on Hacker News at the time.

2. Then convert the response object to a Python list to store *submission_ids*. These IDs are used to build as et of dictionaries that each store information about one of the current submissions.

3. Set up an empty listed called *submission_dicts* to store these dictionaries. Loop through the IDs of the top 30 posts.

4. We make a new API call for each submission by generating a URL that includes the current value of *submission_id*. Then print the status of each request along with its ID to see whether it is successful.

5. Create a dictionary for the submission currently being processed, where the title of the submission, link to the discussion, and the number of comments the article has received is stored.

6. Then append each *submission_dict* to the list *submission_dicts*.

7. Sort the list of dictionaries by the number of comments by using a function called `itemgetter()`, which comes from the `operator` module. The key 'comments' is passed through the function, and it pulls the value associated with that key form each dictionary in the list. The `sorted()` function then uses this value as its basis for sorting the list in reverse order to place the most-commented stories first.

8. Once the list is ordered, loop through the list and print out three pieces of information about each of the top submissions: title, link to discussion page, and the number of comments the submission currently has.

For more information about the kind of information available through the Hacker News API: <https://github.com/HackerNews/API>

---

### TRY IT YOURSELF: API

**17-1. Other Languages**: Modify the API call in python_repos.py so it generates a chart showing the most popular projects in other languages. Try languages such as JavaScript, Ruby, C, Java, Perl, Haskell, and Go.

**17-2. Active Discussions**: Using the data from hn_submissions.py, make a bar chart showing the most active discussions currently happening on Hacker News. The height of each bar should correspond to the number of comments each submission has. The label for each bar should include the submission’s title and should act as a link to the discussion page for that submission.

**17-3. Testing python_repos.py**: In python_repos.py, we printed the value of status_code to make sure the API call was successful. Write a program called test_python_repos.py that uses unittest to assert that the value of status_code is 200. Figure out some other assertions you can make—for example, that the number of items returned is expected and that the total number of repositories is greater than a certain amount.

**17-4. Further Exploration**: Visit the documentation for Plotly and either the GitHub API or the Hacker News API. Use some of the information you find there to either customize the style of the plots we’ve already made or pull some
different information and create your own visualizations.

---

## Summary

What we learned in this chapter:

* Use APIs to write programs that automatically gather data and use it to create a visualization.
* Explore the GitHub API to find the most-starred Python projects along with the Hacker News API.
* How to use the Requests package to automatically issue an API call to GitHub and process results of the call.
