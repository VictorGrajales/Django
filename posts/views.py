

# Create your views here.
from django.shortcuts import render
from datetime import datetime

posts = [
    {
        'title': 'The programming is beautiful',
        'user': {
            'name': 'Eliaz One',
            'picture': 'https://picsum.photos/seed/plane/60/60',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1036/800/600',
    },
    {
        'title': 'Space',
        'user': {
            'name': 'Freedy Vega',
            'picture': 'https://picsum.photos/seed/car/60/60',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/903/800/600',
    },
    {
        'title': 'I love programming',
        'user': {
            'name': 'Eliaz One',
            'picture': 'https://picsum.photos/seed/men/60/60',
        },
        'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
        'picture': 'https://picsum.photos/id/1076/800/600',
    }
]

def list_posts(request):

    return render(request, 'feed.html', {'posts': posts})
