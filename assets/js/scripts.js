// Set Variables
var mobile_toggle = 'closed';

$(document).ready(function() {

	"use strict";

	// Main Menu Drop Down
	$('ul#navigation').superfish({
        delay:       600,
        animation:   {opacity:'show',height:'show'},
        speed:       'fast',
        autoArrows:  true,
        dropShadows: false
    });

	// Language Drop Down
	$('ul#language-selection').superfish({
        delay:       600,
        animation:   {opacity:'show',height:'show'},
        speed:       'fast',
        autoArrows:  true,
        dropShadows: false
    });

	// Accordion
	$( ".accordion" ).accordion( { autoHeight: false } );

	// Toggle
	$( ".toggle > .inner" ).hide();
	$(".toggle .title").bind('click',function() {
		$(this).toggleClass('active');
		if ($(this).hasClass('active')) {
			$(this).closest('.toggle').find('.inner').slideDown(200, 'easeOutCirc');
		} else {
			$(this).closest('.toggle').find('.inner').slideUp(200, 'easeOutCirc');
		}
	});

	// Tabs
	$(function() {
		$( "#tabs" ).tabs();
	});

	// PrettyPhoto
	$("a[rel^='prettyPhoto']").prettyPhoto({social_tools:false});

	// Search Button Toggle
	$(".menu-search-button").click(function() {
		$(".menu-search-field").toggleClass("menu-search-focus", 200);
	});

	// Price Breakdown Toggle
	$(".price-breakdown").click(function() {
		$(".price-details .price-breakdown").toggleClass("price-breakdown-open", 200);
		$(".price-details .price-breakdown-display").toggleClass("price-breakdown-display-open", 200);
		return false;
	});

	// Mobile Menu
	$(".mobile-menu-button").click(function(){
		$(".mobile-menu-inner").stop().slideToggle(350);
		return false;
	});

	// Calendar Message
	$(".datepicker2").click(function(e){
        $(".ui-datepicker-calendar").effect("pulsate", { times:1 }, 900);
		$(".calendar-notice").fadeIn(1200, function() {
			// Animation complete
		});
		e.stopPropagation();
    });

	// Header Google Map
	$(".gmap-button").click(function(){
		$('#header-gmap').slideToggle(900);
		if (!map) {
			initialize(12.296472,75.727932);

		}
		$('.gmap-button').toggleClass('gmap-button-hover');
	});

});

$(window).load(function(){

	"use strict";

	// Main Slider
	$('.slider').flexslider({
		animation: "fade",
		controlNav: false,
		directionNav: true,
		slideshow: false,
		start: function(slider){
			$('body').removeClass('loading');
		}
	});

	// Text Slider
	$('.text-slider').flexslider({
		animation: "fade",
		controlNav: false,
		directionNav: true,
		slideshow: true,
		start: function(slider){
			$('body').removeClass('loading');
		}
	});

});

$(function() {

	"use strict";

	// Datepicker
	$(".datepicker").datepicker();

	// Make Datepicker Fields Read Only
	$("#open_date_from").attr('readonly', true);
	$("#open_date_to").attr('readonly', true);

	// Booking page open datepicker
	$("#open_datepicker").datepicker({
		numberOfMonths: 2,
		minDate: 0,
		beforeShowDay: function(date) {
			var date1 = $.datepicker.parseDate($.datepicker._defaults.dateFormat, $("#open_date_from").val());
			var date2 = $.datepicker.parseDate($.datepicker._defaults.dateFormat, $("#open_date_to").val());
			return [true, date1 && ((date.getTime() == date1.getTime()) || (date2 && date >= date1 && date <= date2)) ? "dp-highlight" : ""];
		},
		onSelect: function(dateText, inst) {
			var date1 = $.datepicker.parseDate($.datepicker._defaults.dateFormat, $("#open_date_from").val());
			var date2 = $.datepicker.parseDate($.datepicker._defaults.dateFormat, $("#open_date_to").val());
			if (!date1 || date2) {
				$("#open_date_from").val(dateText);
				$("#open_date_to").val("");
			} else {
				if(Date.parse(dateText) < Date.parse(date1)){
					$("#open_date_from").val(dateText);
					$("#open_date_to").val("");
				}
				else {
					$("#open_date_to").val(dateText);
				}
			}
		}
	});

});

// Add/Remove Rooms For Booking Form
$(document).ready(function() {

	"use strict";

	var i = '';

	$('.rooms-wrapper div[class^="room-"]:not(div.room-0)').hide();
	$('#book_room').change(function(e) {
		$('.rooms-wrapper div[class^="room-"]').hide();
		e.preventDefault();
		var selectedVal = $(this).val();

		if(selectedVal > 1) {
			for(i = 1; i <= selectedVal; i++ ) {
				$('div[class^=room-'+ i +']').show();
			}
		}
		else {
			$('div.room-0').show();
		}
	});

});
