import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'
import HoverPopup from './hover.js'

const ChessChallengesTable = ({ challenges, currentUserUplandID}) => {
    const [acceptedChallenge, setAcceptedChallenges] = useState([]);
    const [successfullyDeleted, setsuccessfullyDeleted] = useState(false);
    const [blankUplandID, setBlankUplandID] = useState(false);
    
    const AcceptChallenge = async (UplandID, link, index) => {
      if (currentUserUplandID == "BLANK") {
        setBlankUplandID(true)
        setTimeout(() => setBlankUplandID(false), 3000);
        return
      }
      
      window.open(link, '_blank');
      
      try {
        await axios.post('/accepted', {
          link,
          currentUserUplandID,
          UplandID
        });
  
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
  
      } catch (error) {
        console.error('Error:', error);
      }
    };
  
    const DeleteChallenge = async (link, accepted) => {
      try {
        const res = await axios.post('/delete', { link });
        
        if (res.data == 'Success') {
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
                
                {challenge.uplandID == -1 ? (
                  <td>
                    <HoverPopup text="**No UplandID associated w/ this Lichess account!** ">
                      <button style={{ backgroundColor: '#dc143c', color: 'white', padding: '5px', borderRadius: '3px', border: 'none' }}>
                        N/A
                      </button>
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
  
                <td>
                  {(acceptedChallenge.includes(index) || challenge.accepted) ? (
                    <span style={{ display: 'inline-block', backgroundColor: 'Purple', color: 'white'}}>
                      Accepted
                    </span>
                  ) : (
                    <span style={{ display: 'inline-block', backgroundColor: '#00ffff', color: '#000000'}}>
                      Available
                    </span>
                  )}
                </td>
  
                <td>
                  {!acceptedChallenge.includes(index) && !challenge.accepted && !(currentUserUplandID === challenge.uplandID) && (
                    <button
                      onClick={() => AcceptChallenge(challenge.uplandID, challenge.link, index)}
                      style={{backgroundColor: '#a52a2a'}}
                    >
                      Accept
                    </button>
                  )}
  
                  {!acceptedChallenge.includes(index) && !challenge.accepted && challenge.uplandID === currentUserUplandID && (
                    <button
                      onClick={() => DeleteChallenge(challenge.link, challenge.accepted, index)}
                      style={{backgroundColor: 'red'}}
                    >
                      Delete
                    </button>
                  )}
  
                  {(acceptedChallenge.includes(index) || challenge.accepted) && challenge.accepter === currentUserUplandID && (
                    <button
                      onClick={() => CancelChallenge(challenge.link, index)}
                      style={{backgroundColor: '#3498db'}}
                    >
                      Cancel
                    </button>
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
      </>
    );
  };  

export default ChessChallengesTable