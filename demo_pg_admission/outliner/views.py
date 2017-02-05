from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response 
from rest_framework.renderers import TemplateHTMLRenderer

from .models import Entry

from .serializers import EntrySerializer


# Create your views here.

@api_view(['GET', 'POST'])
def entryListAPI(request):
	if request.method == 'GET':
		entries = Entry.objects.all()
		entriesSerializer = EntrySerializer(entries, many=True)
		return Response(entriesSerializer.data)

	elif request.method == 'POST':
		serializer = EntrySerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		




@api_view(['GET', 'PUT', 'DELETE'])
def entryDetailAPI(request, id):
	try:
		entry = Entry.objects.get(pk=id)
	except Entry.DoesNotExist:	
		return Response(status=status.HTTP_404_NOT_FOUND)

	if request.method == 'GET':
		serializer = EntrySerializer(entry)
		return Response(serializer.data)	

	elif request.method == 'PUT':
		serializer = EntrySerializer(entry, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	elif request.method == 'DELETE':
		entry.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
			


@api_view(['GET', 'POST'])
def entryList(request):
	
	# renderer_classes = [TemplateHTMLRenderer]
	
	if request.method == 'GET':
		entries = Entry.objects.all().filter(parent=None, deleted=False)
		entriesSerializer = EntrySerializer(entries, many=True)
		context = {
					'entry'   :{
								'heading' : 'Welcome to Outliner.',
								'text'    : 'Click on one of your entries below to get started or add a new one.'					
					},
					'isNotStartingPage' : False,
					'entries' : entriesSerializer.data
					}
		return Response(context, template_name='outliner/outliner.html')

	elif request.method == 'POST':
		serializer = EntrySerializer(data=request.data)
		if serializer.is_valid():
			print(repr(serializer))
			serializer.save()
			return Response(serializer.data, template_name='outliner/done.html')
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)		

	return render(request, 'outliner/outliner.html')

@api_view(['GET', 'POST', 'DELETE'])
def entryDetail(request, id):
	try:
		entry = Entry.objects.get(pk=id, deleted=False)
		children = entry.entry_set.all().exclude(deleted=True)
	except Entry.DoesNotExist:	
		return Response({'error' : 'Sorry.The entry does not exist or has been deleted.'}, template_name='outliner/done.html')	

	print("method is %s" % request.method)	
	if request.method == 'GET':
		serializer = EntrySerializer(entry)
		context = {
					'isNotStartingPage' : True,
					'entry' : serializer.data,
					'entries' : children
		}
		return Response(context, template_name='outliner/outliner.html')	

	elif request.method == 'POST':
		print('post called ')
		print(request.data)


		serializer = EntrySerializer(entry, data=request.data)
		if serializer.is_valid():
			print(repr(serializer))
			print(serializer.validated_data.get('deleted'))
			
			#soft delete
			#when user clicks Delete button, the entry is submitted in the form with "_deleted" appended to its heading
			if "_deleted" in request.data.get('heading'):
				serializer.validated_data['deleted']=True
				print("going to delete")
			serializer.save()
			return Response({'id' : entry.id}, template_name='outliner/done.html')	
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
		
	elif request.method == 'DELETE':
		entry.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
			
	else:
		print(request.method)

def showEntry(request, pk):
	return render(request, 'outliner/outliner.html')