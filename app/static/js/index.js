$(document).ready(function(){
    type = localStorage.type;
    if(type==0){
        $("#addnew").hide();
    }else{
        $("#addnew").show();
    }
});



$(document).ready(function(){
    $("#new-user").click(function(){
        username = $("#username").val();
        password = $("#password").val();
        $.post("/register",{
            username : username,
            password : password
        },function(data){
             if(data.code==0){
                alert("新用户添加成功");
                $("#myModal").modal('hide');
            }else{
                alert("注册失败");
            }
        })
    })
})