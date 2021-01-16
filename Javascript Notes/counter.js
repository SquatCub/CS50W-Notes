if (!localStorage.getItem('counter')) {
    localStorage.setItem('counter', 0);
}

function count(){
    let counter = localStorage.getItem('counter');
    counter++;
    document.querySelector('h1').innerHTML = counter;

    localStorage.setItem('counter', counter);
}

document.addEventListener('DOMContentLoaded', function() { //Funcion para inicializar el DOM cuando este aun no se haya renderizado
    document.querySelector('h1').innerHTML = localStorage.getItem('counter');
    document.querySelector('button').onclick = count; // == documento.querySelector('button').addEventListener('click', count)
})