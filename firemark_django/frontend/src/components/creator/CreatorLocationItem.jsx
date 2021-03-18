import React from "react";
import Form from "react-bootstrap/Form";
import Card from "react-bootstrap/Card";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Jumbotron from "react-bootstrap/Jumbotron";
import { SimpleTextCreator } from "../item-types/SimpleText";
import { SimpleExitCreator } from "../item-types/SimpleExit";

const typesMap = {
    "simple text": SimpleTextCreator,
    "simple exit": SimpleExitCreator
};

export default function CreatorLocationItem(props) {
    const onUpdate = props.onUpdate;
    const type = props.item.type || "";
    const config = props.item.config || {};

    function setType(newType) {
        onUpdate({type: newType, config: config});
    }
    function setConfig(newConfig) {
        onUpdate({type: type, config: newConfig});
    }

    const ItemComponent = typesMap[type] || Placeholder;

    return (
        <Card className="p-2 mb-2" style={{overflow: "hidden"}}>
            <Form className="mb-2">
            <Form.Group as={Row} className="pb-2 border-bottom shadow-bottom-3">
            <Form.Label column sm="4">Type</Form.Label>
            <Col sm="8">
            <Form.Control as="select" onChange={e=>setType(e.target.value)} value={type}>
                <option>Choose type...</option>
                {Object.keys(typesMap).map(item => <option value={item}>{item}</option>)}
            </Form.Control>
            </Col>
            </Form.Group>
            </Form>
            <ItemComponent config={config} onConfigChange={setConfig} />
        </Card>
    );
}

function Placeholder(props) {
    return <Jumbotron className="text-secondary text-center p-2">Choose item type from the dropdown above</Jumbotron>;
}