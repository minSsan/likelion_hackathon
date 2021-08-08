function menuBtn(e){
    for(const btn of document.querySelectorAll('.content-menu-btn')) {
        btn.style.backgroundColor = "rgb(243, 243, 243)";
    }
    for(let box of document.querySelectorAll('.content-box')) {
        box.style.display = "none"
    }
    e.style.backgroundColor = "rgba(228, 236, 245, 1)";

    let box = document.querySelector('.box' + e.getAttribute('box_id'));
    box.style.display = "flex";
}