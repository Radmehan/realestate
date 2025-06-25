from django.shortcuts import render
from .models import AddPlace,AddVillaApartment,Type
from django.http import HttpResponse
from math import ceil
from django.core.paginator import Paginator

# Create your views here.
def properties(request):
    allhomes = AddVillaApartment.objects.all()
    homes = AddVillaApartment.objects.all()
    # books = Product.objects.filter(cls__cls='Nursery') 
    per_page=12
    paginator = Paginator(homes, per_page=per_page)
    page_number = request.GET.get('page')
    books_page = paginator.get_page(page_number)

    context = {'allhomes': allhomes, 'homes':books_page}
    return render(request,'house/homes.html',context)


def home_single(request,id):
    house = AddVillaApartment.objects.filter(id=id)
    context = {'i':house[0]}
    return render(request,'house/home-single.html',context)

def places(request):
    allPlaces = []
    allPlace = AddPlace.objects.values('city','id')
    places = {item['city'] for item in allPlace}
    for city in places:
        place =AddPlace.objects.filter(city=city)
        n = len(place)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allPlaces.append([place,range(1,nSlides),nSlides])
        
    context = {'allPlaces': allPlaces}

    return render(request,'house/places.html',context)

def place_single(request, city):
    places = AddPlace.objects.filter(city=city)

    images = [place.image_id for place in places if place.image]

    try:
        apartment_type = Type.objects.get(villa_appartment__iexact='Apartment')
        villa_type = Type.objects.get(villa_appartment__iexact='Villa')
    except Type.DoesNotExist:
        apartment_type = villa_type = None

    apartments = AddVillaApartment.objects.filter(city=city, type=apartment_type) if apartment_type else []
    villas = AddVillaApartment.objects.filter(city=city, type=villa_type) if villa_type else []

    context = {
        'city': city,
        'places': places,
        'images': images,
        'image_count': len(images),
        'apartments' : apartments,
        'villas' : villas,
    }
    return render(request, 'house/place-single.html', context)



def place_quick_view(request,id):
    place = AddPlace.objects.filter(id=id)
    context = {'i':place[0]}
    return render(request,'house/palce_quick_view.html',context)