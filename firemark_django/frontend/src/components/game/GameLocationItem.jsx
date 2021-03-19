import React from "react";
import { SimpleText } from "../item-types/SimpleText";
import { SimpleExit } from "../item-types/SimpleExit";

const itemTypesMap = {
    "simple text": SimpleText,
    "simple exit": SimpleExit
};

export default function GameLocationItem(props) {

    function handleAction(actionData) {
        const action = {
            action_item: props.id,
            action_data: JSON.stringify(actionData)
        };
        props.onAction(action);
    }

    const ItemComponent = itemTypesMap[props.type];
    return <ItemComponent data={props.data} onAction={(actionData)=>handleAction(actionData)} />;
}