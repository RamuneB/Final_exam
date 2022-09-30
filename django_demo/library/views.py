from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages

from .models import Uzrasas, Kategorija
from .forms import RegistrationForm


def index(request):
    # Suskaičiuokime keletą pagrindinių objektų
    num_uzrasai = Uzrasas.objects.all().count()
    #num_instances = UzrasasInstance.objects.all().count()
    
    # Laisvos knygos (tos, kurios turi statusą 'g')
    #num_instances_available = UzrasasInstance.objects.filter(status__exact='g').count()
    
    # Kiek yra autorių    
    num_kategorijos = Kategorija.objects.count()
    
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    # perduodame informaciją į šabloną žodyno pavidale:
    context = {
        'num_uzrasai': num_uzrasai,
        #'num_instances': num_instances,
       # 'num_instances_available': num_instances_available,
        'num_kategorijos': num_kategorijos,
        'num_visits': num_visits,
    }

    # renderiname index.html, su duomenimis kintamąjame context
    return render(request, 'library/index.html', context=context)


class UzrasasListView(generic.ListView):
    model = Uzrasas
    context_object_name = 'my_uzrasas_list'
    template_name = 'library/uzrasas_list.html'



class UzrasasDetailView(generic.DetailView):
    model = Uzrasas


def kategorijos(request):
    paginator = Paginator(Kategorija.objects.all(), 2)
    page_number = request.GET.get('page')
   
    paged_kategorijos = paginator.get_page(page_number)
    context = {
        'kategorijos': paged_kategorijos
    }
    return render(request, 'library/kategorijos.html', context)


def kategorija(request, kategorija_id):

    selected_kategorija = get_object_or_404(Kategorija, pk=kategorija_id)
    context = {
        'kategorija': selected_kategorija
    }
    return render(request, 'library/kategorija.html', context)


def search(request):
    query = request.GET.get('query')
    search_results = Uzrasas.objects.filter(Q(title__icontains=query) | Q(summary__icontains=query))
    return render(request, 'library/search.html', {'uzrasai': search_results, 'query': query})

'''
def register(request):
    if request.method == 'POST':
        # pasiimame reikšmes iš registracijos formos
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # tikriname, ar sutampa slaptažodžiai
        if password == password2:
            # tikriname, ar neužimtas username
            if User.objects.filter(username=username).exists():
                messages.error(request, f'Vartotojo vardas {username} užimtas!')
                return redirect('library:register')
            else:
                # tikriname, ar nėra tokio pat email
                if User.objects.filter(email=email).exists():
                    messages.error(request, f'Vartotojas su el. paštu {email} jau užregistruotas!')
                    return redirect('library:register')
                else:
                    # jeigu viskas tvarkoje, sukuriame naują vartotoją
                    User.objects.create_user(username=username, email=email, password=password)
                    messages.info(request, 'Registracija sėkminga')
        else:
            messages.error(request, 'Slaptažodžiai nesutampa!')
            return redirect('library:register')

    return render(request, 'library/register.html')
'''
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
    else:
         form = RegistrationForm()
    return render(request, 'library/register.html', {'form': form})