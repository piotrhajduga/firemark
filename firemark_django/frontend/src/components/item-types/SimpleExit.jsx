import React from "react";
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
    const label = props.config.label || "";
    const destination = props.config.destination || "";

    function changeLabel(newLabel) {
        onConfigChange({label:newLabel, destination:destination});
    }

    function changeDestination(newDestination) {
        onConfigChange({label:label, destination:newDestination});
    }

    return (
        <Form>
        <Form.Group as={Row} className="mb-2">
        <Form.Label column sm="4">Label</Form.Label>
        <Col sm="8">
        <Form.Control type="text" placeholder="Label" onChange={e=>changeLabel(e.target.value)} value={label} />
        </Col>
        </Form.Group>
        <CreatorLocationExit destination={destination} onDestination={changeDestination}/>
        </Form>
    );
}