from django.contrib.auth import authenticate, login
from medic.forms import MedicRegistrationForm
from django.shortcuts import redirect
from django.views.generic import FormView

class MedicRegistration(FormView):

    template_name = 'medic_registration.html'
    form_class = MedicRegistrationForm
    success_url='/'
    
    def form_valid(self, form):

        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return redirect(self.success_url)