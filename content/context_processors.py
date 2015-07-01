from content.models import *
import logging

def accommodation( request ):

	room_types = ''
	try:
		room_types = RoomType.objects.all();
	except Exception, e:
		logging.error( 'problem getting accommodation type through context processor' )

	return {
		'room_types': room_types,
	}

def resort_detail( request ):
	resort_detail = ''
	try:
		resort_detail = ResortInfo.objects.get( pk = 1 )
	except Exception, e:
		logging.error( 'problem getting resort_detail through context processor' )

	return {
		'resort_detail': resort_detail
	}