jQuery(function($){
  $('a[href*="#"]').on('click.smoothscroll', function( e ){
  var hash= this.hash, _hash   = hash.replace(/#/,''), theHref = $(this).attr('href').replace(/#.*/, '');
  if( theHref && location.href.replace(/#.*/,'') != theHref ) return;
  var $target = _hash === '' ? $('body') : $( hash + ', a[name="'+ _hash +'"]').first();
  if( ! $target.length ) return;
  e.preventDefault();
  $('html, body').stop().animate({ scrollTop: $target.offset().top - 0 }, 1000, 'swing', function(){
  window.location.hash = hash;
        });
    });
});

$(document).ready(function() {
	$('form').on('submit', function(event) {
		$.ajax({
			data : {
				name : $('#email').val(),
        email : $('#name').val(),
        age : $('#age').val(),
        height : $('#height').val(),
        weight : $('#weight').val()
			},
			type : 'POST',
			url : '/app'
		})
		.done(function(data) {
			if (data.error) {
				$('#errorAlert').text(data.error).show();
        $('#successAlert').hide();
			}
			else {
				$('#successAlert').text(data.name).show();
        $('#errorAlert').hide();
			}
		});
		event.preventDefault();
	});
});

$(function() {
  $("#btn_form").click(function() {
    $(".form").css("display", "none");

    // $("#p-caption-hide").css("display", "none");

  });

  // $("#p-caption-display").click(function() {
  //   $(".hidden-area").css("display", "block");

  //   $("#p-caption-hide").css("display", "block");
  // });
});