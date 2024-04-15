import React, { useState, useEffect } from 'react';
import './App.css'
import ChessChallengesTable from './Sections/Database.js'
import { RenderDatabase } from './Helpers/functions.js';
import { UserSection } from './Sections/Login.js'; // Import UserSection from Login component
import { SubmitChallenge } from './Sections/SubmitChallenge.js';

const MainPage = () => {
  const [challengeData, setChallengesData] = useState([]);
  const [finalUserUplandID, setFinalUserUplandID] = useState('BLANK'); // Lift state up

  const [infosection, setInfoSection] = useState(false);

  useEffect(() => {
    resetChallenges();
  }, [finalUserUplandID]); // Watch for changes in finalUserUplandID only

  const resetChallenges = async () => {
    const challengeTableData = await RenderDatabase();
    setChallengesData(challengeTableData);
  };

  const toggleInfoSection = () => {
    setInfoSection(!infosection);
  };

  return (
    <>
      <header>
        <div>
          <h2 className="title">UPLAND CHESS</h2>
        </div>
        <div className="author-info">by dogeyboy19</div>
        <br/>

        
        <div className={"toggleInfoSection"} onClick={toggleInfoSection}>
          {!infosection ? (
            <div className="toggleBar">
              <span className="toggleText">
                CLICK FOR IMPORTANT INFO!!
              </span>
              <span className="close">⬇️</span>
            </div>
          ) :
            <div className={"contentSection"} >
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

        
        
      </header>

      <UserSection setFinalUserUplandID={setFinalUserUplandID} setChallengesData={setChallengesData}/>

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