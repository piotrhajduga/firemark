import React, { Component } from "react";
import SimpleText from "./item-types/SimpleText";
import SimpleExit from "./item-types/SimpleExit";

const itemTypesMap = {
    "simple text": SimpleText,
    "simple exit": SimpleExit
};

export default class GameLocationItem extends Component {

    constructor(props) {
        super(props);
    }

    handleAction(actionData) {
        const action = {
            action_item: this.props.codename,
            action_data: JSON.stringify(actionData)
        };
        console.log(action);
        this.props.onAction(action);
    }

    render() {
        const ItemComponent = itemTypesMap[this.props.type];
        return <ItemComponent data={this.props.data} onAction={(actionData)=>this.handleAction(actionData)} />;
    }
}