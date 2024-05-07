import React, { useState} from 'react';
import './../App.css'


const ToggleBar = () => {
    const [infosection, setInfoSection] = useState(false);
    
    const toggleInfoSection = () => setInfoSection(!infosection);
    
    return (
        <div className={"toggleInfoSection"} onClick={toggleInfoSection}>
            {!infosection ? (
                <div className="toggleText">
                <span >
                    CLICK FOR IMPORTANT INFO!!
                </span>
                <span className="close">⬇️</span>
                </div>
            ) :
                <div>
                <span className="close">⬆️</span>
                
                <span className="warning">**</span>
                If your chess challenge expires, HIT DELETE and it will be removed from the list and you'll be refunded
                <span className="warning">**</span>
                <br />
                <span className="warning">WARNING:</span>
                If you confirmed through Upland you want to accept a challenge, even if you CANCEL, you won't get your money back!!
                <br />
                <br />
                <span className="important">Important:</span>
                <br />
                YOU MUST HAVE A LICHESS ACCOUNT!
                <br />
                CHALLENGE MUST BE MARKED AS "ACCEPTED" & NOT "AVAILABLE" IN ORDER FOR WAGERS TO BE RESOLVED
                </div>
            }
        </div>
    )   
};  

export {ToggleBar}