import React, { useState, useEffect } from "react";
import Cookies from "js-cookie";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Loader from "../Loader"
import GameLocation from "./GameLocation"


function requestGame(action) {
    const gameUrl = "/api/game/";

    if (action) {
        const csrftoken = Cookies.get('csrftoken');
        const request = {
            method: "PUT",
            headers: {
                "content-type":"application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify(action)
        };
        return fetch(gameUrl, request).then((response) => response.json());
    } else {
        return fetch(gameUrl).then((response) => response.json());
    }
}

export default function Game(props) {
    const [loading, setLoading] = useState(true);
    const [location, setLocation] = useState({});

    useEffect(() => {
        requestGame().then(setLocation).then(() => setLoading(false));
    }, []);

    async function handleAction(action) {
        setLoading(true);
        requestGame(action).then(setLocation).then(() => setLoading(false));
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