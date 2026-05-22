const name = "Alice";
let age = 5;

if (age >= 0 && age <= 120){
    if (age >= 18){
        console.log(name + " is an Adult.");
    }
    else if (age <= 17){
        console.log(name + " Is a minor.");
    }
} 
else {
    console.log("Invalid age.");
}