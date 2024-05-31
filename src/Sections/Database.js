import React, { useState, useEffect } from 'react';
import { BrowserRouter as Router, useNavigate } from 'react-router-dom';
import axios from 'axios';

import {BASE_URL as baseUrl} from "../FIXED_FRONTEND_VARIABLES.js"
import { RenderDatabase } from '../Helpers/RenderDatabase.js';
import './../App.css'

import { HoverPopup } from '../Components/hover.js'



const ChessChallengesTable = ({ challenges, currentUserUplandID}) => {
    // const [acceptedChallenge, setAcceptedChallenges] = useState([]);
    const [cancelledChallenge, setCancelledChallenge] = useState(false);
    
    const [deletedChallege, setDeletedChallege] = useState(false);
    const [nothingRefunded, setNothingRefunded] = useState(false);
    const [processing, setProcessing] = useState(false);
    const [unableToDelete, setUnableToDelete] = useState(false);
    
    const [blankUplandID, setBlankUplandID] = useState(false);
    const [visitorError, setVisitorError] = useState(false);
    const [invalidBearerError, setInvalidBearerError] = useState(false);
    
    

    // useEffect(() => {
    //   // Store state variables in localStorage when component unmounts
      
    //   console.log("CHALLENGES: ", challenges)
      
    // }, [challenges]);

    const AcceptChallenge = async (link, index) => {
      if (currentUserUplandID === "BLANK") {
        setBlankUplandID(true)
        setTimeout(() => setBlankUplandID(false), 3000);
        return
      }
      
      try {
        const res = await axios.post(baseUrl + '/accepted', { link, currentUserUplandID});
        RenderDatabase();

        if (res.data === -1) {
          setVisitorError(true)
          setTimeout(() => setVisitorError(false), 5000);
          return
        } else if (res.data === -2) {
          setInvalidBearerError(true)
          setTimeout(() => setInvalidBearerError(false), 5000);
          return
        }

        window.open(link, '_blank');
        // setAcceptedChallenges([acceptedChallenge, index]);
      } catch (error) {
        console.error('Error:', error);
      }
    };
  
    const CancelChallenge = async (link, index) => {
      // const updatedAcceptedChallenges = acceptedChallenge.filter((acceptedIndex) => acceptedIndex !== index);
      
      try {
        await axios.post(baseUrl + '/cancel', { link });
        RenderDatabase();
        // setAcceptedChallenges(updatedAcceptedChallenges);

        setCancelledChallenge(true)
        setTimeout(() => setCancelledChallenge(false), 5000);
  
      } catch (error) {
        console.error('Error:', error);
      }
    };
  
    const DeleteChallenge = async (link) => {
      
      try {
        const res = await axios.post(baseUrl + '/delete', { link });
        RenderDatabase();

        if (res.data === 'Success') {
          setDeletedChallege(true)
          setTimeout(() => setDeletedChallege(false), 5000);
        } else if (res.data === "Nothing to refund") {
          setNothingRefunded(true)
          setTimeout(() => setNothingRefunded(false), 5000);
        } else if (res.data === "Processing") {
          setProcessing(true)
          setTimeout(() => setProcessing(false), 5000);
        } else if (res.data === "error") {
          setUnableToDelete(true)
          setTimeout(() => setUnableToDelete(false), 5000);
        }
  
      } catch (error) {
        console.error('Error:', error);
      }
    };


    // Go to different pages by the click of a button
    const navigate = useNavigate();

    const ViewEscrow = async (escrowId) => {
      navigate('/escrow', { state: {escrowId, currentUserUplandID} });
    };

    const ViewLichess = async (lichessId) => {
      navigate('/lichess', { state: {lichessId, currentUserUplandID} });
    };
  
    
    return (
      <>
        <table>
          <thead>
            <tr>
              <th>Challenge</th>
              <th>Upland ID</th>
              <th>Lichess ID</th>
              <th>Lichess Rating</th>
              <th>Wager</th>
              <th>Link</th>
              <th>Availability</th>
              <th>Accept Challenge</th>
              <th>Escrow Status</th>
            </tr>
          </thead>
  
          <tbody>
            {challenges.map((challenge, index) => (
              <tr key={index}> 
                <td> {challenge.name} </td>           
                
                {challenge.uplandID === -1 ? (
                  <td>
                    <HoverPopup text="**No UplandID associated w/ this Lichess account!** ">
                      <div className='textOutliner warning'>
                        N/A
                      </div>
                    </HoverPopup>
                  </td>
                ) : (
                  <td> {challenge.uplandID} </td>
                )}


                <td> 
                  <div 
                    onClick={() => ViewLichess(challenge.lichessID)}
                    className='textOutliner lichess'
                  >
                    {challenge.lichessID} 
                  </div>
                </td>


                <td> {challenge.opponentRating} </td>
                <td> {challenge.wageramt} </td>
  
                <td>
                  <a href={challenge.link} target="_blank" rel="noopener noreferrer">
                    ENTER GAME
                  </a>
                </td>
  
                <td >
                  {/* acceptedChallenge.includes(index) && */}
                  {(challenge.accepted === "YES") && (
                    <span className='textOutliner accepted'>
                      Accepted
                    </span>
                  )} 
                  
                  {(challenge.accepted === "NO") && (
                    <span className='textOutliner available'>
                      Available
                    </span>
                  )}

                  {(challenge.accepted === "COMPLETED") && (
                    <span className='textOutliner completed'>
                      COMPLETED
                    </span>
                  )}
                </td>
  
                <td>

                {/* {!acceptedChallenge.includes(index) && } */}
                  {challenge.accepted === "NO" && !(currentUserUplandID === challenge.uplandID) && !(challenge.uplandID === -1) && ( 
                    <button 
                      onClick={() => AcceptChallenge(challenge.link, index)}
                      className='acceptButton'
                    >
                      Accept
                    </button>
                  )}

                {/* !acceptedChallenge.includes(index) && */}
                  {challenge.accepted === "NO" && challenge.uplandID === currentUserUplandID &&(
                    <button
                      onClick={() => DeleteChallenge(challenge.link, challenge.accepted, index)}
                      className='deleteButton'
                    >
                      Delete
                    </button>
                  )}

                  {challenge.readyStatus === "NO" && challenge.accepted !== "NO" && challenge.uplandID === currentUserUplandID &&(
                    <button
                      onClick={() => DeleteChallenge(challenge.link, challenge.accepted, index)}
                      className='deleteButton'
                    >
                      Delete
                    </button>
                  )}
                  
                {/* acceptedChallenge.includes(index) ||  */}
                  {challenge.readyStatus === "NO" && (challenge.accepted === "YES") && (challenge.accepter === currentUserUplandID || challenge.uplandID === currentUserUplandID)  && (
                    <button
                      onClick={() => CancelChallenge(challenge.link, index)}
                      className='cancelButton'
                      style= {{marginTop: "5px"}}
                    >
                      Cancel
                    </button>
                  )}

                  {challenge.uplandID === -1 && (
                    <HoverPopup text="Once wager transactions on the escrow is confirmed on the EOS blockchain, it will be resolved">
                      <span className='textOutliner completed'>
                        COMPLETED
                      </span>
                    </HoverPopup>
                    
                  )}
                </td>


                <td> 
                    {challenge.readyStatus === "YES" && (
                      <button 
                        onClick={() => ViewEscrow(challenge.escrowId)}
                        className='textOutliner ready3'
                      >
                        GOOD TO GO
                      </button>
                    )}  
                    
                    {challenge.readyStatus === "NO" && (
                      <div 
                        onClick={() => ViewEscrow(challenge.escrowId)}
                        className='textOutliner ready2'
                      >
                        ESCROW NOT READY
                      </div>
                    )}

                    {challenge.readyStatus === "RESOLVING" && (
                      <div 
                        onClick={() => ViewEscrow(challenge.escrowId)}
                        className='textOutliner ready1'
                      >
                        RESOLVING
                      </div>
                    )}
                </td>
  
              </tr>
            ))} 
          </tbody>
        </table>
  
        {deletedChallege && (
          <div className={`notification notification-success`}>
            <div className="notification-content">
              Challenge Successfully Deleted & Escrow Refunded!
            </div>
          </div>
        )}

        {nothingRefunded && (
          <div className={`notification notification-success`}>
            <div className="notification-content">
              Challenge Successfully Deleted...but there was nothing in the escrow to refund
            </div>
          </div>
        )}

        {processing && (
          <div className={`notification notification-error`}>
            <div className="notification-content">
              Cannot delete...transactions are still processing
            </div>
          </div>
        )}

        {unableToDelete && (
          <div className={`notification notification-error`}>
            <div className="notification-content">
              Unknown Error
            </div>
          </div>
        )}

        {blankUplandID && (
          <div className={`notification notification-error`}>
            <div className="notification-content">
              Need to be logged in to accept!
            </div>
          </div>
        )}

        {visitorError && (
          <div className={`notification notification-error`}>
            <div className="notification-content">
              You are a visitor...need to be UPLANDER LEVEL AT LEAST to accept!
            </div>
          </div>
        )}
        

        {cancelledChallenge && (
          <div className={`notification notification-success`}>
            <div className="notification-content">
              Challenge Cancelled!
            </div>
          </div>
        )}

        {invalidBearerError && (
            <div className={`notification notification-error`}>
            BEARER TOKEN IS INVALID
            </div>
        )}

      </>
    );
  };  

export { ChessChallengesTable }