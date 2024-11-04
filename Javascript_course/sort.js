let arr=[1,9,7,2];
console.log(arr);

//arr=arr.sort();(wrong approach for sorting directly).\

arr=arr.sort((a,b)=>a-b);
console.log(arr);//Ascending order.

let brr=arr.sort((a,b)=>b-a);
console.log(brr);//descending order.


// Dealing with negative numbers too.
let x=[1,-9,-3,2];
x=x.sort((a,b)=>Math.abs(a)-Math.abs(b));
console.log(x);
