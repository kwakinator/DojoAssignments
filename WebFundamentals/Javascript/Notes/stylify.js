

//document has to load itself out. once the .ready is in place-- the page will load at that point.

var $ = function(thingy){

  var stuffthingycando = {
            ready: function(callback){
              document.addEventListener('DOMContentLoaded', function(){
                callback();
              })
            },
            click: function(callback){
              document.getElementById(thingy).addEventListener('click', function() {
                callback();
              })
            }
  }

  return stuffthingycando;
}

console.log($(document));

$(document).ready(function(){
  console.log('the document is ready!');

  $('katiestyle').click(function(){
    document.getElementById('styler').href='teamkatie.css';
  })

})
