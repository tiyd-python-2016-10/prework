Handlebars.registerHelper('prevent-orphan', function(text) {
    var lastSpace = text.toLowerCase().lastIndexOf(" ");
    return text.slice(0, lastSpace) + text.slice(lastSpace).replace(' ', "&nbsp;");
});

Handlebars.registerHelper('fullname', function(person) {
    return person.first + " " + person.last;
});



var source = $('#post-template').html();
var template = Handlebars.compile(source);
// console.log(template)
var context = {
  title: 'Our First Post',
  content: '<p>This is some content for our post add some more stuff until it wraps trying some more.</p>',
  author: 'Daniel Yuschick',
  name: {first:"Sam", last:"boyarsky"},
  image: 'for_you.jpg',
  sources: [
  { title: 'CSS Weekly', url: 'http://css-weekly.com/' },
  { title: 'Smashing Magazine', url: 'https://www.smashingmagazine.com/' },
],
  myList: ["hi mom", "blah di blah", "hmmm", "creativity, out the window", "good thing we're in a basement"],
  myObj: {uno:"hi mom",
          dos:"blah di blah",
          tres:"hmmm",
          cuatro:"creativity, out the window",
          cinco:"good thing we're in a basement"
        }
};



var html = template(context);
console.log(html)


$("#main").html(html)
