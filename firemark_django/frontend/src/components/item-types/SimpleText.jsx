import React, { useState, useEffect } from "react";
import Form from "react-bootstrap/Form";
import ReactMarkdown from 'react-markdown'


export function SimpleText(props) {
    return <ReactMarkdown>{ props.data.content }</ReactMarkdown>;
}

export function SimpleTextCreator(props) {
    const onConfigChange = props.onConfigChange;
    const [content, setContent] = useState(props.config.content || "");

    useEffect(()=>onConfigChange({content:content}),[content]);

    return (
        <Form>
        <Form.Group>
        <Form.Label>Content</Form.Label>
        <Form.Control as="textarea" onChange={e=>setContent(e.target.value)}>{content}</Form.Control>
        </Form.Group>
        </Form>
    );
}