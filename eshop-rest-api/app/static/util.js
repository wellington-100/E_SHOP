





function updateAPI(method, url, payload, cb) {

    
    let xhr = new XMLHttpRequest()
    xhr.open(method, url)
    xhr.setRequestHeader('Content-type', 'application/json')
    xhr.onload = function (){
        let data
        if(xhr.responseText){
            data = JSON.parse(xhr.responseText)
        } else {
            data = null
        }
        cb(data, xhr)

    }
    xhr.send(
        JSON.stringify(payload)
    )
}     

