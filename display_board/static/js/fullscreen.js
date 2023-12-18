document.getElementById('fullscreen-btn').addEventListener('click', function () {
    var elem = document.documentElement;
    var navbar = document.getElementById('navbar');
    var fullscreen_btn = document.getElementById('fullscreen-btn');

    if (!document.fullscreenElement) {
        if (elem.requestFullscreen) {
            elem.requestFullscreen();
        }
        if (navbar) {
            navbar.style.display = 'none';
        }
        if (fullscreen_btn) {
            fullscreen_btn.style.display = 'none';
        }
    } else {
        if (document.exitFullscreen) {
            document.exitFullscreen();
        }
    }
});

document.addEventListener('fullscreenchange', function () {
    var navbar = document.getElementById('navbar');
    var fullscreen_btn = document.getElementById('fullscreen-btn');

    // Check if fullscreen mode is exited
    if (!document.fullscreenElement && navbar) {
        // Show the navbar
        navbar.style.display = ''; // Set to an empty string to use the default display property
    }
    if (!document.fullscreenElement && fullscreen_btn) {
        fullscreen_btn.style.display = ''; // Set to an empty string to use the default display property
    }
});
