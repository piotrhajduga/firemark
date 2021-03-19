import React, { useState, useEffect } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import ListGroup from "react-bootstrap/ListGroup";
import Loader from "../Loader";
import apiCall from "~/utilities/api-call";


function requestLocations(search) {
    const url = "/api/locations/";
    return apiCall(url).then((response) => response.json());
}

export default function ChooseLocationModal(props) {
    const [loading, setLoading] = useState(true);
    const [locations, setLocations] = useState([]);
    const [chosen, setChosen] = useState(null);
    const onLocation = props.onLocation;

    useEffect(()=>{
        if (props.show) {
            requestLocations().then(setLocations).then(()=>setLoading(false));
        }
    },[props.show]);

    const locationsList = locations.map(location=>{
        if (chosen && chosen.id==location.id) {
            return (
            <ListGroup.Item action active>{location.codename}</ListGroup.Item>
            );
        } else {
            return (
            <ListGroup.Item action onClick={()=>setChosen(location)}>{location.codename}</ListGroup.Item>
            );
        }
    });

    function submit() {
        onLocation(chosen);
    }

    function cancel() {
        onLocation(null);
    }

    return (
    <Modal show={props.show} backdrop="static" centered>
        <Modal.Header>{props.title}</Modal.Header>
        <Modal.Body>
            <Loader loading={loading}>
                <ListGroup>{locationsList}</ListGroup>
            </Loader>
        </Modal.Body>
        <Modal.Footer>
            <Button onClick={submit}>OK</Button>
            <Button variant="secondary" onClick={cancel}>Cancel</Button>
        </Modal.Footer>
    </Modal>
    );
}