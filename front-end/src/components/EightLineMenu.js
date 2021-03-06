import React from 'react';
import '../index.css';

function EightLineMenu(props) {
    return (
        <div>
            <select class="custom-select" id="ominoe-select" onChange={props.setOminoeTypes} value={props.ominoe_id}>
                <option value=""></option>
                <option value="pent-non">Pentominoes (non-unique)</option>
                <option value="tetr-pent-unq">Tetronimoes and Pentominoes (both unique)</option>
                <option value="tetr-pent-non">Tetronimoes and Pentominoes (both non-unique)</option>
                <option value="tetr-unq-pent-non">Tetronimoes (unique) and Pentominoes (non-unique)</option>
                <option value="tetr-non-pent-unq">Tetronimoes (non-unique) and Pentominoes (unique)</option>
                <option value="pent-hex-non">Pentominoes and Hexominoes (both non-unique)</option>
            </select>
            <button class="button" onClick={props.readyToTile}>Ready To Tile</button>
        </div>
    );
}

export default EightLineMenu;