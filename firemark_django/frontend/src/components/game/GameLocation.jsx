import React from "react";
import GameLocationItem from "./GameLocationItem"


export default function GameLocation(props) {
    const onAction = props.onAction || (action=>{});
    const location = props.location;

    const items = location.items.map((item) => (
        <GameLocationItem key={item.codename} codename={item.codename} type={item.type} data={item.data} onAction={(action)=>onAction(action)} />
    ));

    return (
        <div className="rounded bg-light text-dark p-5">
        {items}
        </div>
    );
}