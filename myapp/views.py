from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 1
    feature1.title = "Layanan Kami Cepat"
    feature1.desc = "pemesanan makanan kami dibuat oleh chef ternama sehingga penyajiannya cepat dan juga berkualitas"
    feature1.icon = "bi bi-clipboard-data"

    feature2 = Feature()
    feature2.id = 2
    feature2.title = "Layanan Kami Berkualitas"
    feature2.desc = "Semua masakkan kami berkualitas tinggi karena dimasak oleh para chef yang ahli dalam bidangnya"
    feature2.icon = "bi bi-gem"

    feature3 = Feature()
    feature3.id = 3
    feature3.title = "Dapat Dipesan Secara Daring"
    feature3.desc = "Semua menu kami dapat dipesan secara daring melalui aplikasi Yummy yang tersedia di Playstore dan Appstore"
    feature3.icon = "bi bi-inboxes"

    features = [feature1, feature2, feature3]


    return render(request, 'index.html', {'features' : features})

def counter(request):
    text = request.POST['text']
    words = len(text.replace(' ', '')) 
    
    return render(request, 'counter.html', {'words': words})

