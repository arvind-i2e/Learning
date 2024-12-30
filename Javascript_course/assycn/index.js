//Synchronous Programming (initiate one by one)
// let a = prompt("Enter your name");
// console.log(a + " Welcome to the universe");

//Asynchronous programming
// console.log("Start");
// setTimeout(function () {
//   console.log("Hey I'm Great");
// }, 3000);
// console.log("End");

// Callback function 
function loadScript(src, Callback) {
  var script = document.createElement("Script");
  script.src = src;
  script.onload = function () {
    console.log("Loaded script with SRC " + src);
    Callback(src);
  };
  document.body.appendChild(script);
}
function hello(src) {
  alert("Hello Universe " + src);
}
loadScript(
  "https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js",
  hello
);
