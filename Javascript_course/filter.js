//Filter out even element from array.

arr = [1, 9, 2, 7, 4, 5, 6, 2, 8];
console.log(arr);

arr = arr.filter((ele) => {
  return ele % 2 != 0 ? true : false;
});
console.log(arr);

let vrr = arr.filter((ele) => ele > 5);
console.log(vrr);
