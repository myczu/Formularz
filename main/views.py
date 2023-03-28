from django.shortcuts import render
from .forms import VenueForm



def home(request):

    form = VenueForm()

    if request.method == 'POST':
        form = VenueForm(request.POST)
        if form.is_valid():
            form.save()

            
    context =  {'form':form}
    return render(request, 'home.html', context)
