
const navLinks = document.querySelectorAll(".nav-menu .nav-link")
const openMenuButton = document.querySelector("#menu-open-button")
const closeMenuButton = document.querySelector("#menu-close-button")

openMenuButton.addEventListener("click", () =>{
document.body.classList.toggle("show-mobile-menu");

})

closeMenuButton.addEventListener("click", () => openMenuButton.click());

// navlinks 
navLinks.forEach(link => {
  link.addEventListener("click", () => openMenuButton.click());
});


// Initialize Swiper
const swiper = new Swiper('.slider-wrapper', {
  loop: true,
  grabCursor: true,
  spaceBetween: 25,

  // If we need pagination
  pagination: {
    el: '.swiper-pagination',
    clickble: true,
    dynamicBullets: true,
  },

  // Navigation arrows
  navigation: {
    nextEl: '.swiper-button-next',
    prevEl: '.swiper-button-prev',
  },

  //Responsive breakpoints 
breakpoints: {
  0: {
  slidesPerView: 1
    },

     768: {
  slidesPerView: 2
    },

     1024: {
  slidesPerView: 3
    },
  }
});
