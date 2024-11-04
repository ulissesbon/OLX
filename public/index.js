async function carregarAnimais(){
    // axios.get('http://localhost:8000/animais')
    //     .then(response => console.log(response.data))
    
        //uma response que espera o get da porta do servidor indicado
    const response = await axios.get('http://localhost:8000/animais')
    // console.log(response.data)

        //animais pega os dados vindo dessa response
    const animais = response.data

        //lista que está associada ao id cadastrado no documento html
    const lista = document.getElementById('lista-animais')

    //antes de listar, apago o texto para não ser duplicado em manipularFormulario
    lista.innerHTML = ''
    
    animais.forEach(animal => {
        //para cada animal eu crio um elemento com o nome e coloco na lista
        const item = document.createElement('li')
        item.innerText = animal.nome

        lista.appendChild(item)
    });
}


function manipularFormulario() {
    const form_animal = document.getElementById('form-animal')
    const input_nome = document.getElementById('nome')

    form_animal.onsubmit = async (event) => {
        event.preventDefault() //para não reiniciar a página toda vez que clicar em gravar
        const nome_animal = input_nome.value

        await axios.post('http://localhost:8000/animais', {
            nome: nome_animal,
            idade: 1,
            sexo: 'Não especificado',
            cor_pelagem: 'Sem cor'
        }) 

        alert(`Animal cadastrado: ${nome_animal}`)
        carregarAnimais()
    }
}



function app(){
    console.log('App iniciado')
    carregarAnimais()
    manipularFormulario()
}

app()