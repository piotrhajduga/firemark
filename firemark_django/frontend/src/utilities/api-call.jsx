import Cookies from "js-cookie";

export default function apiCall(url, method="GET", data=null) {
    switch (method) {
    case "GET":
        return fetch(url);
    case "PUT":
    case "POST":
    case "PATCH":
    case "DELETE":
        const csrftoken = Cookies.get('csrftoken');
        let request = {
            method: method,
            mode: "same-origin",
            headers: {
                "content-type":"application/json",
                "X-CSRFToken": csrftoken
            },
            body: (method != "DELETE") ? JSON.stringify(data) : null
        };
        return fetch(url, request);
    }
    throw Error(`Invalid http method: ${method}`);
}