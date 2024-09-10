let slidePosition = 0;
const slides = document.getElementsByClassName('box');
const totalSlides = slides.length;

document.getElementById('slide-right').addEventListener("click", function() {
    moveToNextSlide();
  });
document.getElementById('slide-left').addEventListener("click", function() {
    moveToPrevSlide();
  });

document.getElementById('home').addEventListener("mouseover", function() {
  gotoPos(0);
  });
document.getElementById('Qualifications').addEventListener("mouseover", function() {
  gotoPos(1);
  });
document.getElementById('Portfolio').addEventListener("mouseover", function() {
  gotoPos(2);
  });
document.getElementById('Services').addEventListener("mouseover", function() {
  gotoPos(3);
  });
document.getElementById('AIPage').addEventListener("mouseover", function() {
  gotoPos(4);
  });

function gotoPos(pos) {
  while (slidePosition != pos) {
    moveToNextSlide();
  }
}

function updateSlidePosition() {
  for (let slide of slides) {
    slide.classList.remove('box--visible');
    slide.classList.add('box--hidden');
  }

  slides[slidePosition].classList.add('box--visible');
}

function moveToNextSlide() {
  if (slidePosition === totalSlides - 1) {
    slidePosition = 0;
  } else {
    slidePosition++;
  }

  updateSlidePosition();
}

function moveToPrevSlide() {
  if (slidePosition === 0) {
    slidePosition = totalSlides - 1;
  } else {
    slidePosition--;
  }



  updateSlidePosition();
}