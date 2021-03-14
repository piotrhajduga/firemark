import React, { Component } from "react";


export default class SimpleText extends Component {

    constructor(props) {
        super(props);
    }

    render() {
        return <p>{ this.props.data.content }</p>;
    }
}