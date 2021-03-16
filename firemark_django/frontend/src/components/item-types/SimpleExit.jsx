import React, { useState } from "react";
import Button from "react-bootstrap/Button";
import Form from "react-bootstrap/Form";


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
    return (
        <Form>
        <Form.Control type="text" placeholder="Label">{props.item.label}</Form.Control>
        </Form>
    );
}