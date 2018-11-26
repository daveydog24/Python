let counter = 1

function takeTurn(){
    counter++;
    console.log("The turn is now at:", counter)
}

function changeSquare(num){
    console.log(num)
    
    if (counter % 2 == 1){
        itemContent = document.getElementById(num).innerHTML(
            `<img class="x" src="https://upload.wikimedia.org/wikipedia/commons/7/77/Letter_x.svg" alt="x">`
        )
    }
    else{
        itemContent = document.getElementById(num).innerHTML(
            `<img class="o" src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBd4LBnt4XNgIlH3phAUY6iAnOPem_WJsrAeSo8v7ONK00Xoeiqg" alt="o">`
        )
    }
    takeTurn()
}
