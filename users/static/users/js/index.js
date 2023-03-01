'use strict';

(function() {
    // Side Nav

    const sideNavElement = document.getElementById('sidenav');
    const sideNavContent = document.getElementById('sidenav-content');

    function handleSideNavExpandClick(e) {
        e.preventDefault();

        if (sideNavElement.offsetWidth > 0) {
            sideNavElement.style.width = 0;
        } else {
            sideNavElement.style.width = `${sideNavContent.offsetWidth}px`;
        }
    }
    const sideNavExpandBtns = document.querySelectorAll('.sidenav-expand-btn');
    if (sideNavExpandBtns) {
        sideNavExpandBtns.forEach(sideNavExpandBtn => {
            sideNavExpandBtn.addEventListener('click', handleSideNavExpandClick, false);
        });
    }
})();
