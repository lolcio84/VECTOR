from django.shortcuts import render
from django.http import HttpResponse
from .models import Photo

# Create your views here.

def hello(request):
    return HttpResponse("Hello user")

def inter(request):

    count = request.session.get("counter", 0)

    if request.method == "POST":
        count +=1
        request.session["counter"] = count


    return render(request, "inter.html", {"count": count})

def hub(request):
    return render(request, "hub.html")

def upload_photo(request):
    if request.method == "POST" and request.FILES.get("myfile"):
        image_file = request.FILES["myfile"]
        new_photo = Photo.objects.create(image = image_file)

        return render(request, "upload.html", {"photo": new_photo})
    
    return render(request, "upload.html")

def show_photos(request):
    # Pobieramy wszystkie zdjęcia z bazy danych
    all_photos = Photo.objects.all()
    return render(request, "show.html", {"photos": all_photos})



