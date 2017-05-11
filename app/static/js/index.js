$(document).ready(function(){
    $("#commitnew").click(function(){
        file = $("#filepush").get(0).files[0];
        $.post("/insertNewImage",{
            img:file
        },function(data){
            alert(data);
        })
    })
});