/*
	Author: BestPixels
	Template: Booki - Responsive HTML Book Landing Page
	Version: 1.0
*/
;(function($){
	'use strict';
	
	//Global Variables
	var $body = $('body');
	$body.append('<div class="demo-panel"><div class="demo-toggle"><a href="javascript:void(0)"><i class="icofont icofont-gears"></a></i></div><div class="demo-content"><ul class="color-list"><li><a href="#" class="color-trigger color-green" title="color"></a></li><li><a href="#" class="color-trigger color-blue" title="color-blue"></a></li><li><a href="#" class="color-trigger color-orange" title="color-orange"></a></li><li><a href="#" class="color-trigger color-Yellow" title="color-yellow"></a></li><li><a href="#" class="color-trigger color-purple" title="color-purple"></a></li><li><a href="#" class="color-trigger color-pink" title="color-pink"></a></li></ul></div></div>');
	
	$('.demo-toggle').click(function() {
	  $('.demo-content').toggle('slow');
	});
	
	var $color_trigger = $('.color-trigger');
	if ($color_trigger.length > 0 ) {
		$color_trigger.on("click",function() {
			var $self = $(this);
			var $color_value = $self.attr("title");
			$("#colorcss").attr("href", "css/" + $color_value + ".css");
			$("#mockupimage").attr("src", "images/" + $color_value + ".png");
			return false;
		});
	}
	
})(jQuery);