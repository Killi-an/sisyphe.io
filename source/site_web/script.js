// Nav Sticky
  window.addEventListener('scroll', function() {
    var nav = document.getElementById('nav'); // Get the navigation element
    var scrollPosition = window.scrollY; // Get the current scroll position

    // Check if the scroll position is greater than a small amount
    if (scrollPosition > 50) { // Adjust the value according to your needs
      $(nav).addClass('sticky');
    } else {
      $(nav).removeClass('sticky');
    }
  });

// Small navbar animation
$(document).ready(function () {
    var isAnimating = false; // Variable to track animation state

    $(".cross").hide();
    $(".menu").hide();

    $(".hamburger").click(function () {
        if (!isAnimating) { // Check if animation is not already in progress
            isAnimating = true; // Set animation state to true
            $(".hamburger").hide();
            $(".cross").show();
            $(".menu").slideToggle("slow", function () {
                isAnimating = false; // Reset animation state to false when animation is finished
            });
        }
    });

    $(".cross").click(function () {
        if (!isAnimating) { // Check if animation is not already in progress
            isAnimating = true; // Set animation state to true
            $(".menu").slideToggle("slow", function () {
                $(".cross").hide();
                $(".hamburger").show();
                isAnimating = false; // Reset animation state to false when animation is finished
            });
        }
    });

    $(".small_menu").click(function () {
        if (!isAnimating) { // Check if animation is not already in progress
            isAnimating = true; // Set animation state to true
            $(".menu").slideToggle("slow", function () {
                $(".cross").hide();
                $(".hamburger").show();
                isAnimating = false; // Reset animation state to false when animation is finished
            });
        }
    });
});


// Scroll back to top button
var amountScrolled = 1000;

$(window).scroll(function() {
  if ($(window).scrollTop() > amountScrolled) {
    $('button.back-to-top').addClass('show');
  } else {
    $('button.back-to-top').removeClass('show');
  }
});

$(document).on('click', 'button.back-to-top', function() {
  $('html, body').scrollTop(0);
  return false;
});