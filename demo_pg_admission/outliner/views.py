from django.shortcuts import render


# Create your views here.
def showEntry(request, pk):
	return render(request, 'outliner/outliner.html')