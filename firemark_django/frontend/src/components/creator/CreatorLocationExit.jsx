import React, { useState, useEffect } from "react";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import ChooseLocationModal from "./ChooseLocationModal";


export default function CreatorLocationExit(props) {
    const [chooseLocation,setChooseLocation] = useState(false);
    const [destination,setDestination] = useState(props.destination);
    const onDestination = props.onDestination;

    useEffect(() => {onDestination({destination: destination})}, [destination]);

    let destinationSpan;
    if (destination) {
        destinationSpan = <span className="mx-auto text-success">{destination}</span>;
    } else {
        destinationSpan = <span className="mx-auto text-danger">no location chosen</span>;
    }

    function onTargetLocation(location) {
        setDestination(location);
        setChooseLocation(false);
    }

    return (
        <Row>
        <Col sm="8" className="d-flex align-items-center text-center">
            {destinationSpan}
        </Col>
        <Col sm="4">
            <Button block className="w-100" onClick={()=>setChooseLocation(true)}>Change</Button>
        </Col>
        <ChooseLocationModal show={chooseLocation} onLocation={onTargetLocation} title="Choose exit location" />
        </Row>
    );
}