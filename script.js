fetch("/text.json")
  .then(function (response) {
    return response.json();
  })
  .then(function (myJson) {
	text = myJson.text.replace("\n", "<br>");
    document.getElementById("content-text").innerHTML = text;
  })
  .catch(function (error) {
    console.log("Error: " + error);
  });
