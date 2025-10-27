from django.shortcuts import render
from orm_model.models import Worker

def index(request):
    # people = Worker.objects.all()
    people = Worker.objects.filter(id=25)
    return render(request, 'index.html', {'people': people})
