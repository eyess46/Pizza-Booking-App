from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .forms import OrderForm
from .models import Order
from django.utils import timezone 

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = OrderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f'Thank You For Choosing Us, Your Request Is On its Way.')
            return render(request, 'index.html')
    else:
        form = OrderForm

    return render(request, 'index.html', {'form': form})

def about(request):

    return render(request, 'about.html') 

def contact(request):

    return render(request, 'contact.html') 



        


