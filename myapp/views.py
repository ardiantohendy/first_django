from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature(1, "Layanan Kami Cepat", "pemesanan makanan kami dibuat oleh chef ternama sehingga penyajiannya cepat dan juga berkualitas", "bi bi-clipboard-data")
    feature2 = Feature(2, "Layanan Kami Berkualitas", "Semua masakkan kami berkualitas tinggi karena dimasak oleh para chef yang ahli dalam bidangnya", "bi bi-gem")
    feature3 = Feature(3, "Dapat Dipesan Secara Daring", "Semua menu kami dapat dipesan secara daring melalui aplikasi Yummy yang tersedia di Playstore dan Appstore", "bi bi-inboxes")

    features = [feature1, feature2, feature3]

    return render(request, 'index.html', {'features' : features})

def counter(request):
    text = request.POST['text']
    words = len(text.replace(' ', '')) 
    
    return render(request, 'counter.html', {'words': words})

