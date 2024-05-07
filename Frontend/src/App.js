import React, { useState, useEffect } from 'react';
import './App.css'
import ChessChallengesTable from './Sections/Database.js'
import { RenderDatabase } from './Helpers/functions.js';
import { UserSection } from './Sections/Login.js'; // Import UserSection from Login component
import { ToggleBar } from './Sections/ToggleInfoBar.js';


const MainPage = () => {
  const [challengeData, setChallengesData] = useState([]);
  const [finalUserUplandID, setFinalUserUplandID] = useState('BLANK'); // Lift state up
  
  useEffect(() => {
    resetChallenges();
  }, [finalUserUplandID]);

  const resetChallenges = async () => {
    const challengeTableData = await RenderDatabase();
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
        
      </header>

      <ToggleBar/>

      <UserSection setFinalUserUplandID={setFinalUserUplandID} setChallengesData={setChallengesData}/>

      <ChessChallengesTable challenges={challengeData} currentUserUplandID={finalUserUplandID}/>
      
      {/* <SubmitChallenge finalUserUplandID={finalUserUplandID}/> */}
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