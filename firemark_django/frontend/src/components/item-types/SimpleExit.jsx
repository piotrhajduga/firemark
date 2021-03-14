import React, { Component } from "react";
import Button from "react-bootstrap/Button";


export default class SimpleText extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return (
            <Button onClick={(e)=>this.handleClick(e)}>{ this.props.data.label }</Button>
        );
    }

    handleClick(e) {
        e.preventDefault();
        this.props.onAction({});
    }
}