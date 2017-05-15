from django.shortcuts import render
from django.utils import timezone
from .models import Rule

def policies_list(request):
    rules = Rule.objects.order_by('-priority')
    return render(request, 'policies/policies_list.html', {'rules': rules})

# Create your views here.
