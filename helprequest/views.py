from django.utils.decorators import method_decorator
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, UpdateView, CreateView
from django.views.generic.base import TemplateView

from helprequest.models import HelpRequest
from patient.models import Patient

from helprequest.forms import HelpRequestForm


@method_decorator(login_required, name='dispatch')
class HelpRequestList(ListView):

    model = HelpRequest
    template_name = "help_request_list.html"
    context_object_name = "help_requests"
    paginate_by = 20
    order_by="category"


@method_decorator(login_required, name='dispatch')
class HelpRequestDetail(DetailView):

    model = HelpRequest
    template_name = "help_request_detail.html"
    context_object_name = "help_request"


@method_decorator(login_required, name='dispatch')
class RequestHelp(CreateView):
    """
    TODO: on save of the help request, link the user requesting help to the patient fild of the help request
    """

    template_name = 'help_request.html'
    form_class = HelpRequestForm
    success_url = 'status'

    def form_valid(self, form):
        form.instance.patient =  Patient.objects.get(id=self.request.user.id)
        form.save()

        return redirect(self.success_url)


@method_decorator(login_required, name='dispatch')
class HelpRequestStatus(TemplateView):
    """
    TODO: 
        - should show the status of the help request. The frontend will be refreshing every 5 seconds
        - next, we can have the backend to send a signal to the frontend when the help request status changes 
    """
    template_name = 'help_request_status.html'


@method_decorator(login_required, name='dispatch')
class HelpRequestUpdate(UpdateView):
    model = HelpRequest
    fields = ["medic_notes"]
    template_name = 'help_response.html'
    success_url = '/' 
