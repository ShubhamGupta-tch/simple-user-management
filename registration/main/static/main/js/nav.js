const hamburger = document.querySelector('.hamburger');
const navlinks = document.querySelector('.nav-links');
const links = document.querySelectorAll('.nav-links li');

hamburger.addEventListener('click', () => {
    navlinks.classList.toggle('open');

    hamburger.classList.toggle('toggle');
    console.log(hamburger.classList);

    links.forEach((link, index) => {
        // console.log(link.style.animation.includes("NavlinkFadeIn"))
        if (link.style.animation.includes("NavlinkFadeIn")){
            link.style.animation = `NavlinkFadeOut 0.5s ease forwards ${(index/(links.length))}s`;
        }
        else{
            link.style.animation = `NavlinkFadeIn 0.5s ease forwards ${index/(links.length)}s`;
    }
    });
});
