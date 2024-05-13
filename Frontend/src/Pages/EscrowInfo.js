// EscrowPage.js
import React, { useState, useEffect } from 'react';
import { useLocation, useNavigate } from 'react-router-dom';
import axios from 'axios';

import {BASE_URL as baseUrl} from "../../FIXED_FRONTEND_VARIABLES"
import '../App.css';

const EscrowPage = () => {
  const navigate = useNavigate();
  const { state } = useLocation();

  const [escrow, setEscrow] = useState([]);
  const [assets, setAssets] = useState([]);
  const [status, setStatus] = useState('');
  const [upx, setUpx] = useState('');


  const handleBackToHome = () => {
    navigate('/');
  };


  useEffect(() => {
    if (state?.escrowId) {
      regenerateEscrow();
    }

    // if (state?.currentUserUplandID){
    //   console.log("HERE")
    //   console.log(state?.currentUserUplandID)
    // }
  }, []);


  const regenerateEscrow = async () => {
    try {
      const response = await axios.post(baseUrl + '/getEscrow', { escrowId: state?.escrowId});

      const escrowData = response.data;

      setEscrow(escrowData);
      setAssets(escrowData.assets);
      setStatus(escrowData.status);
      setUpx(escrowData.upx);
    
    } catch (error) {
      console.log(error)
    }
  };



  return (
    <div className="container">
      <button onClick={handleBackToHome}> Back to Home </button>

      <h1 className="smallHeader">VIEWING ESCROW: {state?.escrowId || 'No input value provided'}</h1>
      
      {escrow && (
        <div style={{display:"inline"}}>
            
          <p className="textOutliner accepted">
            <p className="textOutliner completed"> UPX: {upx} </p>
            <p className="textOutliner available"> Status: {status} </p>
          </p>
          

          <table>
            <thead>
                <tr>
                    <th colSpan="3" className="textOutliner ready"> ASSETS </th>
                </tr>
                
                <tr>
                    <th>Amount</th>
                    <th>Owner EOS ID</th>
                    <th>Status</th>
                </tr>
            </thead>
            
            {assets && (
              <tbody>
                {assets.map((asset, index) => (
                  <tr key={index}>
                    <td>{asset.amount}</td>
                    <td>{asset.ownerEosId}</td>
                    <td>{asset.status}</td>
                  </tr>
                ))}
              </tbody>
            )}
          </table>
        
        </div>
      )}
      
      <button onClick={regenerateEscrow} className="submitButton">
        Regenerate
      </button>
      
    </div>
  );
};

export { EscrowPage };