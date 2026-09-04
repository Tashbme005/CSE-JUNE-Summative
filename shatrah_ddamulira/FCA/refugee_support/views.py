from django.shortcuts import redirect, render
from .forms import RefugeeForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def registration_form(request):
    form = RefugeeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('registration_form')

    return render(request, 'registration_form.html', {'form': form})

def view_forms(request, pk=None):
    return render(request, 'registration_form.html')

def update_form(request, pk=None):
    return render(request, 'registration_form.html') 

def delete_form(request, pk=None):
    return render(request, 'registration_form.html')