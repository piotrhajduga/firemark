import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Button from "react-bootstrap/Button";
import CreatorLocation from "./CreatorLocation";
import ChooseLocationModal from "./ChooseLocationModal";
import Cookies from "js-cookie";


function postLocationData(location) {
    console.log(location);
    let gameUrl;
    if (location.id) {
        gameUrl = `/api/locations/${location.id}/`;
    } else {
        gameUrl = "/api/locations/";
    }
    const csrftoken = Cookies.get('csrftoken');
    const request = {
        method: location.id?"PUT":"POST",
        headers: {
            "content-type":"application/json",
            "X-CSRFToken": csrftoken
        },
        body: JSON.stringify({
            codename: location.codename,
            tags: "",
            public: true
        })
    };

    return fetch(gameUrl, request).then((response) => {
        console.log(response);
        return response.json();
    });
}


export default function Creator(props) {
    const [location, setLocation] = useState(null);
    const [chooseLocation,setChooseLocation] = useState(false);

    function onTargetLocation(target) {
        setLocation(target);
        setChooseLocation(false);
    }

    function onSaveLocation(target) {
        postLocationData(target).then(()=>{
            setLocation(target);
        });
    }

    const addLocationButtonPlaceholder = (
        <Button onClick={(e)=>setLocation({})} variant="outline-light" className="w-100" size="lg">Add location</Button>
    );

    return (
        <Container fluid className="h-100 w-100">
        <Row className="pt-3 gx-2">
        <Col>
        {location===null?addLocationButtonPlaceholder:<CreatorLocation location={location} onLocation={onTargetLocation} onSave={onSaveLocation} />}
        </Col>
        <Col xs={4} md={3} lg={2}>
            <Button className="w-100" onClick={(e)=>setLocation({})}>Add location</Button>
            <Button className="w-100" onClick={(e)=>setChooseLocation(true)}>Edit location</Button>
        </Col>
        </Row>
        <ChooseLocationModal show={chooseLocation} onLocation={onTargetLocation} title="Choose location" />
        </Container>
    );
}