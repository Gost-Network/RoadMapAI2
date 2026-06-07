console.log("Dashboard Loaded");

document
.getElementById("routeBtn")
.addEventListener("click", function(){

    let source =
    document.getElementById("source").value;

    let destination =
    document.getElementById("destination").value;

    if(
        source === "" ||
        destination === ""
    ){

        alert(
            "Please Enter Source And Destination"
        );

        return;
    }

    console.log(
        source,
        destination
    );

});