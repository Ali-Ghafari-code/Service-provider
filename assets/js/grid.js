
//sidebar animation//
let navItems = document.getElementsByClassName("nav");
// Loop through each nav item
for (let i = 0; i < navItems.length; i++) {
    let arrowIcon = navItems[i].querySelector('.fa-arrow-right');

    navItems[i].addEventListener('mouseover', function () {
        arrowIcon.classList.replace('fade-out', 'fade-in');
    });
    navItems[i].addEventListener('mouseout', function () {
        arrowIcon.classList.replace('fade-in', 'fade-out');
    });
}
// sidebar
const close = document.querySelector(".close");
const sidebar = document.querySelector('.sidebar');
const btn = document.querySelector('.bar');
const body = document.body; // Select the body element


function toggleSubMenu(clickedElement) {
    // Find the next sibling element (submenu)
    let submenu = clickedElement.nextElementSibling;

    // Get all elements with the class "Submenu"
    let allSubmenus = document.querySelectorAll('.Submenu');

    // Close all submenus
    allSubmenus.forEach(function (item) {
        if (item !== submenu) {
            item.classList.add('d-none');
        }
    });

    // Toggle the visibility of the selected submenu
    submenu.classList.toggle("d-none");
}
jalaliDatepicker.startWatch({ time: true });
btn.addEventListener('click', function () {
    sidebar.classList.add('active');
    sidebar.style.visibility = 'visible';
});

close.addEventListener('click', function () {
    sidebar.classList.remove('active');
});




