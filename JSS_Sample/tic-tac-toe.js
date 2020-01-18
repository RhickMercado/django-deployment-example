console.log('Connected!');

var restart = document.querySelector('#btnRestart')

// Grabs all the squares
var squares = document.querySelectorAll('td');

// var r1c1 = document.querySelector("#R1C1");
// var r1c2 = document.querySelector("#R1C2");
// var r1c3 = document.querySelector("#R1C3");
// var r2c1 = document.querySelector("#R2C1");
// var r2c2 = document.querySelector("#R2C2");
// var r2c3 = document.querySelector("#R2C3");
// var r3c1 = document.querySelector("#R3C1");
// var r3c2 = document.querySelector("#R3C2");
// var r3c3 = document.querySelector("#R3C3");
//
// r1c1.addEventListener('click', function(){
//   if (r1c1.textContent == "X") {
//     r1c1.textContent = "O";
//   } else if (r1c1.textContent == "O") {
//     r1c1.textContent = "";
//   } else {
//     r1c1.textContent = "X";
//   }
// })

// Clear all the squares
// r1c1.addEventListener('dblclick', function(){
//   r1c1.textContent = "";
// })

// Clear all the squares
function clearBoard() {
  // for each (var a in squares) {
  //   a.textContent = '';
  //
  // }
  for (var i = 0; i < squares.length; i++) {
    squares[i].textContent = '';
  }
}

function changeMarker(){
  if(this.textContent === ''){
    this.textContent = 'X';
  } else if(this.textContent === 'X') {
    this.textContent = 'O';
  } else {
    this.textContent = '';
  }
}

for (var i = 0; i < squares.length; i++) {
  squares[i].addEventListener('click', changeMarker);
}
restart.addEventListener('click', clearBoard);

// Check the square marker


// For loop to add event listeners to all the squares
