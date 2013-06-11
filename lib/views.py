from django.http import HttpResponse
from django.shortcuts import render
from django.core import serializers
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
import json

class RestView(View):

    def dispatch(self, request, *args, **kwargs):
        
        # set accept variable from http accept header
        if 'application/json' in request.META['HTTP_ACCEPT'].split(','):
            self.accept = 'json'
        else:
            self.accept = 'html'        

        # call method determined by http proverb
        if 'pk' in kwargs:
            if request.method == 'GET':
                return self.get_item(request, *args, **kwargs)
            elif request.method == 'POST':
                return self.post_item(request, *args, **kwargs)
            elif request.method == 'PUT':
                return self.put_item(request, *args, **kwargs)
            elif request.method == 'DELETE':
                return self.delete_item(request, *args, **kwargs)
        else:
            if request.method == 'GET':
                return self.get_items(request, *args, **kwargs)
            elif request.method == 'POST':
                return self.post_items(request, *args, **kwargs)
            elif request.method == 'PUT':
                return self.put_items(request, *args, **kwargs)
            elif request.method == 'DELETE':
                return self.delete_items(request, *args, **kwargs)

    def render(self, request, template, response):
        if self.accept == 'json':
            jsonObject = {}
            for key in response:
                element = response[key]

                if isinstance(element, models.query.QuerySet):
                    jsonObject[key] = []
                    obj = serializers.serialize("python", element)
                    for e in obj:
                        d = e['fields']
                        d['pk'] = e['pk']
                        jsonObject[key].append(d)
                elif isinstance(element, models.Model):
                    d = serializers.serialize("python", [element])[0]
                    jsonObject[key] =  d['fields']
                    jsonObject[key]['pk'] =  d['pk']
                else:
                    jsonObject[key] = element

            return self.jsonResponse(jsonObject)
        else:
            return render(request, template, response)

    def jsonResponse(self, jsonObject):
        return HttpResponse(json.dumps(jsonObject, cls=DjangoJSONEncoder), content_type="application/json")
        
    def post_item(request):
        return HttpResponse(status=501)

    def put_item(request):
        return HttpResponse(status=501)

    def delete_item(request):
        return HttpResponse(status=501)

    def get_items(request):
        return HttpResponse(status=501)

    def post_items(request):
        return HttpResponse(status=501)

    def put_items(request):
        return HttpResponse(status=501)

    def delete_items(request):
        return HttpResponse(status=501)