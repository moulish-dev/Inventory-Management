from django.shortcuts import render

# Create your views here.

def base_dashboard(request):
    return render(request, 'orders/base_dashboard.html' )
