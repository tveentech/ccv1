from django.db import models
from django.db.models import signals
from django.conf import settings
from content.helper import send_email_mandrill

def send_mail_admin( sender, instance, created, **kwargs ):

	if isinstance( instance, Enquiry ):
		email_subject = "CoffeeCastle Enquiry Request"
		email_body = "This person wants to contact you.<br>\
					Name : %s<br>\
					Phone No: %s<br>\
					Email ID:%s<br>\
					Message:%s<br>" %(
						instance.name,
						instance.phone,
						instance.email,
						instance.message
					)
		from_name = instance.name
		from_email = settings.DEFAULT_FROM_EMAIL
		recipients = settings.ADMINS

	elif isinstance( instance, Booking ):
		email_subject = "CoffeeCastle Booking Request"
		email_body = "Reservation from %s to %s.<br>Name:%s,<br>\
					Phone No:%s,<br>Message:%s<br>"	%(
						instance.checkin,
						instance.checkout,
						instance.name,
						instance.phone,
						instance.message
					)
		from_name = instance.name
		from_email = settings.DEFAULT_FROM_EMAIL
		recipients = settings.ADMINS

	send_email_mandrill(
		email_subject,
		email_body,
		from_name,
		from_email,
		recipients,
	)


class Testimonial( models.Model ):
	name = models.CharField( max_length = 255, blank = False )
	room_type = models.CharField ( max_length = 255 )
	message = models.TextField ( blank = False )

	def __unicode__( self ):
		return u'%s' % ( self.name )

class ResortInfo( models.Model ):
	name = models.CharField( max_length = 255, blank = False )
	phone = models.CharField( max_length = 255, blank = False, help_text = 'Phone Number to be displayed on the webiste' )
	email = models.CharField( max_length = 255, blank = False )
	address = models.TextField ( blank = False )
	directions = models.TextField ( blank = False, help_text = 'Direction to the resort from major locations nearyby' )

	def __unicode__( self ):
		return u'%s' % ( self.name )

class RoomType( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	description = models.TextField( blank = False )
	poster = models.TextField( blank = True, help_text = 'Url of the poster to be displayed seperated by pressing enter' )
	room_rate = models.CharField( max_length = 255 , blank = True )
	bed_type = models.CharField( max_length = 255 , blank = True )
	no_of_persons = models.IntegerField( default = 2, blank = True )
	size_of_room = models.CharField( max_length = 255 , blank = True )
	view = models.CharField( max_length = 255 , blank = True )
	ensuite_bathroom = models.CharField( max_length = 255 , blank = True )
	free_internet = models.CharField( max_length = 255 , blank = True )
	breakfast_included = models.CharField( max_length = 255 , blank = True )
	gym_access = models.CharField( max_length = 255 , blank = True )
	pickup_drop = models.CharField( max_length = 255 , blank = True )
	room_service = models.CharField( max_length = 255 , blank = True )
	created_at = models.DateTimeField( auto_now_add = True )

	def __unicode__( self ):
		return u'%s' % ( self.title )

	def get_poster_list( self ):
		posters = []

		if self.poster:
			posters = self.poster.split()

		return posters

class Booking( models.Model ):
	name = models.CharField( max_length = 255, blank = False )
	phone = models.CharField( max_length = 255, blank = False )
	email = models.EmailField( max_length = 255, blank = False )
	checkin = models.DateField( blank = False )
	checkout = models.DateField( blank = False )
	message = models.TextField( blank = True )
	created_at = models.DateTimeField( auto_now_add = True )
	is_confirmed = models.BooleanField( default = False )

	def __unicode__( self ):
		return u'%s' % ( self.name )

class Enquiry( models.Model ):
	name = models.CharField( max_length = 255, blank = False )
	phone = models.CharField( max_length = 255, blank = False )
	email = models.EmailField( max_length = 255, blank = False )
	message = models.TextField( blank = False )
	created_at = models.DateTimeField( auto_now_add = True )

	class Meta:
		verbose_name_plural = "Enquiries"

	def __unicode__( self ):
		return u'%s' % ( self.name )

class Activity( models.Model ):
	title = models.CharField( max_length = 255, blank = False )
	description = models.TextField( blank = False )
	poster = models.TextField( blank = False, help_text = 'one url of the poster to be displayed in the activity section' )

	class Meta:
		verbose_name_plural = "Activities"

	def __unicode__( self ):
		return u'%s' % ( self.title )

	def get_posters( self ):
		posters = []

		if self.poster:
			posters = self.poster.split()

		return posters

# signals.post_save.connect( send_mail_admin, sender = Booking )
# signals.post_save.connect( send_mail_admin, sender = Enquiry )