import React, { useState } from "react";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Button from "react-bootstrap/Button";
import CreatorLocationItem from "./CreatorLocationItem";


export default function CreatorLocation(props) {
    const [codename, setCodename] = useState(props.location.codename || "");
    const [items, setItems] = useState(props.location.items || []);

    const itemsList = items.map((item, i) => (
        <CreatorLocationItem key={i} item={item} />
    ));

    return (
        <Container className="rounded bg-light text-dark p-5">
        <Row>
            <Form>
            <Form.Group controlId="locationCodename">
            <Form.Label>Codename</Form.Label>
            <Form.Control type="text" placeholder="Location codename" defaultValue={codename} onChange={e=>setCodename(e.target.value)} />
            <Form.Text>If you live this blank the codename will be assigned automatically</Form.Text>
            </Form.Group>
            </Form>
        </Row>
        <Row className="mt-2">
            {itemsList}
        </Row>
        <Row>
            <Button block onClick={e=>setItems(oldItems=>{
                return [{}].concat(oldItems);
            })}>Add item</Button>
        </Row>
        </Container>
    );
}