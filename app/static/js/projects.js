var toggleOfficial = document.getElementById("toggle-official");
toggleOfficial.onclick = function() {
    document.querySelectorAll('.official').forEach(el => el.classList.remove('hidden'));
    document.querySelectorAll('.unofficial').forEach(el => el.classList.add('hidden'));

    document.getElementById("toggle-official").classList.add('active');
    document.getElementById("toggle-all").classList.remove('active');
    document.getElementById("toggle-unofficial").classList.remove('active');
}

var toggleAll = document.getElementById("toggle-all");
toggleAll.onclick = function() {
    document.querySelectorAll('.official').forEach(el => el.classList.remove('hidden'));
    document.querySelectorAll('.unofficial').forEach(el => el.classList.remove('hidden'));

    document.getElementById("toggle-official").classList.remove('active');
    document.getElementById("toggle-all").classList.add('active');
    document.getElementById("toggle-unofficial").classList.remove('active');
}

var toggleUnofficial = document.getElementById("toggle-unofficial");
toggleUnofficial.onclick = function() {
    document.querySelectorAll('.official').forEach(el => el.classList.add('hidden'));
    document.querySelectorAll('.unofficial').forEach(el => el.classList.remove('hidden'));

    document.getElementById("toggle-official").classList.remove('active');
    document.getElementById("toggle-all").classList.remove('active');
    document.getElementById("toggle-unofficial").classList.add('active');
}