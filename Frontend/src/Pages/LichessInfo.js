import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import axios from 'axios';

import {BASE_URL as baseUrl} from "../../FIXED_FRONTEND_VARIABLES"
import '../App.css';


const LichessPage = () => {
  const navigate = useNavigate();
  const { state } = useLocation();

  const [stats, setStats] = useState('');
  const [deviation, setDeviation] = useState('');
  const [rating, setRating] = useState('');
  const [games, setGames] = useState('');



  useEffect(() => {
    if (state?.lichessId) {
      // console.log(state?.lichessId)
      regenerateStats();
    }

    // if (state?.currentUserUplandID){
    //   console.log("HERE")
    //   console.log(state?.currentUserUplandID)
    // }
  }, []);



  const regenerateStats = async () => {
    try {
      const response = (await axios.post(baseUrl + '/getLichessInfo', { lichessId: state?.lichessId}));

      const lichessData = response.data;

      setStats(lichessData);
      setRating(lichessData.rating);
      setGames(lichessData.games);

      let dev = (lichessData.rd < 100) ? "LOW" : "HIGH"
      setDeviation(dev);

    } catch (error) {
      console.log(error)
    }
  };


  const handleBackToHome = () => {
    navigate('/');
  };


  return (
    <div className="container">
      <button onClick={handleBackToHome}> Back to Home </button>

      <h1 className="smallHeader">VIEWING PLAYER: {state?.lichessId || 'No input value provided'}</h1>
      
      {stats && (
        <div style={{display:"inline"}}>
            
          <p className="smallHeader accepted">
            <p className="textOutliner completed"> Rating: {rating} </p>
            <p className="textOutliner available"> Rated Games: {games} </p>
            <p className="textOutliner ready"> Deviation: {deviation} </p>
          </p>
        </div>
      )}
      
      <button onClick={regenerateStats} className="submitButton">
        Regenerate
      </button>
      
    </div>
  );
};

export { LichessPage };