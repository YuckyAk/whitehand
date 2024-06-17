var burgerMenu = document.getElementById('burger-menu');
var overlay = document.getElementById('menu');
burgerMenu.addEventListener('click',function(){
  this.classList.toggle("close");
  overlay.classList.toggle("overlay");
});

// Открытия модального окна
document.querySelector(".open_modal").addEventListener("click", function() {
  document.querySelector(".form-zvonok").style.display = "flex";
});

// Закрытие модального окна
document.querySelector(".close_modal").addEventListener("click", function() {
  document.querySelector(".form-zvonok").style.display = "none";
});




  $(window).load(function() {
    $('.flexslider').flexslider({
      animation: "slide"
    });
  });
oznokom = document.querySelector('.oznokom')
main = document.querySelector('.main')
if (oznokom == null){
main.style.backgroundImage="url()";
main.style.height = 'unset'
}

  $('.buy').click(function(){
    $('.bottom').addClass("clicked");
  });

  $('.remove').click(function(){
    $('.bottom').removeClass("clicked");
  });