from django.contrib.auth import authenticate, login
from django.views.generic.edit import FormView
from patient.forms import PatientRegistrationForm
from django.shortcuts import redirect


class PatientRegistration(FormView):

    template_name = 'patient_registration.html'
    form_class = PatientRegistrationForm
    success_url='/'
        
    def form_valid(self, form):

        form.save()
        username = self.request.POST['username']
        password = self.request.POST['password1']
        user = authenticate(username=username, password=password)
        login(self.request, user)

        return redirect(self.success_url)