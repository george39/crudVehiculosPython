from django.shortcuts import render
from pages.models import Page

#Create your views here.


def save_vehicle(request):

    return render(request, 'pages/create_vehicle.html', {
        'title': 'Crear vehículo'
    })
    # vehicle = Page(
    #     brand = 'brand',
    #     line = 'line',
    #     price = 'price'
    # )

    #vehicle.save()