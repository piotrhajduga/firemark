import React, { Component } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";


export default class Header extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Container fluid className="mb-2 py-1">
            <Row><Col>
            <h1>Firemark</h1>
            </Col></Row>
            </Container>
        );
    }
}