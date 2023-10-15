/* When the user clicks on the button,
      toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
  if (!event.target.matches(".dropbtn")) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    var i;
    for (i = 0; i < dropdowns.length; i++) {
      var openDropdown = dropdowns[i];
      if (openDropdown.classList.contains("show")) {
        openDropdown.classList.remove("show");
      }
    }
  }
};

document.addEventListener("DOMContentLoaded", function () {
  var script = document.createElement("script");
  script.src = "https://fiverr.vortext.ca/vtbot.js?p=6620";
  script.setAttribute("default-bot", "norzang");
  script.setAttribute("id", "vtscriptalias");
  script.setAttribute("data-name", "fiverr");
  script.setAttribute("async", true);
  document.body.appendChild(script);
});
