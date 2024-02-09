//javascript to hide and show form on profile page
window.onload = function () {
  document.getElementById("update_form").style.display = "none";
};

function toggleForm() {
  var myForm = document.getElementById("update_form");
  var displaySetting = myForm.style.display;
  if (displaySetting == "block") {
    myForm.style.display = "none";
  } else {
    myForm.style.display = "block";
  }
}
//javascript for close button on django message
document.querySelectorAll('.close').forEach(function (button) {
  button.addEventListener('click', function () {
    this.closest('.alert').remove();
  });
});

//javascript to fix navabar when scrolling
var navbar = document.querySelector('.navbar');
// Add a scroll event listener
window.addEventListener('scroll', function () {
  // If the user has scrolled more than 100 pixels, fix the navbar to the top of the page
  if (window.scrollY > 100) {
    navbar.classList.add('fixed-top');
  } else {
    // Otherwise, remove the fixed-top class
    navbar.classList.remove('fixed-top');
  }
});

