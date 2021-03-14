import React, { Component } from "react";
import Cookies from "js-cookie";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import Col from "react-bootstrap/Col";
import Spinner from "react-bootstrap/Spinner";
import GameLocationItem from "./GameLocationItem"


export default class GameLocation extends Component {
    gameUrl = "/api/game/";

    constructor(props) {
        super(props);

        this.state = {
            loading: true,
            codename: "",
            items: []
        };
    }

    updateStateWithData(data) {
        this.setState(Object.assign({loading: false}, data));
    }

    updateStateLoading() {
        this.setState({loading: true});
    }

    componentDidMount() {
        fetch(this.gameUrl)
        .then((response) => response.json())
        .then((data) => this.updateStateWithData(data));
    }

    handleAction(action) {
        this.updateStateLoading();
        const csrftoken = Cookies.get('csrftoken');
        const request = {
            method: "PUT",
            headers: {
                "content-type":"application/json",
                "X-CSRFToken": csrftoken
            },
            body: JSON.stringify(action)
        };
        fetch(this.gameUrl, request)
        .then((response) => response.json())
        .then((data) => this.updateStateWithData(data));
    }

    render() {
        let items;

        if (this.state.loading) {
            items = (
                <Row className="justify-content-center text-center"><Col md="10" lg="4">
                <Spinner className="mx-auto my-5" animation="border" role="status"></Spinner>
                </Col></Row>
            );
        } else {
            items = this.state.items.map((item) => (
                <Row className=" justify-content-center"><Col md="10" lg="4">
                <GameLocationItem key={item.codename} codename={item.codename} type={item.type} data={item.data} onAction={(action)=>this.handleAction(action)} />
                </Col></Row>
            ));
        }

        return (
            <Container fluid className="location pt-2">
            {items}
            </Container>
        );
    }
}