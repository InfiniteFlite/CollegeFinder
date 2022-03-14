$(document).ready(function() {
    processSubmit();
});

processSubmit(){
    $(".mainForm").submit(function(e){

        passed = document.getElementById("APpassed");
        taken = document.getElementById("APtaken");
        if(parseInt(passed.value()) > parseInt(taken.value()))
        {
            alert("You cannot have passed more AP Classes than you took!");
        }
        //else {
        //    console.log("Hi");
        //    $("#form").submit();
        //}
    return false
    });
}
