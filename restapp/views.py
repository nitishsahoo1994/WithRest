from django.shortcuts import render
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.generic.base import View
from restapp.models import Employee
from restapp.serializers import EmployeeSerializer
from django.http import HttpResponse


class EmployeeCRUDCBV(View):
    def get(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id',None)
        if id is not None:
            emp=Employee.objects.get(id=id)
            eserializer=EmployeeSerializer(emp)
            json_data=JSONRenderer().render(eserializer.data)
            return HttpResponse(json_data,content_type='application/json')
        qs=Employee.objects.all()
        eserializer = EmployeeSerializer(qs,many=True)
        json_data = JSONRenderer().render(eserializer.data)
        return HttpResponse(json_data, content_type='application/json')



