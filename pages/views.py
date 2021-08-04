from django.shortcuts import render
from .models import Team
from cars.models import Car


# Create your views here.
def home(request):
    # TODO  fetch teams data --car data
    teams = Team.objects.all()
    all_cars = Car.objects.all()
    # todo values will not repeat in search div
    featured_cars = Car.objects.order_by('-created_dated').filter(is_featured =True)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    data = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'pages/home.html', data)


def about(request):
    # TODO  fetch teams data
    teams = Team.objects.all()
    data = {
        'teams': teams,
    }
    return render(request, 'pages/about.html',data)


def contact(request):
    return render(request, 'pages/contact.html')


def services(request):
    return render(request, 'pages/services.html')
