// Create an array.
arr = [1, 6, 8, 3];
console.log(arr);
n=arr.length;
console.log(n);//return length of 

//Traverse the array
for(let i=0;i<n;i++){
    console.log(arr[i]);
}

//Fetching through index
console.log(arr[2]);

// Operations with arrays(basics)
arr.push(9);//Add element at last
console.log(arr);
arr.push(0);
console.log(arr);
arr.pop();//Remove element from last
console.log(arr);
arr.unshift(2);
console.log(arr);//Add element at first
arr.shift();//Remove first element
console.log(arr);

