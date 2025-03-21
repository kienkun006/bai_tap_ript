let n = prompt();
if ((n % 4 ===0 && n% 100 !==0)  || (n % 400 ===0)){
    console.log( n,": Là năm nhuậm");
}
else{
    console.log(n ,": Không phải năm nhuậm");
}
