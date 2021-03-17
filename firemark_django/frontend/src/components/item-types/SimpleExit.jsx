import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import CreatorLocationExit from "../creator/CreatorLocationExit";


export function SimpleExit(props) {
    function handleClick(e) {
        e.preventDefault();
        props.onAction({});
    }

    return (
        <Button onClick={handleClick}>{ props.data.label }</Button>
    );
}

export function SimpleExitCreator(props) {
    const onConfigChange = props.onConfigChange;
    const [label, setLabel] = useState(props.config.label);
    const [destination, setDestination] = useState(null);

    useEffect(
        ()=>onConfigChange({label:label, destination:destination}),
        [label, destination]
    );

    return (
        <Form>
        <Form.Group as={Row} className="mb-2">
        <Form.Label column sm="4">Label</Form.Label>
        <Col sm="8">
        <Form.Control type="text" placeholder="Label" onChange={e=>setLabel(e.target.value)} value={label} />
        </Col>
        </Form.Group>
        <CreatorLocationExit destination={destination} onDestination={setDestination}/>
        </Form>
    );
}