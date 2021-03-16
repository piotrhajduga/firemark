import React, { useState } from "react";
import Form from "react-bootstrap/Form";


export function SimpleText(props) {
    return <p>{ props.data.content }</p>;
}

export function SimpleTextCreator(props) {
    return (
        <Form>
        <Form.Label>Content</Form.Label>
        <Form.Control as="textarea">{props.item.content}</Form.Control>
        </Form>
    );
}