	$('.multiple-items').slick({
  		infinite: true,
  		slidesToShow: 3,
  		slidesToScroll: 1,
		arrows: false,
		autoplay: true,
  		autoplaySpeed: 2000,
		dots:false,
		centerMode: true,
  		centerPadding: '60px',
		responsive: [{
      	breakpoint: 1024,
      	settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: false,
      }
    },
    {
      breakpoint: 600,
      settings: {
        slidesToShow: 2,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }]
	});
