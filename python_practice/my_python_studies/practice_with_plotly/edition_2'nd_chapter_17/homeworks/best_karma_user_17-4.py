import csv
import requests

from plotly import subplots
from operator import itemgetter
from plotly import offline

def get_nameuser(id_stoty):
    """Returns user's name and the link to its page on Hacker News."""
    # getting each url adress to pull a username.
    url_story = f'https://hacker-news.firebaseio.com/v0/item/{id_stoty}.json?print=pretty'
    url_story_obj = requests.get(url_story)
    user_story_dict = url_story_obj.json()

    # get username.
    user = user_story_dict['by']
    # get link with username.
    link_page = f'https://news.ycombinator.com/user?id={user}'
    if len(user) > 5:
        username_link = f'<a href="{link_page}">{user[:5]}...</a>'
    else:
        username_link = f'<a href="{link_page}">{user}</a>'

    return user, username_link

def get_karmauser(user):
    """Returns user's karma."""
    user_url = f'https://hacker-news.firebaseio.com/v0/user/{user}.json?print=pretty'
    user_url_obj = requests.get(user_url)
    user_dict = user_url_obj.json()

    karma = user_dict['karma']
    number_submissions = len(user_dict['submitted']) 

    return karma, number_submissions

def get_url():
    """Gets url adress and append the getted url object in id_list."""
    # get url most the bests stories.
    url = 'https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty'
    url_obj = requests.get(url)
    print(f'Status code {url_obj.status_code}')
    # Saving getted data in list.
    id_list = url_obj.json()

    return id_list

def get_data_graph(id_list):
    """Gets data to build the graphs on the surface."""
    user_karma_dicts = []
    for id_stoty in id_list[:30]: # first 30 best stories.
        user, username_link = get_nameuser(id_stoty)
        karma, number_submissions = get_karmauser(user)

        user_karma_dict = {
            'nameuser_description': user,
            'username_link': username_link,
            'karma': karma,
            'num_sub': number_submissions,
        }

        if user_karma_dict not in user_karma_dicts:
            print(f'ID: {id_stoty}\tNameuser: {user}')
            print(f'User: {user}\tKarma: {karma}\n')

            user_karma_dicts.append(user_karma_dict)

    user_karma_dicts = sorted(user_karma_dicts, key=itemgetter('karma'),
        reverse=True)

    return user_karma_dicts

def get_lists_data(user_karma_dicts):
    """Replace data in lists."""
    un_descriptions, username_links, karmas, num_subs = [], [], [], []
    for user_karma_dict in user_karma_dicts:
        un_descriptions.append(user_karma_dict['nameuser_description'])
        username_links.append(user_karma_dict['username_link'])
        karmas.append(user_karma_dict['karma'])
        num_subs.append(user_karma_dict['num_sub'])

    return un_descriptions, username_links, karmas, num_subs

def get_traces(un_descriptions, username_links, karmas, num_subs):
    """Gets trace objects and returs of them in list."""
    trace1 = {
        'type': 'bar',
        'x': username_links,
        'y': karmas,
        'marker': {
            'line': {'width': 1.5},
        },
        'hovertext': un_descriptions,
        'opacity': 0.5,
        'name': 'Karmas',
    }

    trace2 = {
        'type': 'scatter',
        'x': username_links,
        'y': num_subs,
        'hovertext': un_descriptions,
        'mode': 'lines',
        'name': 'Submissions',
    }

    return [trace1, trace2]

def get_layout():
    """Gets layout (assigns a style for graph)."""
    layout = {
        'title': 'Karma of the best users on Hacker News',
        'titlefont': {'size': 24},
    }
    layout_axis1 = {
        'xaxis': {
            'title': 'Users',
            'titlefont': {'size': 16},
            'tickfont': {'size': 14},
            'tickangle': -90,
        },
        'yaxis': {
            'title': 'Karma',
            'titlefont': {'size': 16},
            'tickfont': {'size': 14},
        },
    }

    layout_axis2 = {
        'xaxis2': {
            'title': 'Users',
            'titlefont': {'size': 16},
            'tickfont': {'size': 14},
            'tickangle': -90,
        },
        'yaxis2': {
            'title': 'Number of submissions',
            'titlefont': {'size': 16},
            'tickfont': {'size': 14},
        },
    }

    return [layout, layout_axis1, layout_axis2]

def get_graph(un_descriptions, username_links, karmas, num_subs):
    """Builds a graph."""
    data = get_traces(un_descriptions, username_links, karmas, num_subs)
    layout_settings = get_layout()

    fig = subplots.make_subplots(rows=1, cols=2, specs=[[{}, {}]],
        subplot_titles=('Analisys of karma', 'Analisys of submissions'))

    fig.append_trace(data[0], 1, 1)
    fig.append_trace(data[1], 1, 2)

    for set_layout in layout_settings:
        fig['layout'].update(set_layout)
        fig['layout'].update(set_layout)
        fig['layout'].update(set_layout)

    offline.plot(fig, filename='karmas_users.html')

if __name__ == '__main__':
    id_list = get_url()
    user_karma_dicts = get_data_graph(id_list)
    un_descriptions, username_links, karmas, num_subs = get_lists_data(
        user_karma_dicts)
    get_graph(un_descriptions, username_links, karmas, num_subs)