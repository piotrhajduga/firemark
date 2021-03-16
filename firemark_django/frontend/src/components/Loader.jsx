import React from "react";
import Spinner from "react-bootstrap/Spinner";


export default function Loader(props) {
    const style = props.style || {width: "4rem", height: "4rem"};
    const loader = (
        <div className="w-100 h-100 d-flex align-items-center position-absolute top-0 left-0">
        <Spinner className="mx-auto" animation="border" role="status" style={style}>
        <span className="visually-hidden">Loading...</span>
        </Spinner>
        </div>
    );

    if (props.loading) {
        return loader;
    } else {
        return props.children || loader;
    }
}