import React, { useState, useEffect } from 'react';
import './App.css'
import ChessChallengesTable from './Database.js'
import { ChallengeDatabase } from './functions.js';
import { UserSection } from './Login.js'; // Import UserSection from Login component
import { SubmitChallenge } from './SubmitChallenge.js';

const MainPage = () => {
  const [challengeData, setChallengesData] = useState([]);
  const [finalUserUplandID, setFinalUserUplandID] = useState('BLANK'); // Lift state up


  useEffect(() => {
    resetChallenges();
  }, [finalUserUplandID]); // Watch for changes in finalUserUplandID only

  const resetChallenges = async () => {
    const challengeTableData = await ChallengeDatabase();
    setChallengesData(challengeTableData);
  };

  return (
    <>
      <header>
        <div>
          <h2 className="title">UPLAND CHESS</h2>
        </div>
        <div className="author-info">by dogeyboy19</div>
        <br/>

        <div className="contentSection">
          <span className="warning">**</span>
          If your chess challenge expires, HIT DELETE and it will be removed from the list and you'll be refunded
          <span className="warning">**</span>
          <br />
          <span className="warning">WARNING:</span>
          If you confirmed through Upland you want to accept a challenge, even if you CANCEL, you won't get your money back!!
          <br />
          <span className="important">Important:</span>
          YOU MUST HAVE A LICHESS ACCOUNT!
          <br />
        </div>
      </header>


      <UserSection setFinalUserUplandID={setFinalUserUplandID} setChallengesData={setChallengesData}/> {/* Pass setFinalUserUplandID as prop */}

      <ChessChallengesTable challenges={challengeData} currentUserUplandID={finalUserUplandID}/>

      <SubmitChallenge finalUserUplandID={finalUserUplandID}/>
    </>
  );
};

export default MainPage;



/*
      <div style={{ marginTop: '100px', marginLeft: '20px'}}>
        <a href="https://reactnative.dev/docs/colors" > 
          Colors 
        </a>
      </div>

      <div style={{ marginTop: '20px', marginLeft: '20px'}}>
        <a href="https://www.w3.org/Style/Examples/007/fonts.en.html" > 
          Fonts 
        </a>
      </div>
*/