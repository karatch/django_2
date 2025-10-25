from django.shortcuts import render
from orm_model.models import Worker

def index(request):
    people = Worker.objects.all().order_by('-id')
    return render(request, 'index.html', {'people': people})
