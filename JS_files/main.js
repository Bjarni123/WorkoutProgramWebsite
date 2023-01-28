import * as program from "./JSON_files/workoutProgram.json";
var data = program.Block1;

/*
fetch("./JSON_files/workoutProgram.json")
    .then((response) => response.json())
    .then((data) => program = data);
*/

console.log("DATA: ", data);