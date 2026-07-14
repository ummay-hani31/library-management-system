// =========================
// Library Management System
// JavaScript
// =========================

// Auto close alerts

setTimeout(function(){

    let alerts=document.querySelectorAll(".alert");

    alerts.forEach(function(alert){

        alert.classList.add("fade");

        setTimeout(function(){

            alert.remove();

        },500);

    });

},3000);

// Confirm delete

function confirmDelete(){

    return confirm("Are you sure you want to delete this record?");

}

// Highlight active menu

document.addEventListener("DOMContentLoaded",function(){

    let current=window.location.pathname;

    let links=document.querySelectorAll(".nav-link");

    links.forEach(function(link){

        if(link.getAttribute("href")==current){

            link.classList.add("active");

        }

    });

});