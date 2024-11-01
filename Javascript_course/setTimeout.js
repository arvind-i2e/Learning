// setTimeout(function() {
//     console.log("hello");
// }, 2 * 1000); //For 2 second timeout.
// setTimeout(function bye() {
//     console.log("bye");
// }, 1 * 1000);//For 1 second timeout.

// Print 1 to 10 but with delay of 1 sec after each number gets printed.
// for (let i = 1; i <= 10; i++) {
//   setTimeout(function () {
//     console.log(i);
//   }, i * 1000);
// }

// Print 10 to 1 but with delay of 1 sec after each number gets printed.
for (let i = 10; i >= 1; i--) {
  setTimeout(function () {
    console.log(i);
  }, (11 - i) * 500);
}
