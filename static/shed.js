cab = document.getElementsByClassName('cab')


function clean_cabs(){
    for (i = 0; i < cab.length; i++) {
        if (cab[i].innerText == '') {
            cab[i].parentElement.remove()
        }
    }
}


[1, 2, 3, 4, 5, 6].forEach(clean_cabs)