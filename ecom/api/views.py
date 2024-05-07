from django.http import JsonResponse

# Create your views here.
def home(request):
    return JsonResponse({'name':'Sai kumar','description':'Ecommerce website using django and react'})