fetch("./JSON_files/workoutProgram.json")
    .then((response) => response.json())
    .then((data) => console.log(data));