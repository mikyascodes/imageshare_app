window.onload = function () {
  document.getElementById("upload_form").style.display = "none";
};

function toggleUploadForm() {
  var myUploadForm = document.getElementById("upload_form");
  var displaySetting = myUploadForm.style.display;
  if (displaySetting == "block") {
    myUploadForm.style.display = "none";
  } else {
    myUploadForm.style.display = "block";
  }
}
