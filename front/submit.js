var form = document.querySelector("form");

form.addEventListener("submit", function(event) {
  var data = new FormData(form);
  var output = "";
  for (const entry of data) {
    output = output + entry[0] + "=" + entry[1] + "\r";
  };
  event.preventDefault();
}, false);