from django.shortcuts import render

# Create your views here.
def showPages(request):
	return render(request, 'welcomeApp/welcome.html')