// $() is used for selecting items in the DOM



/**
 * Adding AJAX request endpoints for each navbar button
 * 
 * TODO
 * Condense this as it is a lot of repeated code.
 */
$(document).ready(function(){
    $("#hide").click(function(){
        $(this).hide();
        });
    

    $('#btn_home').click(function(){
    
        const xhr = new XMLHttpRequest();
        const container = document.getElementById('content-container');
        
        xhr.onload = function() {
            if (this.status === 200) {
                    container.innerHTML = xhr.responseText;
                } else {
                    console.warn('Did not recieve 200 response code.')
                }};
        xhr.open('get', '/home');
        xhr.send();
    });


    $('#btn_personal_life').click(function(){
        
        const xhr = new XMLHttpRequest();
        const container = document.getElementById('content-container');
        
        xhr.onload = function() {
            if (this.status === 200) {
                    container.innerHTML = xhr.responseText;
                } else {
                    console.warn('Did not recieve 200 response code.')
                }};
        xhr.open('get', '/personal');
        xhr.send();
    });


    $('#btn_work_history').click(function(){
        
        const xhr = new XMLHttpRequest();
        const container = document.getElementById('content-container');
        
        xhr.onload = function() {
            if (this.status === 200) {
                    container.innerHTML = xhr.responseText;
                } else {
                    console.warn('Did not recieve 200 response code.')
                }};
        xhr.open('get', '/work');
        xhr.send();
    });


    $('#btn_programming').click(function(){
        
        const xhr = new XMLHttpRequest();
        const container = document.getElementById('content-container');
        
        xhr.onload = function() {
            if (this.status === 200) {
                    container.innerHTML = xhr.responseText;
                } else {
                    console.warn('Did not recieve 200 response code.')
                }};
        xhr.open('get', '/programming');
        xhr.send();
    });


    $('#btn_contact').click(function(){
        
        const xhr = new XMLHttpRequest();
        const container = document.getElementById('content-container');
        
        xhr.onload = function() {
            if (this.status === 200) {
                    container.innerHTML = xhr.responseText;
                } else {
                    console.warn('Did not recieve 200 response code.')
                }};
        xhr.open('get', '/contact');
        xhr.send();
    });
    
    
    
        // $.getJSON('/card', {
        //     // Parameters to pass thru
        // }, function(data) {
        //     $('#card-heading').text(data['card-heading']);
        //     document.getElementById('card-image').src=data['card-image'];
        //     $('#card-description').text(data['card-description'])
        //     });
        // });  
});

// function navbarToggle() {
//     var x = document.getElementById("nav-bar-list");
//     if (x.style.display === "block") {
//       x.style.display = "none";
//     } else {
//       x.style.display = "block";
//     }
//   }


// xhr.onload = function() {
//     if (this.status === 200) {
//         container.innerHTML = xhr.responseText;
//     } else {
//         console.warn('Did not recieve 200 response code.')
//     }

// }


// xhr.open('get', '/hobbies');
// xhr.send();




// var loc = window.location.pathname;
// var dir = loc.substring(0, loc.lastIndexOf('/'));

// console.log(loc)
// console.log(dir)