from django.template import Context, Template, loader
from django.http import HttpResponse, Http404

from django.shortcuts import render_to_response
import settings

def serve_templates(request, document_root, path):
	return render_to_response(document_root + "/" + path)

def home(request):
	t = loader.get_template('base.html')
	return render_to_response(settings.ROOT_PATH + "/" + "templates/base.html")

def about(request):
	return HttpResponse(request, "about")
