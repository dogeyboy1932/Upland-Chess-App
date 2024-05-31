import React, { useState, useEffect } from 'react';
import '../App.css'

import { ChessChallengesTable } from '../Sections/Database.js'
import { RenderDatabase } from '../Helpers/RenderDatabase.js';
import { UserSection } from '../Sections/Login.js';
import { ToggleBar } from '../Sections/ToggleInfoBar.js';


const MainPage = () => {
  const [challengeData, setChallengesData] = useState([]);
  const [finalUserUplandID, setFinalUserUplandID] = useState('BLANK'); // Lift state up
  

  useEffect(() => {
    resetChallenges();
  }, []);

  const resetChallenges = async () => {
    console.log("RESET")

    const challengeTableData = await RenderDatabase();
    setChallengesData(challengeTableData);

    // console.log(challengeTableData)
  };

  return (
    <>
      <header>
        <div> <h2 className="title">UPLAND CHESS</h2> </div>
        <div className="author-info">by dogeyboy19 </div>
      </header>

      <ToggleBar/>

      <UserSection setFinalUserUplandID={setFinalUserUplandID} setChallengesData={setChallengesData}/>

      <ChessChallengesTable challenges={challengeData} currentUserUplandID={finalUserUplandID} setChallengesData={setChallengesData}  />
    </>
  );
};

export {MainPage};