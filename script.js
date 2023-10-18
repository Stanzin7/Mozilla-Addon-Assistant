jQuery(document).ready(function () {
  // Toggle the chatbot display
  $(".chatbot-toggler").on("click", function (e) {
    if ($("body").hasClass("show-chatbot")) {
      $("body").removeClass("show-chatbot");
    } else {
      $("body").addClass("show-chatbot");
    }
  });

  // Close the chatbot
  $(".close-btn").on("click", function (e) {
    $("body").removeClass("show-chatbot");
  });

  // Handle send button click
  $("#send-btn").on("click", function (e) {
    sendMessage();
  });
});

function sendMessage() {
  let userInput = document.getElementById("user_input").value; // Adjusted this line to match the new textarea id

  fetch("/ask", {
    method: "POST",
    body: new URLSearchParams({ user_message: userInput }),
    headers: {
      "Content-Type": "application/x-www-form-urlencoded",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      let chatBox = document.querySelector(".chatbox");
      chatBox.innerHTML +=
        "<li class='chat outgoing'><p>User: " + userInput + "</p></li>";
      chatBox.innerHTML +=
        "<li class='chat incoming'><span class='material-symbols-outlined'>smart_toy</span><p>Bot: " +
        data.message +
        "</p></li>";

      // Clear the input
      document.getElementById("user_input").value = "";

      // Scroll to the bottom of the chatbox
      $(".chatbox").animate({ scrollTop: $(".chatbox")[0].scrollHeight }, 0);
    });
}

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
