from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.
def index(request):
    return render(request, 'index.html')


def submit_query(request):
    query = request.GET['query']
    try:
        answer = eval(query)
        my_dict = {
            'query': query,
            'answer': answer,
            'error': False
        }
        return render(request, 'index.html', context=my_dict)
    except:
        my_dict = {
            'query': query,
            'error': True
        }
        return render(request, 'index.html', context=my_dict)
