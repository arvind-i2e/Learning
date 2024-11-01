// Callback function: It is a function that pass into another function.

function product(a,b,c){
    return a*b*c;
}

function fun(x,y){
    let a=x(2,5,4);
    console.log(a-y);
}
fun(product,7);