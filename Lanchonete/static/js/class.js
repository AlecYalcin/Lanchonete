// Javascript Criado com a Intenção de Adicionar CLASSES ao Forms

const inputName = document.querySelector('form')

for(var input=0; input < inputName.length; input++) {
    if (inputName[input].tagName == 'INPUT') {
        inputName[input].classList.add("form-control")
        inputName[input].classList.add("form-control-md")
    }    
    inputName[input].classList.add('m-1')
}