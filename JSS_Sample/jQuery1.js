$('h1').click(function(){
  console.log('There was a click!')
  $(this).text("I was changed!")
})

$('input').eq(0).keypress(function(event){
  // console.log(event);
  // $('h3').toggleClass('turnBlue');
  if (event.which === 13) {
    $('h3').toggleClass('turnBlue');
  }
})

// on()

$('h1').on('dblclick',function() {
  $(this).toggleClass('turnRed');
})

$('h1').on('mouseenter',function() {
  $(this).toggleClass('turnBlue');
})

$('input').eq(1).on('click',function(){
  $('.container').slideUp(3000);
})
