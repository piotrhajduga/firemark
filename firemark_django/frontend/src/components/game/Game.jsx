import React, { useState, useEffect } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Loader from "../Loader"
import GameLocation from "./GameLocation"
import apiCall from "~/utilities/api-call";


function callGameApi(action) {
    const gameUrl = "/api/game/";

    if (action) {
        return apiCall(gameUrl, "PUT", action).then((response) => response.json());
    } else {
        return apiCall(gameUrl).then((response) => response.json());
    }
}

export default function Game(props) {
    const [loading, setLoading] = useState(true);
    const [location, setLocation] = useState({});

    useEffect(() => {
        callGameApi().then(setLocation).then(() => setLoading(false));
    }, []);

    async function handleAction(action) {
        setLoading(true);
        callGameApi(action).then(setLocation).then(() => setLoading(false));
    }

    return (
        <Container fluid className="h-100 w-100 top-box">
        <Row className="h-100 w-100 pt-3 gx-2">
        <Col>
        <Loader loading={loading}>
        <GameLocation onAction={(action)=>handleAction(action)} location={location} />
        </Loader>
        </Col>
        </Row>
        </Container>
    );
}