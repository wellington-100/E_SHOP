





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

        // store the product id into the container's attribute
        productContainer.setAttribute('data-product-id', data[0]["id"])
    }
    xhr.send()
}

function orderProduct(){
    let product_id = productContainer.getAttribute('data-product-id')
    xhr = new XMLHttpRequest()
    xhr.open("POST", `/orders/${product_id}`)
    xhr.onload = function() {
        console.log(xhr.responseText)
    }
    xhr.send()
}

loadProduct()