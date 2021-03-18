import React from "react";
import Form from "react-bootstrap/Form";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import CreatorLocationItem from "./CreatorLocationItem";

const defaultLocation = {
    codename: "",
    items: []
};

export default function CreatorLocation(props) {
    const onLocation = props.onLocation || (()=>{});
    const onSave = props.onSave || (()=>{});
    const location = Object.assign(defaultLocation, props.location);

    function addItem() {
        const update = Object.assign({}, location, {
            items: location.items.concat({})
        });
        onLocation(update);
    }

    function updateItem(key, data) {
        onLocation(Object.assign({}, location, {
            items: location.items.map((item, i)=>{
                return (key==i) ? data : item;
            })
        }));
    }

    function changeCodename(codename) {
        onLocation(Object.assign({}, location, {codename: codename}));
    }

    function save() {
        onSave(location);
    }

    const itemsList = location.items.map((item, i) => (
        <CreatorLocationItem key={i} item={item} onUpdate={(data)=>updateItem(i,data)} />
    ));

    return (
        <Container className="rounded bg-light text-dark p-5">
        <Row>
            <Form>
            <Form.Group controlId="codename" as={Row}>
            <Form.Label column sm="4">Codename</Form.Label>
            <Col sm="8">
            <Form.Control type="text" placeholder="Location codename" value={location.codename} onChange={e=>changeCodename(e.target.value)} />
            <Form.Text>If you live this blank the codename will be assigned automatically</Form.Text>
            </Col>
            </Form.Group>
            </Form>
        </Row>
        <Row className="mt-2">
            {itemsList}
        </Row>
        <Row>
            <Button block onClick={addItem} variant="outline-secondary">Add item</Button>
        </Row>
        <Row className="mt-3">
            <Button block onClick={save} variant="primary">Save location</Button>
        </Row>
        </Container>
    );
}