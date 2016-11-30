var url = "http://api.open-notify.org/iss-now.json"

function updatePosition(){
    $.ajax({
        url: url
    }).done(function(result) {
        console.log("result ready")
        var lat = result.iss_position.latitude
        var long = result.iss_position.longitude
        console.log(result.iss_position)
        var text = "latitude: " + lat + " longitude: " + long
        // text += "<br/>" + Date().toISOString()
        $("#location").html()

    });
    console.log("After Ajax")
    // $("#some_element_on_the_page").html(lat)
}

$("#doStuff").click(updatePosition)
// setInterval(updatePosition, 1000)
