$(document).ready(function() {
    processSubmit();
});

function processSubmit(){
    $(".mainForm").submit(function(e){
        var formId = this.id,
        form = this;
        passed = document.getElementById("APpassed");
        taken = document.getElementById("APtaken");
        if(document.getElementById("APpassed").value > document.getElementById("APtaken").value)
        {
            alert("You cannot have passed more AP Classes than you took!");
            e.preventDefault(e);
        }
        else {
           form.submit();
            }
    });
}
