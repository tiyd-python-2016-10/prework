

function createTable(){
    current_seconds = 0
    var rows = 10
    var cols = 10

    var $table = $("<table>")
    $("#gameboard").empty()
    $("#gameboard").append($table)
    for(var row = 0; row < rows; row++){
        var $row = $("<tr>")
        $table.append($row)
        console.log($row)
        for(var col = 0; col < cols; col++){
            var $col = $("<td>")
            $col.click(clickCell).contextmenu(rightClick)
            if(Math.random() < .25){
                $col.addClass("bombcell")
            }
            $row.append($col)
            $col.attr("id", row + "_" + col)

        }
    }
}

function rightClick(event){
    console.log(this)
    event.preventDefault()
    $(this).toggleClass("flagcell")
}

function clickCell(){

    if(!clock){
        clock = setInterval(updateClock, 1000)
    }


    console.log(this)
    if ($(this).hasClass("bombcell")){
        $(this).addClass("redcell")
        gameLost()
    }
    findNeighbors($(this))
}

function findNeighbors(cell){
    console.log(cell.attr("id").split("_"))
    var x = parseInt(cell.attr("id").split("_")[0])
    var y = parseInt(cell.attr("id").split("_")[1])
    var count = 0
    var neighbors = [$("#" + (x-1) + "_" + (y-1)),
                     $("#" +  x    + "_" + (y-1)),
                     $("#" + (x+1) + "_" + (y-1)),
                     $("#" + (x-1) + "_" +  y),
                     $("#" + (x+1) + "_" +  y),
                     $("#" + (x-1) + "_" + (y+1)),
                     $("#" +  x    + "_" + (y+1)),
                     $("#" + (x+1) + "_" + (y+1))
                 ]
    for(var i = 0; i < neighbors.length; i++) {
        if (neighbors[i].hasClass("bombcell")){
            count++
        }
    }
    if (count == 0) {
        for(var i = 0; i < neighbors.length; i++) {
            neighbors[i].click()
        }
    }
    cell.addClass("clicked"+count)
    cell.html(count + "")
    console.log(y)
    console.log(count)
}
function gameWon(){

}
function gameLost(){
    clearInterval(clock)
    console.log("You lose")
    $(".bombcell").addClass("redcell")
    $('td').unbind("click").unbind("contextmenu")
}

var clock
var current_seconds = 0
function updateClock(){
    $("#clock").html(current_seconds++)
}

$("#cols")
$("#startButton").click(createTable)
