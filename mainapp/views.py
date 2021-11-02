from django.shortcuts import get_object_or_404, redirect, render
from mainapp.models import Vehicle
from django.http import HttpResponse, HttpRequest
from django.contrib import messages
from mainapp.forms import FormVehicle
from django.db.models import Q

# Create your views here.


# PABINA DE INICIO
def index(request):

    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })




# GUARDAR UN VEHÍCULO
def save_vehicle(request):


    if request.method == 'POST':
       
        brand = request.POST['brand']
        line = request.POST['line']
        color = request.POST['color']
        detail = request.POST['detail']
        price = request.POST['price']

        vehicle = Vehicle(
            brand = brand,
            line = line,
            color = color,
            detail = detail,
            price = price

        )
        
        vehicle.save()

        messages.success(request, f'El vehículo {vehicle.brand} se creo correctamente ')
        
        return redirect('create')
       
    else: 

        return HttpResponse("<h2>No se ha podido crear el vehículo</h2>")


def create_vehicle(request):
    return render(request, 'create_vehicle.html')





#DESABILITAR UN VEHÍCULO
def disable_vehicle(request, id):
    vehicle = Vehicle.objects.get(pk=id)

    vehicle.visible = 0
    vehicle.save()
    return redirect('vehicles')

    

#HABILITAR UN VEHÍCULO
def enable_vehicle(request, id):
    vehicle = Vehicle.objects.get(pk=id)

    vehicle.visible = 1
    vehicle.save()
    return redirect('vehicles')        



# OBTENER LA LISTA DE TODOS LOS VEHÍCULOS
def filter(request, brand): 
    
    vehicle = request.POST.get(pk=brand)

    return render(request, 'get_vehicles.html', {
        'vehicles': vehicle
    })            



# HABILITAR UN VEHÍCULO
def habilitar(request):
    vehicles = Vehicle.objects.all() 
    return render(request, 'habilitar_vehicle/habilitar_vehicle.html', {
        'vehicles': vehicles
    })    
    return render(request, 'habilitar_vehicle/habilitar_vehicle.html')
        
          

# EDITAR UN VEHÍCULO
def edit(request, id):
    vehicle = Vehicle.objects.get(pk=id)
    return render(request, 'edit_vehicle/edit.html')


 

 # BUSCAR POR MARCA           
def get_vehicles(request):
    busqueda = request.GET.get("buscar")
    vehicles = Vehicle.objects.all()

    if busqueda:
        vehicles = Vehicle.objects.filter(
            Q(brand__icontains = busqueda)
        ).distinct()

    return render(request, 'get_vehicles.html', {
        'vehicles': vehicles
    })   



#GUARDAR VEHÍCULO OTRO METODO
def create_full_vehicle(request):
    if request.method =='POST':
        vehicle_form = FormVehicle(request.POST)
        if vehicle_form.is_valid():
            vehicle_form.save()
            return redirect('create')
    else: 
       vehicle_form = FormVehicle()
    return render(request, 'edit_vehicle/edit.html', {'form': vehicle_form})  




# ACTUALIZAR UN VEHÍCULO
def update_vehicle(request, id):
    
    vehicle = get_object_or_404(Vehicle, id = id)
    if request.method == 'POST':
        vehicle_form = FormVehicle(request.POST, instance= vehicle)
        
        if vehicle_form.is_valid():
            vehicle_form.save()
            return redirect('vehicles')  
    else :
        vehicle_form = FormVehicle()                   
        return render(request, 'edit_vehicle/edit.html', {'form': vehicle_form}) 




