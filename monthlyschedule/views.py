from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def index(request):
    #return HttpResponse(" empty index page")
    # Render the HTML template index.html with the data in the context variable.

    # Number of visits to this view, as counted in the session variable.
    # https://docs.djangoproject.com/en/5.0/topics/http/sessions/
    date_range = range(1, 31)
    person_range = ['Bill', 'Alfred', 'Tomas', 'Juan']
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    return render(request,
                  'index.html',
                  context={
                      'num_visits': num_visits,
                      'date_range': date_range,
                      'person_range': person_range
                  })
