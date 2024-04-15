import React, { useState} from 'react';
import axios from 'axios';

import HoverPopup from '../Components/hover.js'
import './../App.css'


const ChessChallengesTable = ({ challenges, currentUserUplandID}) => {
    const [acceptedChallenge, setAcceptedChallenges] = useState([]);
    
    const [successfullyDeleted, setsuccessfullyDeleted] = useState(false);
    const [challengeCancelled, setChallengeCancelled] = useState(false);
    const [blankUplandID, setBlankUplandID] = useState(false);
    const [visitorError, setVisitorError] = useState(false);
    
    const AcceptChallenge = async (UplandID, link, index) => {
      if (currentUserUplandID === "BLANK") {
        setBlankUplandID(true)
        setTimeout(() => setBlankUplandID(false), 3000);
        return
      }
      
      try {
        const res = await axios.post('/accepted', {
          link,
          currentUserUplandID,
          UplandID
        });

        if (res.data === -1) {
          setVisitorError(true)
          setTimeout(() => setVisitorError(false), 5000);
          return
        }

        window.open(link, '_blank');
        setAcceptedChallenges([acceptedChallenge, index]);
      } catch (error) {
        console.error('Error:', error);
      }
    };
  
    const CancelChallenge = async (link, index) => {
      const updatedAcceptedChallenges = acceptedChallenge.filter((acceptedIndex) => acceptedIndex !== index);
      
      try {
        await axios.post('/cancel', { link });
        setAcceptedChallenges(updatedAcceptedChallenges);

        setChallengeCancelled(true)
        setTimeout(() => setChallengeCancelled(false), 5000);
  
      } catch (error) {
        console.error('Error:', error);
      }
    };
  
    const DeleteChallenge = async (link, accepted) => {
      try {
        const res = await axios.post('/delete', { link });
        
        if (res.data === 'Success') {
          setsuccessfullyDeleted(true)
          setTimeout(() => setsuccessfullyDeleted(false), 5000);
        } 
  
      } catch (error) {
        console.error('Error:', error);
      }
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
  
                <td> {challenge.lichessID} </td>
                <td> {challenge.opponentRating} </td>
                <td> {challenge.wageramt} </td>
  
                <td>
                  <a href={challenge.link} target="_blank" rel="noopener noreferrer">
                    {challenge.link}
                  </a>
                </td>
  
                <td >
                  {(acceptedChallenge.includes(index) && challenge.accepted) ? (
                    <span className='textOutliner accepted'>
                      Accepted
                    </span>
                  ) : (
                    <span className='textOutliner available'>
                      Available
                    </span>
                  )}
                </td>
  
                <td>
                  {!acceptedChallenge.includes(index) && !challenge.accepted && !(currentUserUplandID === challenge.uplandID) && !(challenge.uplandID === -1) && (
                    <button 
                      onClick={() => AcceptChallenge(challenge.uplandID, challenge.link, index)}
                      className='acceptButton'
                    >
                      Accept
                    </button>
                  )}
  
                  {!acceptedChallenge.includes(index) && !challenge.accepted && challenge.uplandID === currentUserUplandID && (
                    <button
                      onClick={() => DeleteChallenge(challenge.link, challenge.accepted, index)}
                      className='deleteButton'
                    >
                      Delete
                    </button>
                  )}
  
                  {(acceptedChallenge.includes(index) || challenge.accepted) && challenge.accepter === currentUserUplandID && (
                    <button
                      onClick={() => CancelChallenge(challenge.link, index)}
                      className='cancelButton'
                    >
                      Cancel
                    </button>
                  )}

                  {challenge.uplandID === -1 && (
                    <div className='textOutliner warning'>
                      Invalid
                    </div>
                  )}
                </td>
  
              </tr>
            ))} 
          </tbody>
        </table>
  
        {successfullyDeleted && (
          <div className={`notification notification-success`}>
            <div className="notification-content">
              Challenge Successfully Deleted & Escrow Refunded!
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

        {challengeCancelled && (
          <div className={`notification notification-success`}>
            <div className="notification-content">
              Challenge Cancelled!
            </div>
          </div>
        )}
      </>
    );
  };  

export default ChessChallengesTable 