function check(n) {
    if (n < 2) { 
        return false;
    }
    for (let i = 2; i <= Math.sqrt(n); i++) {
        if (n % i === 0) {
            return false;
        }
    }
    return true;
}
let k = 1000;
while (!check(k)) {
    k++;
}
console.log(k, 'là số thỏa mãn  ');

