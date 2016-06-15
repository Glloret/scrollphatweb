$(document).ready(function () {
  ws = new WebSocket("ws://192.168.1.132:8888/ws");
  $('.square').click(function(event){
    led= event.target.id
    if ($(this).attr('b')== 0) {
      $(this).attr('b',1).removeClass('off').addClass('on');
    } else {
      $(this).attr('b',0).removeClass('on').addClass('off');
      led = led*-1
    }
    ws.send(led);
  });
});
$(window).ready(updateHeight);
$(window).resize(updateHeight);
function updateHeight()
{
    var div = $('.square');
    var width = div.width();
    div.css('height', width);
}
