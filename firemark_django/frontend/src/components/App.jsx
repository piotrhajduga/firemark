import React, { Component } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Header from "./Header"
import GameLocation from "./GameLocation"


export default class App extends Component {
    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Container fluid>
            <Row><Col>
            <Header />
            </Col></Row>
            <Row><Col>
            <GameLocation />
            </Col></Row>
            </Container>
        );
    }
}