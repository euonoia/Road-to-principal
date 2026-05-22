function calculateTip(billTotal, tipPercent){
    return billTotal * (tipPercent/100);
}

console.log("Test 1 (Should be 15):", calculateTip(100, 15)); 
console.log("Test 2 (Should be 10):", calculateTip(50, 20));  
console.log("Test 3 (Should be 4.5):", calculateTip(30, 15));