$(function () {
    var ht = $(".list>h3").html();
    $(".create").on("click", function () {
       $(".shade").removeClass("hid");
       var strs = "<h3>新增</h3><span style='display: none'>id<input type=\"text\" class='nid' value='0'></span>";
       strs += "<span style='display: none'>页面信息<input type=\"text\" value='" + ht + "'></span>";
       if (ht == "班级信息") {
           strs += "<span class='thename'>班级名称<input type=\"text\"></span>"
       }
       strs += "<span><button class='confirms'>确定</button><button class='consoles'>取消</button></span>";
       $(".projectile").removeClass("hid").html(strs);

   });
   $(document).on("click", ".confirms", function () {
       if (ht == "班级信息") {
           var urls = '/classes/';
       }
       var nid = $(".nid").val();
       var name = $(".thename").children("input").val();
       data = nid + "-" +name;
       $.ajax({
           url: urls,
           type: "PUT",
           data: data,
           dataType: "JSON",
           complete: function () {
               $(".shade").addClass("hid");
               $(".projectile").addClass("hid");
           }
       })
   });
   $(document).on("click", ".consoles", function () {
       $(".shade").addClass("hid");
       $(".projectile").addClass("hid");
   });
});