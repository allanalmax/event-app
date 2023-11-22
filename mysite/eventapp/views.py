from django.shortcuts import render, redirect
from .models import CreateEvent
from .forms import EventForm
from django.contrib.auth.decorators import login_required
from django.template import loader
from django.http import HttpResponse

# Create your views here.
@login_required
def index(request):
    template = loader.get_template('eventapp/index.html')
    context = {}
    return HttpResponse(template.render(context, request))

@login_required
def create_event(request):
    if request.method == 'POST':
        form = EventForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('eventapp:show_data')
    else:
        form = EventForm()
        
    return render(request, 'eventapp/create_event.html', {'form': form})

@login_required  
def show_data(request):
    events = CreateEvent.objects.all()
    return render(request, 'eventapp/show_data.html', {'events': events})

