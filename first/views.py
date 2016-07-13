from django.shortcuts import render
from .models import Sub


def sub_list(request):
	subs = Sub.objects.order_by('name')
	return render(request, 'first/sub_list.html', {'subs':subs})

# Create your views here.
