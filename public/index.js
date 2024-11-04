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
    
    animais.forEach(animal => {
        //para cada animal eu crio um elemento com o nome e coloco na lista
        const item = document.createElement('li')
        item.innerText = animal.nome

        lista.appendChild(item)
    });

    

}

function app(){
    console.log('App iniciado')
    carregarAnimais()
}

app()