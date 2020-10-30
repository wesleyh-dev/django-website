$(document).ready(function(){
  // Add smooth scrolling to all links
  $("a").on('click', function(event) {

    // Make sure this.hash has a value before overriding default behavior
    if (this.hash !== "") {
      // Prevent default anchor click behavior
      event.preventDefault();

      // Store hash
      var hash = this.hash;

      // Using jQuery's animate() method to add smooth page scroll
      // The optional number (800) specifies the number of milliseconds it takes to scroll to the specified area
      var position = $(hash).offset().top - 60;
      $('html, body').animate({
        scrollTop: position
      }, 800, function(){
    
        // Add hash (#) to URL when done scrolling (default click behavior)
        // NO, this will mess up the location I want to scroll to when you click a nav link
      });
    } // End if

  });
});

$(window).scroll(function() {
  var scroll = $(window).scrollTop();

  if (scroll >= 10) {
    $(".navbar").addClass("top-nav-collapse");
  } else {
    $(".navbar").removeClass("top-nav-collapse");
  }
});

// Data Picker Initialization
$('.datepicker').datepicker({
  format: 'mmmm, yyyy'
});

// init Masonry
var $grid = $('.grid').masonry({
  itemSelector: '.grid-item',
  percentPosition: true,
  columnWidth: '.grid-sizer'
});

// layout Masonry after each image loads
$grid.imagesLoaded().progress( function() {
  $grid.masonry();
});

