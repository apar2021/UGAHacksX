/*!
* Start Bootstrap - Grayscale v7.0.6 (https://startbootstrap.com/theme/grayscale)
* Copyright 2013-2023 Start Bootstrap
* Licensed under MIT (https://github.com/StartBootstrap/startbootstrap-grayscale/blob/master/LICENSE)
*/
//
// Scripts
// 

window.addEventListener('DOMContentLoaded', event => {

    // Navbar shrink function
    var navbarShrink = function () {
        const navbarCollapsible = document.body.querySelector('#mainNav');
        if (!navbarCollapsible) {
            return;
        }
        if (window.scrollY === 0) {
            navbarCollapsible.classList.remove('navbar-shrink')
        } else {
            navbarCollapsible.classList.add('navbar-shrink')
        }

    };

    // Shrink the navbar 
    navbarShrink();

    // Shrink the navbar when page is scrolled
    document.addEventListener('scroll', navbarShrink);

    // Activate Bootstrap scrollspy on the main nav element
    const mainNav = document.body.querySelector('#mainNav');
    if (mainNav) {
        new bootstrap.ScrollSpy(document.body, {
            target: '#mainNav',
            rootMargin: '0px 0px -40%',
        });
    };

    // Collapse responsive navbar when toggler is visible
    const navbarToggler = document.body.querySelector('.navbar-toggler');
    const responsiveNavItems = [].slice.call(
        document.querySelectorAll('#navbarResponsive .nav-link')
    );
    responsiveNavItems.map(function (responsiveNavItem) {
        responsiveNavItem.addEventListener('click', () => {
            if (!responsiveNavItem.classList.contains('dropdown-toggle')) {
                if (window.getComputedStyle(navbarToggler).display !== 'none') {
                navbarToggler.click();
                }
            }
        });
    });
document.getElementById('band-profile-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const profileData = {
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
        name: document.getElementById('bandname').value,
        genre: document.getElementById('genre').value,
        instrument: document.getElementById('instrument').value,
        collab_type: document.getElementById('collab-types').value,
        bio: document.getElementById('bio').value
    };

    fetch('http://127.0.0.1:5000/band-register', {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(profileData)
    })
    .then(response => response.json())
    .then(data => {
        console.log('Success:', data);
        alert("Profile Submitted Successfully!");
        document.getElementById('band-profile-form').reset();
    })
    .catch(error => {
        console.error('Error:', error);
        alert("Error Registering!");
    });
});

});