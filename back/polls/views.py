from django.http import *
from polls.models import *
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def index(request):

    return HttpResponse("Index")


@csrf_exempt
def add(request):

    data = json.loads(request.body.decode('utf-8'))

    persona = tablaUNO(nombre=data['nombre'], edad=data['edad'])

    persona.save()

    return HttpResponse("agregado")




@csrf_exempt
def delete(request):

    data = json.loads(request.body.decode('utf-8'))

    persona = tablaUNO.objects.get(id=data['id'])

    persona.delete()

    return HttpResponse("borrado")


@csrf_exempt
def update(request):

    data = json.loads(request.body.decode('utf-8'))

    persona = tablaUNO.objects.get(id=data['id'])

    persona.nombre=data['nombre']

    persona.edad=data['edad']

    persona.save()

    return HttpResponse("editado")




@csrf_exempt
def select(request):

    listaPersonas = serializers.serialize("json", tablaUNO.objects.all())

    data = {"Resultados": json.loads(listaPersonas)}

    return JsonResponse(data)
