from django.shortcuts import render

def carte_view(request):
    return render(request, 'carte.html')