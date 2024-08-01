document.addEventListener('DOMContentLoaded', function() {
    /**
     * Represents the navbar toggler element.
     * @type {HTMLElement}
     */
    const navbarToggler = document.getElementById('navbar-toggler');
    const navbarCollapse = document.getElementById('navbarNav');

    navbarToggler.addEventListener('click', function() {
        navbarCollapse.classList.toggle('show');
    });
});
