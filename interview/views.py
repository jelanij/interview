from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
	if request.method =="POST":
		auth_header = request.META.get('HTTP_AUTHORIZATION','')
		token_type,_,credentials = auth_header.partition(' ')
		import base64
		expected = base64.b64encode(b'interview:question').decode()
		if token_type != 'Basic' or credentials != expected:
			return HttpResponse('Unauthorized',status=401)

		try:
			key = json.loads(request.body)
		except Exception as e:
			return JsonResponse({"status":False,"returned_data":f"Error: {e}.  Unable to parse request. Ensure payload is submitted correctly."},status =405)
		try:
			print("key: "+key['id'])
			if key['id'] =="GET CUSTOMERS":
				element = """{
	"customer": "Spectrum",
	"address": "123 street address",
	"city": "Brandon",
	"details":
		[
			{ "id": 1234567890, "color": "Red" },
			{ "id": 2423423434, "color": "Blue" },
			{ "id": 2131231234, "color": "Yellow" }
		]
}"""
				serialized = json.loads(element)
				return JsonResponse({"status":True,"returned_data":serialized},status =200)
			else:
				return JsonResponse({"status":False,"returned_data":None},status =400)
		except Exception as e:
			return JsonResponse({"status":False,"returned_data":"Error: " +str(e)},status=400)
	else:
		return render(request,'game.html')

@csrf_exempt
def get_data(request):
	if request.method =="GET":
		data = {"payload":[15500,5155,54454,54845,51558,14236,65892]}
		serialized = json.loads(data)
	return JsonResponse({"status":True,"serialized":serialized},status =200)
			

		