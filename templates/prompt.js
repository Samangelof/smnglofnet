async function getData() {
    let response = await fetch(
        "http://127.0.0.1:4041/api/v5/posts/",{
            method: "GET",
            headers: {
                "Content-Type": "application/json"
            }
        }
    )
    .then(res => res.json())
    .then(data => {
        console.log(data);
    })
    .catch(err => {
        console.log(err);
    })
}

getData()