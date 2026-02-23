
const navLinks = Array.from(document.querySelectorAll('[data-link]'))
  .filter(a => a.getAttribute('href')?.startsWith('#'));

const sections = navLinks
  .map(a => document.querySelector(a.getAttribute('href')))
  .filter(Boolean);

function setActive(id){
  navLinks.forEach(a => a.classList.toggle('active', a.getAttribute('href') === '#' + id));
}

const observer = new IntersectionObserver((entries) => {
  const hit = entries
    .filter(e => e.isIntersecting)
    .sort((a,b) => b.intersectionRatio - a.intersectionRatio)[0];

  if (hit?.target?.id) setActive(hit.target.id);
}, { threshold: [0.35, 0.6] });

sections.forEach(s => observer.observe(s));

// Footer év
document.getElementById('year').textContent = new Date().getFullYear();

//form
const form = document.getElementById('contactForm');
const msg = document.getElementById('formMsg');

form.addEventListener('submit', (e) => {
  e.preventDefault();
  msg.textContent = "Köszönjük! (Demo) Üzenet rögzítve.";
  form.reset();
  setTimeout(() => msg.textContent = "", 3500);
});
