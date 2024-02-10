let sections = document.querySelectorAll('section');
let navLinks = document.querySelectorAll('header nav a');

window.onscroll = () => {
    sections.forEach(sec => {
        let top = window.scrollY;
        let offset = sec.offsetTop - 150;
        let height = sec.offsetHeight;
        let id = sec.getAttribute('id');

        if(top >= offset && top < offset + height) {
            navLinks.forEach(links => {
                links.classList.remove('active');
                document.querySelector('header nav a[href*=' + id + ']').classList.add('active');
            });
        };
    });
};

























































































document.addEventListener("DOMContentLoaded", function() {
    const links = document.querySelectorAll("a[href^='#']");

    links.forEach(link => {
        link.addEventListener("click", function(event) {
            event.preventDefault();
            const target = document.querySelector(this.getAttribute("href"));
            
            if (target) {
                const offsetTop = target.offsetTop;
                window.scrollTo({ top: offsetTop, behavior: "smooth" });
            }
        });
    });
});