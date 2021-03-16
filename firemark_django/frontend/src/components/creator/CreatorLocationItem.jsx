import React, { useState, useEffect } from "react";
import Form from "react-bootstrap/Form";
import Card from "react-bootstrap/Card";
import { SimpleTextCreator } from "../item-types/SimpleText";
import { SimpleExitCreator } from "../item-types/SimpleExit";

function Placeholder(props) {
    return <div/>;
}

const itemTypesMap = {
    "simple text": SimpleTextCreator,
    "simple exit": SimpleExitCreator
};

export default function CreatorLocationItem(props) {
    const [itemType, setItemType] = useState(props.item.type || "");

    useEffect(()=>{
        console.log(itemType);
    }, [itemType]);

    const ItemComponent = itemTypesMap[itemType] || Placeholder;

    return (
        <Card className="p-2 mb-2">
            <Form className="mb-2">
            <Form.Row>
            <Form.Group>
            <Form.Label>Type</Form.Label>
            <Form.Control as="select" onChange={e=>setItemType(e.target.value)}>
                <option>Choose type...</option>
                {Object.keys(itemTypesMap).map(item => <option value={item}>{item}</option>)}
            </Form.Control>
            </Form.Group>
            </Form.Row>
            </Form>
            <ItemComponent item={props.item} />
        </Card>
    );
}