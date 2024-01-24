





function loadProduct() {
    //AJAX
    xhr = new XMLHttpRequest()
    xhr.open("GET", "/products")
    xhr.onload = function(){
        response = xhr.responseText
        data = JSON.parse(response)
        productContainer.innerHTML = `
            <h1>${data[0]['name']}</h1>
            <img src="${data[0]['image']}"/>
            <p>${data[0]['description']}</p>
        `
    }
    xhr.send()
}

loadProduct()