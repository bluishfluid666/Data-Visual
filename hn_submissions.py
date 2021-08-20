import requests
from operator import itemgetter
from plotly.graph_objs import Bar
from plotly.offline import offline

url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
response_ids = r.json()
submission_dicts = []
for response_id in response_ids[:30]:
    url = f'https://hacker-news.firebaseio.com/v0/item/{response_id}.json'
    r = requests.get(url)
    response_dict = r.json()

    try:
        comments = response_dict['descendants']
    except:
        comments = 0

    submission_dict = {
        'title': response_dict['title'],
        'hn_link':  f"http://news.ycombinator.com/item?id={response_id}",
        'comments': comments,
    }
    submission_dicts.append(submission_dict)
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
        reverse=True)
#for submission_dict in submission_dicts:
#    print(f'\nArticle: {submission_dict["title"]}.')
#    print(f'Discussion link: {submission_dict["hn_link"]}.')
#    print(f'Comments: {submission_dict["comments"]}.')

xax = []
for submission_dict in submission_dicts:
    title = submission_dict['title'],
    art_url = submission_dict['hn_link']
    article = f'<a href="{art_url}">{title}</a>'
    xax.append(article)
yax = [sd['comments'] for sd in submission_dicts]

data = [{
    'type': 'bar',
    'x': xax,
    'y': yax,
}]

lay = {
    'title': 'Hacker News Top Articles Activity',
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 24},
        'tickfont': {'size': 10},
        },
    'yaxis': {
        'title': 'Comments',
        'titlefont': {'size': 24},
        'tickfont': {'size': 14},
    },
}
fig = {'data': data, 'layout': lay}
offline.plot(fig, filename='active_discussions.html')