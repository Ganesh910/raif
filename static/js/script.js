console.log('Hello from script.js');

document.addEventListener('DOMContentLoaded', () => {
let nav = document.querySelector('nav');
let ham = document.querySelector('.hamburger');

ham.addEventListener('click', () => {
    nav.classList.toggle('nav--active');
    ham.classList.toggle('ham--active');
});
});