function createModale(id) {
    let modaleNode = document.querySelector(id);
    let overlay = modaleNode.querySelector(".overlay");
    let closeBtn = modaleNode.querySelector(".close-btn")


    function openModale(){
        modaleNode.classList.add("active");
    }

    function closeModale(){
        modaleNode.classList.remove("active");
    }

    overlay.addEventListener("click", closeModale);
    closeBtn.addEventListener("click", closeModale);
    return openModale;
}

let modale = createModale("#modale-1");
document.querySelector("#btn-1").addEventListener("click", modale)
document.querySelector("#btn-2").addEventListener("click", modale)
document.querySelector("#btn-3").addEventListener("click", modale)
