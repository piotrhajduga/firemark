import React, { useState } from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import ButtonGroup from "react-bootstrap/ButtonGroup";
import Button from "react-bootstrap/Button";
import CreatorLocation from "./CreatorLocation";
import ChooseLocationModal from "./ChooseLocationModal";
import Cookies from "js-cookie";


function postLocationData(location) {
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
        body: JSON.stringify(location)
    };

    return new Promise((resolve, reject) => {
        fetch(gameUrl, request).then((response) => {
            if (response.ok) {
                resolve(response.json());
            } else {
                reject(response.json());
            }
        });
    });
}

function deleteLocation(id) {
    let gameUrl = `/api/locations/${id}/`;
    const csrftoken = Cookies.get('csrftoken');
    const request = {
        method: location.id?"PUT":"POST",
        headers: {
            "content-type":"application/json",
            "X-CSRFToken": csrftoken
        }
    };

    return new Promise((resolve, reject) => {
        fetch(gameUrl, request).then((response) => {
            if (response.ok) {
                resolve();
            } else {
                reject();
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

    const addLocationButtonPlaceholder = (
        <Button onClick={newLocation} variant="outline-light" className="w-100" size="lg">Add location</Button>
    );

    return (
        <Container fluid className="h-100 w-100">
        <Row className="pt-3 gx-2">
        <Col>
        {location===null?addLocationButtonPlaceholder:<CreatorLocation location={location} onLocation={onTargetLocation} onSave={onSaveLocation} />}
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