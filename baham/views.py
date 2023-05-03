from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import loader
from django.contrib.auth.models import User

from baham.constants import COLOURS
from baham.enum_types import VehicleStatus
from baham.models import Vehicle, VehicleModel, UserProfile

# Create your views here.
def view_home(request):
    template = loader.get_template('home.html')
    context = {
        "navbar": "home"
    }
    return HttpResponse(template.render(context, request))

def view_index(request):
    template = loader.get_template('home.html')
    # Fetch the last 20 records
    vehicles = Vehicle.objects.filter(status=VehicleStatus.AVAILABLE.name).order_by('-date_added')[:18]
    all_vehicles = []
    current_user_id = request.user.id
    for vehicle in vehicles:
        owner = UserProfile.objects.get(pk=vehicle.owner.id)
        obj = {
            'vehicle_id': vehicle.vehicle_id,
            'registration_number': vehicle.registration_number,
            'colour': vehicle.colour,
            'vendor': vehicle.model.vendor,
            'model': vehicle.model.model,
            'type': vehicle.model.type,
            'owner_bio': owner.bio,
            'owner_town': owner.town,
            'owner_first_name': owner.user.first_name,
            'owner_last_name': owner.user.last_name,
            'picture1_url': vehicle.picture1
        }
        all_vehicles.append(obj)

    context = {
        "navbar": "home",
        "vehicles": all_vehicles
    }
    return HttpResponse(template.render(context, request))

def view_vehicles(request):
    template = loader.get_template('vehicles.html')
    vehicles = Vehicle.objects.filter(status=VehicleStatus.AVAILABLE.name).order_by('-date_added')
    all_vehicles = []
    current_user_id = request.user.id
    for vehicle in vehicles:
        owner = UserProfile.objects.get(pk=vehicle.owner.id)
        obj = {
            'vehicle_id': vehicle.vehicle_id,
            'registration_number': vehicle.registration_number,
            'colour': vehicle.colour,
            'vendor': vehicle.model.vendor,
            'model': vehicle.model.model,
            'type': vehicle.model.type,
            'owner_town': owner.town,
            'owner_name': owner.user.username,
            'picture1_url': vehicle.picture1,
            'picture2_url': vehicle.picture2,
            'allow_edit': current_user_id == owner.id
        }
        all_vehicles.append(obj)

    context = {
        "navbar": "vehicles",
        "vehicles": all_vehicles
    }
    return HttpResponse(template.render(context, request))

def view_vehicle(request, id):
    template = loader.get_template('editvehicle.html')
    vehicle = Vehicle.objects.get(pk=id)
    current_user_id = request.user.id
    owner = UserProfile.objects.get(pk=vehicle.owner.id)
    obj = {
        'vehicle_id': vehicle.vehicle_id,
        'registration_number': vehicle.registration_number,
        'colour': vehicle.colour,
        'vendor': vehicle.model.vendor,
        'model': vehicle.model.model,
        'type': vehicle.model.type,
        'owner_town': owner.town,
        'owner_first_name': owner.user.first_name,
        'owner_last_name': owner.user.last_name,
        'picture1_url': vehicle.picture1,
        'picture2_url': vehicle.picture2,
        'allow_edit': current_user_id == owner.id
    }
    context = {
        "navbar": "vehicles",
        "vehicle": obj
    }
    return HttpResponse(template.render(context, request))

def create_vehicle(request):
    template = loader.get_template('createvehicle.html')
    models = VehicleModel.objects.all().values_list('model_id', 'vendor', 'model', 'type').order_by('type', 'vendor', 'model').values()
    # FIXME: Is the below even required if the client desires only the owner to be able to create/alter vehicles?
    users = User.objects.filter(is_superuser=False, is_active=True).all().values_list('id', 'first_name', 'last_name', 'email').order_by('first_name', 'last_name').values()
    context = {
        "navbar": "vehicles",
        "models": models,
        "users": users,
        "colours": COLOURS,
    }
    return HttpResponse(template.render(context, request))

# Create your views here.
def view_aboutus(request):
    template = loader.get_template('aboutus.html')
    context = {
        "navbar": "aboutus"
    }
    return HttpResponse(template.render(context, request))
