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
let conteinerToDo = document.querySelector('div.To-Do-Father');

let newcardToDo = document.querySelectorAll('input.To-Do-NewCard');
newcardToDo.forEach(item => {
    item.addEventListener('click', () => {
        let novaDraggcard = document.createElement('div');
        novaDraggcard.classList.add('draggcard');
        novaDraggcard.setAttribute('draggable', true);

        let novaContent = document.createElement('div');
        novaContent.classList.add('content');

        let novaTextArea = document.createElement('textarea');
        novaTextArea.setAttribute('placeholder', 'Enter a Note');
        novaTextArea.setAttribute('name', 'conteudo');
        novaTextArea.setAttribute('id', 'conteudo');
        novaTextArea.setAttribute('cols', '30');
        novaTextArea.setAttribute('rows', '10');

        // novaContent.appendChild(novaTextArea);
        novaContent.appendChild(novaTextArea);
        novaDraggcard.appendChild(novaContent);
        conteinerToDo.appendChild(novaDraggcard);
    });   
});

let conteinerInProgress = document.querySelector('div.In-Progress-Father');

let newcardInProgress = document.querySelectorAll('input.In-Progress-NewCard');
newcardToDo.forEach(item => {
    item.addEventListener('click', () => {
        let novaDraggcard = document.createElement('div');
        novaDraggcard.classList.add('draggcard');
        novaDraggcard.setAttribute('draggable', true);

        let novaContent = document.createElement('div');
        novaContent.classList.add('content');

        let novaTextArea = document.createElement('textarea');
        novaTextArea.setAttribute('placeholder', 'Enter a Note');
        novaTextArea.setAttribute('name', 'conteudo');
        novaTextArea.setAttribute('id', 'conteudo');
        novaTextArea.setAttribute('cols', '30');
        novaTextArea.setAttribute('rows', '10');

        // novaContent.appendChild(novaTextArea);
        novaContent.appendChild(novaTextArea);
        novaDraggcard.appendChild(novaContent);
        conteinerInProgress.appendChild(novaDraggcard);
    });    
});