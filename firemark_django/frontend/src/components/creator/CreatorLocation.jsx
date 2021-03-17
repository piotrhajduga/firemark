import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import CreatorLocationItem from "./CreatorLocationItem";
import Cookies from "js-cookie";


function postLocationData(id, location) {
    let gameUrl;
    if (id) {
        gameUrl = `/api/locations/${id}/`;
    } else {
        gameUrl = "/api/locations/";
    }
    const csrftoken = Cookies.get('csrftoken');
    const request = {
        method: id?"PUT":"POST",
        headers: {
            "content-type":"application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({
            codename: location.codename,
            tags: "",
            public: true
        })
    };

    return fetch(gameUrl, request).then((response) => {
        console.log(response);
        return response.json();
    });
}

export default function CreatorLocation(props) {
    const [codename, setCodename] = useState(props.location.codename || "");
    const [items, setItems] = useState(props.location.items || []);
    const id = props.location.id;

    function updateItem(key, data) {
        setItems(oldItems=>oldItems.map((item, i)=>{
            return (key==i) ? data : item;
        }));
    }

    function save() {
        postLocationData(id, {codename: codename, items: items});
    }

    const itemsList = items.map((item, i) => (
        <CreatorLocationItem key={i} item={item} onUpdate={(data)=>updateItem(i,data)} />
    ));

    return (
        <Container className="rounded bg-light text-dark p-5">
        <Row>
            <Form>
            <Form.Group controlId="codename" as={Row}>
            <Form.Label column sm="4">Codename</Form.Label>
            <Col sm="8">
            <Form.Control type="text" placeholder="Location codename" defaultValue={codename} onChange={e=>setCodename(e.target.value)} />
            <Form.Text>If you live this blank the codename will be assigned automatically</Form.Text>
            </Col>
            </Form.Group>
            </Form>
        </Row>
        <Row className="mt-2">
            {itemsList}
        </Row>
        <Row>
            <Button block onClick={e=>setItems(oldItems=>{
                return oldItems.concat({});
            })} variant="outline-secondary">Add item</Button>
        </Row>
        <Row className="mt-3">
            <Button block onClick={save} variant="primary">Save location</Button>
        </Row>
        </Container>
    );
}