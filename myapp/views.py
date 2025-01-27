from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'name': 'Watanabe Toru',
        'age' : 27,
        'job' : 'Debugger',
        'company': 'Sun Microsystem',
        'status' : 'Contract'
    }
    return render(request, 'index.html', context)

def counter(request):
    text = request.POST['text']
    words = len(text.replace(' ', '')) 
    
    return render(request, 'counter.html', {'words': words})

