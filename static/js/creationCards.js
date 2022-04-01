window.onload = () => {

    let conteiner = document.querySelector('div.PaideTodos');

    let newcard = document.querySelectorAll('input.createCard');
    newcard.forEach(item => {
        item.addEventListener('click', () => {
            let novaDraggcard = document.createElement('div');
            novaDraggcard.classList.add('draggcard');
            novaDraggcard.setAttribute('draggable', true);

            let novaContent = document.createElement('div');
            novaContent.classList.add('content');

            let novaTextArea = document.createElement('textarea');
            novaTextArea.setAttribute('placeholder', 'Enter a Note');

            // novaContent.appendChild(novaTextArea);
            novaContent.appendChild(novaTextArea);
            novaDraggcard.appendChild(novaContent);
            console.log(conteiner)
            conteiner.appendChild(novaDraggcard);

        });
    });

    // function NewCard() {
    //     let criarCard = document.querySelector('input#done');
    //     criarCard.addEventListener("click", function(){ 
    //         alert("Hello World!"); });
    // }
}