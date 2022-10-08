from django.shortcuts import render, get_object_or_404, redirect, reverse 
from django.http import HttpResponse
from django.views import generic
from django.core.paginator import Paginator
from django.db.models import Q
from django.contrib.auth.forms import User
from django.views.decorators.csrf import csrf_protect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.urls import reverse, reverse_lazy
from .models import Uzrasas, Kategorija
from .forms import RegistrationForm, UserUpdateForm, ProfilisUpdateForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

 

def index(request):
    num_uzrasai = Uzrasas.objects.all().count()
    num_kategorijos = Kategorija.objects.count()
    
    num_visits = request.session.get('num_visits', 1)
    request.session['num_visits'] = num_visits + 1

    context = {
        'num_uzrasai': num_uzrasai,
        'num_kategorijos': num_kategorijos,
        'num_visits': num_visits,
    }

    return render(request, 'library/index.html', context=context)


class UzrasasListView(generic.ListView):
    model = Uzrasas
    context_object_name = 'my_uzrasas_list'
    template_name = 'library/uzrasas_list.html'


class UzrasasDetailView(generic.DetailView):
    model = Uzrasas
    template_name = 'library/uzrasas_detail.html'


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

def filter(request):
    query = request.GET.get('query')
    search_results = Kategorija.objects.filter(Q(first_name__icontains=query))
    return render(request, 'library/filter.html', {'kategorijos': search_results, 'query': query})

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password'])
            messages.info(request, 'Registracija sėkminga')
            return redirect('library:register')
        
    else:
         form = RegistrationForm()
    return render(request, 'library/register.html', {'form': form})
@login_required
def profilis(request):
        if request.method == 'POST':
            u_form = UserUpdateForm(request.POST, instance=request.user)
            p_form = ProfilisUpdateForm(request.POST, request.FILES, instance=request.user.profilis)
            if u_form.is_valid() and p_form.is_valid():
                u_form.save()
                p_form.save()
                messages.success(request, f"Profilis atnaujintas")
                return redirect('library:profilis')
        else:
            u_form = UserUpdateForm(instance=request.user)
            p_form = ProfilisUpdateForm(instance=request.user.profilis)
        context = {
            'u_form': u_form,
            'p_form': p_form,
        }
        return render(request, 'library/profilis.html', context=context)

class LoanedUzrasaiByUserListView(LoginRequiredMixin,generic.ListView):
    model = Uzrasas
    context_object_name = 'uzrasai'
    template_name ='library/user_uzrasai.html'

    def get_queryset(self):
      return Uzrasas.objects.filter(title=self.request.user)


class UzrasasByUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = Uzrasas
    template_name = 'library/user_uzrasas.html'


class UzrasasByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Uzrasas
    fields = ['title', 'kategorija', 'summary', 'cover']
    success_url = reverse_lazy('library:myuzrasai')
    template_name = 'library/user_uzrasas_form.html'
    

    def get_absolute_url(self):
        """Nurodo konkretaus aprašymo galinį adresą"""
        return reverse('uzrasas-detail', args=[str(self.id)])


class UzrasasByUserUpdateView(LoginRequiredMixin,  generic.UpdateView):
    model = Uzrasas
    fields = ['title', 'kategorija', 'summary', 'cover']
    success_url = reverse_lazy('library:myuzrasai')
    template_name = 'library/user_uzrasas_form.html'
   
   

class UzrasasByUserDeleteView(LoginRequiredMixin,  generic.DeleteView):
    model = Uzrasas
    success_url = reverse_lazy('library:myuzrasai')
    template_name = 'library/user_uzrasas_delete.html'

  
class KategorijaByUserDetailView(LoginRequiredMixin, generic.DetailView):
    model = Kategorija
    template_name = 'library/user_kategorija.html'


class LoanedKategorijosiByUserListView(LoginRequiredMixin,generic.ListView):
    model = Kategorija
    context_object_name = 'kategorijos'
    template_name ='library/user_kategorijos.html'

    def get_queryset(self):
        return Kategorija.objects.filter(first_name=self)
   
class KategorijaByUserCreateView(LoginRequiredMixin, generic.CreateView):
    model = Kategorija
    fields = ['first_name', 'description']
    success_url = reverse_lazy('library:mykategorijos')
    template_name = 'library/user_kategorija_form.html'
  
class KategorijaByUserUpdateView(LoginRequiredMixin,  generic.UpdateView):
    model = Kategorija
    fields =['first_name', 'description']
    success_url = reverse_lazy('library:mykategorijos')
    template_name = 'library/user_kategorija_form.html'

class KategorijaByUserDeleteView(LoginRequiredMixin,  generic.DeleteView):
    model = Kategorija
    success_url = reverse_lazy('library:mykategorijos')
    template_name = 'library/user_kategorija_delete.html'
