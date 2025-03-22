let n = parseFloat(prompt("Nhập điểm:"));

if (n >= 9 && n <=10) {
    console.log("Xuất sắc");
} else if (n >= 8 && n<9)  {
    console.log("Giỏi");
} else if (n >= 6.5 && n<8) {
    console.log("Khá");
} else if (n >= 5 && n<6.5) {
    console.log("Trung bình");
} else if (n >=0 && n <5){
    console.log("Yếu");
} else {
    console.log("Lỗi")
}

