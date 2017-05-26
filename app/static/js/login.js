$("document").ready(function(){
    $("#login").click(function(){
        username = $("#username").val();
        password = $("#passwords").val();
        $.post("/login",{
            username:username,
            password:password
        },function(data){
            if(data.code==5){
                alert(1234);
            }else{
                localStorage.type = data.code;
                window.location.href = "/index";
            }
        })
    })
});