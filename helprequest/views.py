from django.forms.models import fields_for_model
from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, UpdateView, CreateView, FormView
from django.views.generic.base import TemplateView

from helprequest.models import HelpRequest

from helprequest.forms import HelpRequestForm



@method_decorator(login_required, name='dispatch')
class HelpRequestList(ListView):

	model = HelpRequest
	template_name = "help_request_list.html"
	context_object_name = "help_requests"
	paginate_by = 20
	order_by="category"
	
	
	"""def get_queryset(self):
		
		key = self.request.GET.get('key', None)
		if  key!= None:
			object_list = self.model.objects.filter(name__icontains = key)
		else:
			object_list = self.model.objects.order_by(self.order_by)
		
		return object_list
    """


@method_decorator(login_required, name='dispatch')
class HelpRequestDetail(DetailView):

    model = HelpRequest
    template_name = "help_request_detail.html"
    context_object_name = "help_request"


@method_decorator(login_required, name='dispatch')
class RequestHelp(FormView):
    """
    TODO: on save of the help request, link the user requesting help to the patient fild of the help request
    """
    template_name = 'help_request.html'
    form_class = HelpRequestForm
    success_url = 'status'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)


@method_decorator(login_required, name='dispatch')
class HelpRequestStatus(TemplateView):
    """
    TODO: 
        - should show the status of the help request. The frontend will be refreshing every 5 seconds
        - next, we can have the backend to send a signal to the frontend when the help request status changes 
    """
    template_name = 'help_request_status.html'
    
    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        # form.send_email()
        return super().form_valid(form)

