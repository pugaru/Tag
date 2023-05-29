function removeHash () { 
    history.pushState("", document.title, window.location.pathname
                                                       + window.location.search);
}


$(function() {
    var hash = window.location.hash;
    if(hash) {
      var slide = $('#modal').find(hash)
      if(slide[0]) {
        $('#modal').modal('show');
      } else {
        console.log('Wrong URL: Could not find slide with id ' + hash);
        removeHash()
      };
    } else {
      /* console.log('no hash') */
    }
});


$('#modal').on('show.bs.modal', function (event) {
    var modal = $(this);
  if(window.location.hash) {
    var slide = modal.find(window.location.hash);
  } else {
    var button = $(event.relatedTarget); // Button that triggered the modal
    var slide = modal.find(button.data('slide'));
  };
  var pk = slide.data('pk');
  document.location.hash = 'slide-' + pk;
  var title = slide.data('title');
  var description = slide.data('description');
  var imageUrl = slide.data('image');
  var fullImageUrl = slide.data('full-image');
  var detailUrl = slide.data('detail');
  var tags = slide.data('tags');
  var date = slide.data('date');
  var fb = slide.data('fb');
  var gplus = slide.data('gplus');
  ($('.photo-title')).text(title);
  ($('.photo-detail-link')).attr('href', detailUrl);
  ($('.photo-description')).text(description);
  ($('.photo-tags')).text(tags);
  ($('.photo-date')).text(date);
  ($('.edit-link')).attr('href', '/admin/blog/imagepost/' + pk + '/change/');
  ($('.facebook-share')).on('click', function(){window.open(fb,'popup','width=600,height=500'); return false;});
  ($('.facebook-share')).attr('href', fb);
  ($('.gplus-share')).attr('href', gplus);
  ($('.pinterest-share')).attr('data-pin-media', fullImageUrl);
  ($('.pinterest-share')).attr('data-pin-url', detailUrl);
  slide.addClass('active');
  slide.find('.carousel-image').attr('src', imageUrl);
  slide.find('.carousel-image').attr('alt', title);
});


$('#modal').on('hide.bs.modal', function (event) {
  var modal = $(this);
  modal.find('.carousel-item').each(function() {
  	$(this).removeClass('active');
  });
  removeHash()
});


$('#carouselControls').on('slide.bs.carousel', function (event) {
  var carousel = $(this);
  var relatedTarget = $(event.relatedTarget);
  var pk = relatedTarget.data('pk');
  document.location.hash = 'slide-' + pk;
  var title = relatedTarget.data('title');
  var description = relatedTarget.data('description');
  var imageUrl = relatedTarget.data('image');
  var fullImageUrl = relatedTarget.data('full-image');
  var detailUrl = relatedTarget.data('detail');
  var tags = relatedTarget.data('tags');
  var date = relatedTarget.data('date');
  var fb = relatedTarget.data('fb');
  var gplus = relatedTarget.data('gplus');  
  ($('.photo-title')).text(title);
  ($('.photo-detail-link')).attr('href', detailUrl);
  ($('.photo-description')).text(description);
  ($('.photo-tags')).text(tags);
  ($('.photo-date')).text(date);
  ($('.edit-link')).attr('href', '/admin/blog/photo/' + pk + '/change/');
  ($('.facebook-share')).on('click', function(){window.open(fb,'popup','width=600,height=500'); return false;});
  ($('.facebook-share')).attr('href', fb);
  ($('.gplus-share')).attr('href', gplus);
  ($('.pinterest-share')).attr('data-pin-url', detailUrl);
  ($('.pinterest-share')).attr('data-pin-media', fullImageUrl);
  var carouselImage = relatedTarget.find('.carousel-image');
  carouselImage.attr('src', imageUrl);
  carouselImage.attr('alt', title);
});



function toggleDarkMode() {
    var body = document.body;
    body.classList.toggle("dark-mode");
}
