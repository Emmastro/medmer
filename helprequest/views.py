from django.forms.models import fields_for_model

from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, UpdateView, CreateView, FormView

from django.views.generic.base import TemplateView

from helprequest.models import HelpRequest

from helprequest.forms import HelpRequestForm, HelpResponseForm

from django.shortcuts import redirect

from datetime import datetime

from medic.models import Medic

@method_decorator(login_required, name='dispatch')
class HelpRequestList(ListView):

    model = HelpRequest
    template_name = "help_request_list.html"
    context_object_name = "help_requests"
    paginate_by = 20
    order_by = "category"


@method_decorator(login_required, name='dispatch')
class HelpRequestDetail(DetailView):

    model = HelpRequest
    template_name = "help_request_detail.html"
    context_object_name = "help_request"

    def post(self, request, *args, **kwargs):
        request_id = request.POST.get("helprequestid")
        help_request = HelpRequest.objects.get(id=request_id)

        # Accept the request
        print(request.user.pk)
        help_request.medic = Medic.objects.get(id=request.user.pk)
        help_request.time_accepted = datetime.now()
        help_request.STATUS = "Accepted"
        print("Help request: ", help_request.medic, help_request.time_requested, help_request.time_accepted)
        print("kwargs:",  kwargs)
        HelpRequest.objects.filter(**kwargs)

        help_request.save()

        return redirect('help_response', request_id)


@method_decorator(login_required, name='dispatch')
class RequestHelp(FormView):
    """
    TODO: on save of the help request, link the user requesting help to the patient fild of the help request
    """
    template_name = 'help_request.html'
    form_class = HelpRequestForm
    success_url = 'status'


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

    def form_valid(self, form):

        form.save()

