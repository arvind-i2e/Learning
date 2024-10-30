// const arr=[1,2,3,4];
// console.log(arr);
// arr=2.14;Error:(Assignment to constant variable)

//Multi-datatype in single array
brr=[4,"Arvind",7.9,true];
console.log(brr);
console.log(typeof(brr));//Object

//2-d array
xrr=[[1,2,3],[2,34,53,3]];
console.log(xrr);

//Different loops with arrays
//For loop
zrr=[3,7,3,8,0,2];
console.log(zrr);
for(let i=0;i<zrr.length;i++){
    zrr[i]*=2;
}
console.log(zrr);

//ForOf loop
for (const ele of zrr) {
    console.log(ele);//In this we can not fetch index
}
for (let ele of zrr) {
    ele*=2;
    console.log(ele);
}

//ForEach loop
zrr.forEach((ele,i,zrr) => {
    console.log(ele,i,zrr);//In this we can fetch index too
});
