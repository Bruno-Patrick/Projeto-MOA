const cards = document.querySelectorAll('.draggcard')
const dropzone = document.querySelectorAll('.dropzone')

cards.forEach(draggcard => {
    draggcard.addEventListener('dragstart', dragstart)
    draggcard.addEventListener('drag', drag)
    draggcard.addEventListener('dragend', dragend)
})

function dragstart() {
    dropzone.forEach( dropzone => dropzone.classList.add('highlight'))
    // this = draggcard
    this.classList.add('is-dragging')
}

function drag() {
}

function dragend() {
    dropzone.forEach( dropzone => dropzone.classList.remove('highlight'))
    this.classList.remove('is-dragging')
    // this = draggcard
}

// Dropzone

dropzone.forEach( dropzone => {
    dropzone.addEventListener('dragenter', dragenter)
    dropzone.addEventListener('dragover', dragover)
    dropzone.addEventListener('dragleave', dragleave)
    dropzone.addEventListener('drop', drop)
})

function dragenter() {
    
}

function dragover() {
    this.classList.add('over')

    const cardBeingDragged = document.querySelector('.is-dragging')

    this.appendChild(cardBeingDragged)
}

function dragleave() {
    this.classList.remove('over')
}

function drop() {
    this.classList.remove('over')
}

// Criar novos Cards
function NewCard() {
    let criarCard = document.querySelector('button#done');
    criarCard.addEventListener("click", function(){ 
        alert("Hello World!"); });
}