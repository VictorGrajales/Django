from django.http import HttpResponse

# Utilities
from datetime import datetime
import json
import pdb

def hello_world(request):
    now = datetime.now().strftime('%b %dth %Y - %H:%M hrs')
    return HttpResponse('Current server time is {now}'.format(now=str(now)))

def numbers(request):
    get_numbers = request.GET['numbers'].split(',')

    numbers = []

    for number in get_numbers:
        numbers.append(int(number))

    data = {
        "numbers": numbers
    }

    json_data = json.dumps(data, indent=4)

    return HttpResponse(json_data, content_type='application/json')


def say_hi(request, name, age):

    if age < 18:
        message = 'Welcome {} you dont open'.format(name)
    else:
        message = '<h1>Welcome {} How are you?</h1>'.format(name)

    return HttpResponse(message)