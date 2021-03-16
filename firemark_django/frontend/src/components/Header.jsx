import React, { useState, useEffect } from "react";
import Navbar from "react-bootstrap/Navbar";
import Nav from "react-bootstrap/Nav";
import Container from "react-bootstrap/Container";

export default function Header(props) {
    const [mode, handleMode] = useState("game");

    useEffect(()=>{
        props.onMode(mode);
    }, [mode]);

    return (
        <Container fluid>
        <Navbar variant="dark">
        <Navbar.Brand><h1 className="display-3">Firemark</h1></Navbar.Brand>
        <Navbar.Toggle aria-controls="header-navbar-nav" />
        <Navbar.Collapse id="header-navbar-nav" className="justify-content-end">
            <Nav activeKey={mode} onSelect={handleMode}>
                <Nav.Item><Nav.Link eventKey="game">Game</Nav.Link></Nav.Item>
                <Nav.Item><Nav.Link eventKey="creator">Creator</Nav.Link></Nav.Item>
            </Nav>
        </Navbar.Collapse>
        </Navbar>
        </Container>
    );
}