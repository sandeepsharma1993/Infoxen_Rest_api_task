from django.shortcuts import render
from django.views.generic import View
from infoxenapiapp.models import OxygenCylinder
from django.http import HttpResponse,JsonResponse
import json
from django.core.serializers import serialize
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class OxyView(View):

    def post(self,request,**kwargs):

        if request.method=='POST':
            data=json.loads(request.body)
            address = data.get('Address')
            business_Name = data.get('Business_Name')
            person_Name = data.get('Person_Name')
            contact = data.get('Contact')


            verified_Status = data.get('Verified_Status')

            try:
                oxy = OxygenCylinder.objects.create(Address=address,Business_Name=business_Name,Person_Name=person_Name,Contact=contact,Verified_Status=verified_Status)
                return JsonResponse({'response':"Your Rources of leads for oxygen cylinders in Delhi has been created"})
            except:
                return JsonResponse({'error':'Please Provide Correct Details'},status=400)


    def get(self,request,**kwargs):

        qs = OxygenCylinder.objects.all().order_by('-id')
        json_data=serialize('json',qs)
        final_list=[]
        pdict=json.loads(json_data)
        for obj in pdict:
            final_list.append(obj['fields'])
        json_data=json.dumps(final_list)

        return JsonResponse(json_data,content_type='application/json',safe=False)
