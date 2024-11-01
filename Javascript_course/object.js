//Object is kind of like map/Dictionary where we have 'Key-Value' pairs
let x = {
  //x is the Object
  'name': "Albert",//we also can use string as a Key.
   age: "50",
   isMarried: true,
};
// console.log(x.isMarried);
// console.log(x.name);
// console.log(x['age']);
// x.age=55;
// console.log(x['age']);
// For in loop for objects.
for (const key in x) {
  console.log(key, x[key]);
}
