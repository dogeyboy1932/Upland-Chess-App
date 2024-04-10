import React, { useState } from 'react';
import axios from 'axios';
import './../App.css'




const submitDetails = async (rated, wager, upland) => {
    try {
      const response = await axios.post('/submit-details', {
        rated, 
        wager,
        upland
      });
      
      return response.data
    } catch (error) {
      console.error('Error:', error);
    }
};

const SubmitChallenge = ({finalUserUplandID}) => {
    const [isChallengeOpen, setChallengeOpen] = useState(false);
    
    const [needLogin, setNeedLogin] = useState(false)
    const [challengeSubmitted, setChallengeSubmitted] = useState(false);
    const [challengeError, setChallengeError] = useState("-1");
    const [visitorError, setVisitorError] = useState(false);
    
    const [rated, setRated] = useState('');
    const [wager, setWager] = useState('');
    

    const handleChallengeSubmit = async () => {
        const res = await submitDetails(rated, wager, finalUserUplandID);
        // console.log(res)
        
        if (res === 1) {
          setChallengeSubmitted(true);
          setTimeout(() => setChallengeSubmitted(false), 5000);
          closeChallengeModal();
        } else if (res === -1 || res === -2 || res === -3 || res === -4) {
          setChallengeError(res);
          setTimeout(() => setChallengeError(1), 5000);
        } else if (res === -5) {
          setVisitorError(true);
          setTimeout(() => setVisitorError(false), 5000);
        }
    }; 

    const openChallengeModal = () => {
        if (finalUserUplandID === "BLANK") {
          setNeedLogin(true)
          setTimeout(() => setNeedLogin(false), 3000);
          return 
        }
        setChallengeOpen(true);
    };

    const closeChallengeModal = () => {
        setChallengeOpen(false);
    };

    return (
        <div className='createChallengeSection'>
            <button onClick={openChallengeModal} className='createChallengeButton'> 
            CREATE CHALLENGE 
            </button>

            <div>
            {isChallengeOpen && (
                <div className='modal modalChallenge'>
                <span className="close" onClick={closeChallengeModal}> &times; </span>
                <h2>Enter Your Challenge Details! </h2>
                
                <label htmlFor="name">Rated? </label>
                <input type="text" id="name" value={rated} onChange={(e) => setRated(e.target.value)} />
                <br />
                
                <label htmlFor="name">Wager? </label>
                <input type="text" id="wager" value={wager} className='user-input' onChange={(e) => setWager(e.target.value)} />
                <br />
                
                <button onClick={handleChallengeSubmit} className='submitButton'>Submit</button>
                </div>
            )}
            </div>

            {needLogin && (
                <div className={`notification notification-error`}>
                Need to be logged in!
                </div>
            )}
            
            {challengeSubmitted && (
                <div className={`notification notification-success`}>
                Challenge Submitted!!
                </div>
            )}

            {challengeError === -1 && (
                <div className={`notification notification-error`}>
                <div >
                    Invalid Upland ID...
                </div>
                </div>
            )}

            {challengeError === -2 && (
                <div className={`notification notification-error`}>
                Invalid Rating...
                </div>
            )}

            {challengeError === -3 && (
                <div className={`notification notification-error`}>
                Invalid Wager...
                </div>
            )}

            {challengeError === -4 && (
                <div className={`notification notification-error`}>
                Sorry, but the amount you wagered exceeds your balance!
                </div>
            )}

            {visitorError && (
                <div className={`notification notification-error`}>
                YOUR LEVEL IS VISITOR! HAVE TO BE AT LEAST AN "UPLANDER" TO CREATE A CHALLENGE!
                </div>
            )}
        </div> 
    )
}

export {SubmitChallenge}
