// Map: Four ways of mapping.
function add10(ele) {
  return ele + 10;
}

let arr = [1, -6, -3, 8];
console.log(arr);

arr = arr.map(add10);
console.log(arr);

arr = arr.map(function (ele) {
  return ele * ele;
});
console.log(arr);

arr = arr.map((ele) => {
  return ele / 10;
});
console.log(arr);

let brr = arr.map((ele) => ele * 2);
console.log(arr);
console.log(brr);
