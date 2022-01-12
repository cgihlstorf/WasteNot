
$(document).ready(function(){ 
    create_dropdown();
});


function myfunction(dropdown_id) {
    console.log(dropdown_id)
    create_dropdown();
    document.getElementById(dropdown_id).classList.toggle('show');
}

window.onclick = function(event) {
    if (!event.target.matches('.dropbtn')) {
      var dropdowns = document.getElementsByClassName("dropdown-content");
      var i;
      for (i = 0; i < dropdowns.length; i++) {
        var openDropdown = dropdowns[i];
        if (openDropdown.classList.contains('show')) {
          openDropdown.classList.remove('show');
        }
      }
    }
  } 

function create_dropdown(){
    $("#listfood").empty();
    $.get("/home/data", function(data){
        let elementS = document.getElementById("listfood");
        for(key in data){
            let a = document.createElement("a");
            a.innerHTML = key;
            a.id = key + 's1';
            a.classList.add("dropdown-item");
            a.setAttribute("name", "food");
            elementS.appendChild(a);
            a.addEventListener('click', function(){
                // console.log("id of the dropdown" + this.id);
                $('#listfood').hide();
                display = document.getElementById('displayDD');
                display.innerText = a.innerHTML;
              });   
        }
    })
}