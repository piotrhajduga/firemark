import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Button from "react-bootstrap/Button";
import CreatorLocation from "./CreatorLocation";
import ChooseLocationModal from "./ChooseLocationModal";
import apiCall from "~/utilities/api-call";


function postLocationData(location) {
    let url;
    if (location.id) {
        url = `/api/locations/${location.id}/`;
    } else {
        url = "/api/locations/";
    }

    return new Promise((resolve, reject) => {
        apiCall(url, location.id?"PUT":"POST", location).then((response) => {
            if (response.ok) {
                resolve(response.json());
            } else {
                reject(response.json());
            }
        });
    });
}

const emptyLocation = {
    codename: "",
    tags: "",
    public: false,
    items: []
};

export default function Creator(props) {
    const [location, setLocation] = useState(null);
    const [chooseLocation,setChooseLocation] = useState(false);

    function newLocation() {
        setLocation(emptyLocation);
    }

    function onTargetLocation(target) {
        setChooseLocation(false);
        setLocation(target);
    }

    function onSaveLocation(target) {
        console.log(target);
        postLocationData(target).then((data)=>{
            setLocation(data);
        });
    }

    return (
        <Container fluid className="h-100 w-100">
        <Row className="pt-3 gx-2">
        <Col>
        {location===null?null:<CreatorLocation location={location} onLocation={onTargetLocation} onSave={onSaveLocation} />}
        </Col>
        <Col xs={4} md={3} lg={2}>
            <ButtonGroup vertical className="w-100">
                <Button className="w-100" onClick={newLocation}>Add location</Button>
                <Button className="w-100" onClick={(e)=>setChooseLocation(true)}>Edit location</Button>
            </ButtonGroup>
        </Col>
        </Row>
        <ChooseLocationModal show={chooseLocation} onLocation={onTargetLocation} title="Choose location" />
        </Container>
    );
}