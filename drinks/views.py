import imp
from tkinter.tix import DirSelectDialog
from django.http import JsonResponse
from .models import Drink
from .serializer import DrinkSerializer

def drink_list(request):
    drinks = Drink.objects.all()
    
    serialiser = DrinkSerializer(drinks, many=True)
    
    return JsonResponse(serialiser.data, safe=False)