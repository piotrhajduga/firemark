import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import CreatorLocation from "./CreatorLocation";

export default function Creator(props) {
    const [location, setLocation] = useState(null);

    const addLocationButtonPlaceholder = (
        <Button onClick={(e)=>setLocation({})} variant="outline-light" className="w-100" size="lg">Add location</Button>
    );

    return (
        <Container fluid className="h-100 w-100 top-box">
        <Row className="pt-3 gx-2">
        <Col>
        {location===null?addLocationButtonPlaceholder:<CreatorLocation location={location}/>}
        </Col>
        <Col xs={4} md={3} lg={2}>
            <Button className="w-100" onClick={(e)=>setLocation({})}>Add location</Button>
        </Col>
        </Row>
        </Container>
    );
}