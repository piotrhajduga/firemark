import React, { useState } from "react";
import Header from "./Header"
import Game from "./game/Game"
import Creator from "./creator/Creator"


export default function App(props) {
    const [mode, handleMode] = useState("creator");

    function renderMainContent() {
        switch(mode) {
            case "game": return <Game />;
            case "creator": return <Creator />;
            default: return <div/>;
        }
    }

    return (
        <div className="bg-dark text-light fixed-top w-100 h-100">
        <Header onMode={handleMode} />
        {renderMainContent()}
        </div>
    );
}