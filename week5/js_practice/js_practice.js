console.log($("body"))
var newButton = $("<button>")
newButton.attr("id","HiMom")
$("body").append(newButton)

function randInt(a,b){
    return Math.floor((Math.random() * b-a) + a);
}
function move(){
    console.log("running")
    
    newTop = randInt(0,1000) + "px"
    newLeft = randInt(0,1000) + "px"
    console.log(newTop, newLeft)
    button = document.getElementById("scardyButton")
    button = $("#scardyButton")

    console.log(button)
    console.log(this)
    button.style.top = newTop
    button.style.left = newLeft
}


function doStuff(){
    console.log("doing stuff")
    //make an array, iterate through it and log each element to the console.

}

function showUserIn(){
    //This is one super annoying way to get user input.
    // userIn = prompt("what do you want?")
    // console.log(userIn)
    console.log(document.getElementById("UserInput").value)
}
document.getElementById("UserInput").addEventListener('keyup', showUserIn)


console.log("hello")

document.getElementById("scardyButton").addEventListener('mouseover', move)

button = document.getElementById("testButton")
header = document.getElementsByTagName("h1")
console.log(header)
header[0].addEventListener('click', doStuff)
// button.addEventListener('click', doStuff)
// button.addEventListener('mousedown', doStuff)
// button.addEventListener('mouseover', doStuff)
// button.addEventListener('mouseout', doStuff)
button.addEventListener('click', showUserIn)
console.log(document)
console.log(button)
