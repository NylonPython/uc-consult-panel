from django.shortcuts import get_object_or_404, render, render_to_response
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.contrib.auth import authenticate, login
from .models import Post, Location, Computer, Printer
# Create your views here.

class IndexView(generic.ListView):
    template_name = 'blog/post_list.html'
    context_object_name = 'recent_blog_posts'
    queryset = Post.objects.all()
class LocationsView(generic.ListView):
    template_name = 'blog/location_list.html'
    context_object_name = 'locations'
    queryset = Location.objects.all()
#class ResourcesView(generic.ListView):
#    template_name = 'blog/resource_list.html'
#    context_object_name = 'locations'
#    queryset = Location.objects.all()

def ResourcesView(request):
    locations = Location.objects.all().prefetch_related('lab_printers')
    return render_to_response('blog/resource_list.html',
            {'locations': locations})

def login_view(request):
	context = {}
	return render(request, 'blog/login.html', context)

def login(request):
	username = request.GET['username']
	password = request.GET['password']
	user = authenticate(username = username, password = password)
	if user is not None:
		if user.is_active:
			login(request, user)
			error_message = 'You have been logged in!'
			context = {
				'error_message': error_message,
			}
			return render(request, 'blog/login_success.html', context)
		else:
			error_message = 'You\'re not active!'
			context = {

				'error_message': error_message

			}
			return render(request, 'blog/login.html', context)

	else:
		error_message = 'Invalid login'
		context = {
			'error_message': error_message
		}
		return render(request, 'blog/login.html', context)

