$(document).ready(function(){
    type = localStorage.type;
    if(type==0){
        $("#addnew").hide();
    }else{
        $("#addnew").show();
    }
})