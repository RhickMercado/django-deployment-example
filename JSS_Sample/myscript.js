function test() {
  var x = 0;
  while (x < 5)
  {
    console.log("Hello");
    x ++
  }

  for (var i = 0; i < 5; i++)
  {
    console.log("Hello with for loop");
  }


  var x = 1;
  while (x <= 25)
  {
    console.log(x);
    x += 2;
  }

  for (var i = 1; i <= 25; i+=2)
  {
    console.log("odd:"+i);
  }
}

function helloYou(name) {
  console.log("Hello "+ name);
}

var roster = [];

function loopname()
{
  var start = prompt("Would like to start the roster y/n")
  var request = "empty";

  if (start =="y") {


    while ( request != "quit")
    {
      request = prompt("Please select an action: add,remove,display, or quit.");
      if (request == "add") {
        add();
      } else if (request == "display")
      {
        display();
      } else if (request == "remove")
      {
        remove();
      }
    }
  }
}

function display()
{
  console.log(roster);
}

function add()
{
  var addName = prompt("What bname would like to add?")
  roster.push(addName)
}

function remove()
{
  var remName = prompt("What name would you like to remove?")
  var index = roster.indexOf(remName);
  roster.splice(index);
}

function empHello(){
  var employee = {
    name: "Rhick Mercado",
    job: "Programmer",
    age: 40,
    lastName:funtion(){
      console.log(this.name.split(" ")[1])
    }
  }
}

// alert("Welcome to your Bank!");
// var deposit = prompt("How much would you like to deposit");
// alert("You've deposited: " + deposit );
// console.log("You are a cool person!");
