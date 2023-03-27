$(document).ready(function() {
	// Get the products from the API
	$.ajax({
		url: 'https://example.com/api/products'
	}).done(function (products) {
		// Loop through the products and add them to the page
		products.forEach(function (product) {
			// Create the HTML for the product
			let productHTML = `
				<div class="col-md-4">
					<div class="card">
						<img class="card-img-top" src="${product.image}" alt="${product.name}">
						<div class="card-body">
							<h5 class="card-title">${product.name}</h5>
							<a href="${product.url}" class="btn btn-primary">Buy Now</a>
						</div>
					</div>
				</div>
			`;
			$('#products .row').append(productHTML);
		});
	});
});


// JavaScript for "Online Store - Products"

$(document).ready(function(){
    // Toggle navigation links on small screens
    $(".navbar-toggler").click(function(){
      $(".navbar-collapse").slideToggle();
    });
    
    // Show/hide "Back to Top" button
    $(window).scroll(function(){
      if($(window).scrollTop() > 100){
        $("#btn-top").fadeIn();
      } else {
        $("#btn-top").fadeOut();
      }
    });
    
    // Scroll to top when "Back to Top" button is clicked
    $("#btn-top").click(function(){
      $("html, body").animate({scrollTop: 0}, 1000);
    });
  });