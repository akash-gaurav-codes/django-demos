from django.shortcuts import render
from django.http import HttpResponse

from .models import User, ExtraCurricularActivity

# Create your views here.
def index(request):
	return HttpResponse("Sahi hai bhai !")

def editProfile(request, userID):
	return render(request, "userProfile/editProfile.html")

def save(request, userID):
	
	user = User.objects.create(
				name    = request.POST['name'],
				gender  = request.POST['gender'], 
				mobile  = request.POST['mobile'], 
				age     = request.POST['age'], 
				address = request.POST['address'], 
				email   = request.POST['email'],
				boardX = request.POST['XthBoard'],
				streamX = request.POST['XthStream'],
				marksX = request.POST['XthMarks'],
				yearX = request.POST['XthYear'],
				boardXII = request.POST['XIIthBoard'],
				streamXII = request.POST['XIIthStream'],
				marksXII = request.POST['XIIthMarks'],
				yearXII = request.POST['XIIthYear'],
				college = request.POST['College'],
				course = request.POST['Course'],
				cgpa = request.POST['CGPA'],
				gradYear = request.POST['GradYear']
	)
					
	i=1
	while (request.POST.__contains__('activity'+str(i))):
		eca = ExtraCurricularActivity.objects.create(
			user = user,
			activityName = request.POST['activity'+str(i)],
			year = request.POST['yearActivity'+str(i)],
			participationOrAward = request.POST['resultActivity'+str(i)]
		)
		i = i+1
	


 		
	return HttpResponse("Thank you. Your form has been submitted")