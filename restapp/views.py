from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.generic.base import View
from restapp.models import Employee
from restapp.serializers import EmployeeSerializer
from django.http import HttpResponse


@method_decorator(csrf_exempt, name='dispatch')
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

    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        serializer=EmployeeSerializer(data=pdata)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource Created Successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json',status=404)

    def put(self,request,*args,**kwargs):
        json_body=request.body
        stream=io.BytesIO(json_body)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp=Employee.objects.get(id=id)
        serializer=EmployeeSerializer(emp,data=pdata,partial=True)
        if serializer.is_valid():
            serializer.save()
            msg={'msg':'Resource updated successfully'}
            json_data=JSONRenderer().render(msg)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json',status=400)



    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        pdata=JSONParser().parse(stream)
        id=pdata.get('id')
        emp=Employee.objects.get(id=id)
        emp.delete()
        msg={'msg':'Resource deleted Successfully'}
        json_data=JSONRenderer().render(msg)
        return HttpResponse(json_data,content_type='application/json')




