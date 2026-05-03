import sys
sys.path.insert(1, 'D:\Programação\Pos\Python\POO')
import Data
import Usuario

from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import UsuarioModel
from .forms import UsuarioForm


# Create your views here.
class UsuarioListView(ListView):
    model = UsuarioModel
    queryset = UsuarioModel.objects.all()

class UsuarioCreateView(CreateView):
    model = UsuarioModel
    fields = '__all__'
    success_url = reverse_lazy('usuario-list')

class UsuarioUpdateView(UpdateView):
    model = UsuarioModel
    fields = '__all__'
    success_url = reverse_lazy('usuario-list')

class UsuarioDeleteView(DeleteView):
    model = UsuarioModel
    fields = '__all__'
    success_url = reverse_lazy('usuario-list')

class UsuarioDetailView(DetailView):
    queryset = UsuarioModel.objects.all()