let counter = 1

function takeTurn(){
    counter++;
    console.log("The turn is now at:", counter)
}

function changeSquare(num){
    num = "img" + num
    console.log(num)
    
    if (counter % 2 == 1){
        document.getElementById(num).src = "https://upload.wikimedia.org/wikipedia/commons/7/77/Letter_x.svg";
        document.getElementById(num).style.display = "block";
        document.getElementById(num).className = "x";   
    } else {
        document.getElementById(num).src = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTBd4LBnt4XNgIlH3phAUY6iAnOPem_WJsrAeSo8v7ONK00Xoeiqg";
        document.getElementById(num).style.display = "block";
        document.getElementById(num).className = "o";
    }
    takeTurn()
}
