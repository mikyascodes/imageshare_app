window.onload = function () {
  // Hide the forms initially
  var updateForms = document.getElementsByClassName("updateform");
  var uploadForms = document.getElementsByClassName("uploadform");

  for (var i = 0; i < updateForms.length; i++) {
    updateForms[i].style.display = "none";
  }

  for (var i = 0; i < uploadForms.length; i++) {
    uploadForms[i].style.display = "none";
  }
};

function toggleForm() {
  var myForm = document.getElementsByClassName("updateform")[0];
  var displaySetting = myForm.style.display;
  myForm.style.display = displaySetting === "block" ? "none" : "block";
}

function toggleUploadForm() {
  var myForm = document.getElementsByClassName("uploadform")[0];
  var displaySetting = myForm.style.display;
  myForm.style.display = displaySetting === "block" ? "none" : "block";
}

//javascript for close button on django message
document.querySelectorAll(".close").forEach(function (button) {
  button.addEventListener("click", function () {
    this.closest(".alert").remove();
  });
});

//javascript to fix navabar when scrolling
var navbar = document.querySelector(".navbar");
// Add a scroll event listener
window.addEventListener("scroll", function () {
  // If the user has scrolled more than 100 pixels, fix the navbar to the top of the page
  if (window.scrollY > 100) {
    navbar.classList.add("fixed-top");
  } else {
    // Otherwise, remove the fixed-top class
    navbar.classList.remove("fixed-top");
  }
});
