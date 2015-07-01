from django.http import HttpResponse
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from django.http import HttpResponse, HttpResponseRedirect, Http404
import json

from models import *

def index( request, template_name = 'index.html' ):

	testimonials = Testimonial.objects.all()

	result = {
		'testimonials': testimonials,
	}

	return render_to_response(
		template_name,
		result,
		context_instance = RequestContext( request ) )

def activities( request, template_name = 'activities.html' ):

	activities = Activity.objects.all()
	result = {
		'activities' : activities,
	}

	return render_to_response(
		template_name,
		result,
		context_instance = RequestContext( request ) )

def contact_us( request, template_name = 'contact_us.html' ):

	result = {
	}

	if request.method == 'POST':
		pass

	return render_to_response(
		template_name,
		result,
		context_instance = RequestContext( request ) )

def accommodation( request, accommodation_id, template_name = 'accommodation.html' ):

	room_detail = RoomType.objects.get( pk = accommodation_id );

	result = {
		'room_detail': room_detail,
	}

	return render_to_response(
		template_name,
		result,
		context_instance = RequestContext( request ) )

def availability( request ):

	response_data = False

	try:
		from content.forms import BookingForm
		availabilityform = BookingForm( request.POST )

		if availabilityform.is_valid():
			availabilityform.save()
			response_data = True

	except Exception, e:
		print e
		import logging
		logging.error( 'problem updating Availability Form' )

	return HttpResponse( json.dumps( response_data ), content_type = 'application/json' )

def contact_message( request ):

	response_data = False

	try:
		from content.forms import EnquiryForm
		enquiryform = EnquiryForm( request.POST )

		if enquiryform.is_valid():
			enquiryform.save()
			response_data = True
	except Exception, e:
		print e
		import logging
		logging.error( 'problem updating Contact Form' )

	return HttpResponse( json.dumps( response_data ), content_type = 'application/json' )