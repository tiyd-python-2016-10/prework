//console.log($('#post-template'))
//var source = $('#post-template').html();
$.ajax({ url: 'api_template.json',
        dataType: 'jsonp'
       }).done( function (source){
                    console.log(source)
                    var template = Handlebars.compile(source);
                    $.ajax(ajaxContext).done(function (response){

                        var html = template( {endpoint:response} )
                        $("#page_hook").html(html)
                    })
                })


// var source = $('#other-template').html();
// var template = Handlebars.compile(source);
// console.log(source)
// var ajaxContext = { url:"http://swapi.co/api/" }

// $.ajax(ajaxContext).done(function (response){
//     console.log(response)
//     var html = template( {endpoint:response} )
//     // var html = template( response )
//     $("#page_hook").html(html)
//
// })
