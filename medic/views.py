from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from medic.models import Medic
from medic.serializers import MedicSerializer


# Create your views here.
@csrf_exempt
def medic_list(request):
    """
    List all or create a new medic
    """
    if request.method == 'GET':
        medic = Medic.objects.all()
        serializer = MedicSerializer(medic, many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MedicSerializer(data=data)
        if serializer.is_valid():
            serilizer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status(400))

@csrf_exempt
def medic_detail(request, pk):
    """
    Retrieve, update or delete a medic.
    """
    try:
        medic = Medic.objects.get(pk=pk)
    except Medic.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = MedicSerializer(medic)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MedicSerializer(medic, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        medic.delete()
        return HttpResponse(status=204)