from django.shortcuts import render

def policies_list(request):
    return render(request, 'policies/policies_list.html', {})

# Create your views here.
