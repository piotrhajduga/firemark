import React from "react";
import GameLocationItem from "./GameLocationItem"
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";


export default function GameLocation(props) {
    const onAction = props.onAction || (()=>{});
    const location = props.location;

    const items = location.items.map((item) => (
        <Row className="vg-2"><GameLocationItem key={item.codename} id={item.id} type={item.type} data={item.data} onAction={(action)=>onAction(action)} /></Row>
    ));

    return (
        <Container className="rounded bg-light text-dark p-5">
        {items}
        </Container>
    );
}