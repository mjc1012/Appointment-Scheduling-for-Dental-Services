from typing import Coroutine
from django.shortcuts import redirect, render
from django.urls.base import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import *
from django.contrib.auth.views import *
from django.urls import reverse_lazy, reverse
from django.contrib.auth.models import User
from myapp.forms import *
from .forms import *

# Create your views here.
    

class Password_Change_View(PasswordChangeView):
    form_class =  UpdatePasswordForm
    success_url = reverse_lazy('toothery:index') 
    

def register(request):
    if request.method == 'POST':
        form1 = Book_Patient_Form(request.POST)
        form2 = CreateUserForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            user = form2.save()
            user.save()
            patient = form1.save(commit=False)
            patient.user = user
            patient.save()
            return redirect('login')
    else:
        form1 = Book_Patient_Form(data=request.POST)
        form2 = CreateUserForm(data=request.POST)
    return render(request, 'registration/register.html', {'form1': form1, 'form2': form2})


def update_user(request, pk):
    patient = Patient.objects.get(id = pk)
    user = User.objects.get(id = patient.user_id)
    if request.method == 'POST':
        form1 = Book_Patient_Form(request.POST, instance=patient)
        form2 = UpdateUserForm(request.POST, instance = user)
        if form1.is_valid() and form2.is_valid():
            user1 = form2.save()
            user1.save()
            patient1 = form1.save(commit=False)
            patient1.user = user1
            patient1.save()
            return redirect('toothery:display_user', pk = pk)
    else:
        form1 = Book_Patient_Form(instance=patient)
        form2 = UpdateUserForm(instance = user)
    return render(request, 'user/update_user_info.html', {'form1': form1, 'form2': form2,  'pk': patient.id, 'pk2': user.id})
   
class Delete_User_View(DeleteView):
    model = User
    template_name = 'user/delete_user.html'
    success_url = reverse_lazy('toothery:index')

    def get_context_data(self,*args, **kwargs):
        context = super(Delete_User_View, self).get_context_data(*args,**kwargs)
        user = User.objects.get(id = self.request.user.id)
        patient = Patient.objects.get(user_id = user.id)
        context = {'pk': patient.id, 'pk2': user.id, 'object': self.get_object()}
        return context