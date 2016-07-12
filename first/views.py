from django.shortcuts import render

def sub_list(request):
	return render(request, 'first/sub_list.html', {})

# Create your views here.
