from operator import itemgetter
from plotly import offline

import requests
import plotly.graph_objs as go

def get_most_popular(average_value, comments):
    for index, comment in enumerate(comments):
        if comment > average_value:
            idx_x = index

    return idx_x

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
        'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict.get('descendants', 0),
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
    reverse=True)


# Save data in lists.
name_links, comments, description_title = [], [], []
for submission_dict in submission_dicts:
    link = submission_dict['hn_link']
    title = submission_dict['title']
    comment = submission_dict['comments']
    description_title.append(f'Stars: {comment}<br />{title}.')

    if len(title) > 11:
        title = f'{title[:12]}...'

    name_links.append(f"<a href='{link}'>{title}</a>")
    comments.append(comment)

average_value = sum(comments) / len(comments)
idx_x = get_most_popular(average_value, comments) + 0.4 # gets maximal index
    #of the discussion that is hight than average value of all numver comments.

# 17-2. Active Discussions:
# Build the graph.
data = [{
    'type': 'bar',
    'x': name_links,
    'y': comments,
    'hovertext': description_title,
    'marker': {
        'color': comments,
        'colorscale': [
            [0, 'rgba(250, 230, 36, 0.6)'],
            [0.25, 'rgba(70, 191, 110, 0.6)'],
            [0.5, 'rgba(32, 146, 139, 0.6)'],
            [0.75, 'rgba(53, 94, 140, 0.6)'],
            [1, 'rgba(68, 2, 85, 0.6)']],
        'reversescale': True,
        'colorbar': {'title': 'lksdfj'},
        'line': {'width': 0.5, 'color': 'rgb(10, 10, 10)'},
    },
    #'opacity': 0.5,
}]
layout = {
    'title': 'Most discussion article.',
    'titlefont': {'size': 28},
    'xaxis': {
        'title': 'Arcticles',
        'titlefont': {'size': 24},
        'tickfont': {'size': 16},
    },
    'yaxis': {
        'title': 'Number of Stars',
        'titlefont': {'size': 24},
        'tickfont': {'size': 16},
    },
    'shapes': [{
        'type': 'rect',
        'xref': 'x',
        'yref': 'y',
        'x0': -0.4,
        'y0': 0,
        'x1': idx_x,
        'y1':comments[0],
        'fillcolor': '#b3b3b3',
        'opacity': 0.2,
        'layer': 'below',
        'line': {
            'width': 0,
        }
    }],
    'annotations': [{
        'text': 'Most discussion articles',
        'x': idx_x,
        'y': comments[0],
    }],
}
offline.plot({'data': data, 'layout': layout}, filename='discussion.html')