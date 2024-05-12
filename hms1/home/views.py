from django.shortcuts import render
from django.http import HttpResponse
from .models import Departments,Doctors, Booking
from .forms import BookingForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def booking(request):
    if request.method == "POST":
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form = {
        'form': form
    }
    return render(request, 'booking.html', dict_form)

def booked(request):
    booked = Booking.objects.all()
    context = {
        'booked_appointments' : booked
    }
    template = "booked.html"

    return render(request, template, context)


def doctors(request):
    dict_docs = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html' , dict_docs)

def contact(request):
    return render(request, 'contact.html') 

def department(request):
    dict_dept={
        'dept': Departments.objects.all()
    }
    return render(request, 'department.html', dict_dept)      

def doctor_search(request):
    query = request.GET.get('q')
    results = Doctors.objects.filter(doc_name__icontains = query)
    template = 'doctors_search.html'
    context = {
        'results' : results,
        'query' : query
    }
    return render(request, template, context)