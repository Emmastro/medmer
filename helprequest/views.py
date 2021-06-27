from django.utils.decorators import method_decorator

from django.contrib.auth.decorators import login_required

from django.views.generic import ListView, DetailView, UpdateView, CreateView

from helprequest.models import HelpRequest

from helprequest.forms import HelpRequestForm

from django.shortcuts import render, redirect

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
def gethelp(request):
    form_class = HelpRequestForm
    form  = form_class(request.POST or None)
    if request.method == 'POST':
        #form = MedicForm(request.POST, request.FILES)
        
        if form.is_valid():

             form.save()
             return redirect('home')
             
            
    context = {'form': form}
    return render(request, 'help_request.html', context)
