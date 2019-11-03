from __future__ import unicode_literals
from django.shortcuts import render
from .models import restaurant

def main(request):
    restos = restaurant.objects.all().order_by('-aggregate_rating')
    context = {
        'restaurants': restos,
    }
    return render(request, 'index.html', context)
