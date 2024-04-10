import React, { useState} from 'react';
import axios from 'axios';

import {ChallengeDatabase} from '../Helpers/functions';
import HoverPopup from '../Components/hover';
import './../App.css'

const UserSection = ({setFinalUserUplandID, setChallengesData}) => {
    const [isDataLoading, setIsDataLoading] = useState(false); // Need to work on 
  
    const [authKey, setAuth] = useState('')
    const [uplandID, setUplandID] = useState('');
    const [lichessID, setLichessID] = useState('');
    const [password, setPassword] = useState('');
    const [currentUserUplandID, setCurrentUserUplandID] = useState('BLANK');
  
    const [isCreateOpen, setCreateOpen] = useState(false);
    const [isLoginOpen, setLoginOpen] = useState(false);
    const [LogoutButton, setLogoutButton] = useState(false)
    const [isGenerate, setIsGenerate] = useState(true)

    const [profileCreated, setProfileCreated] = useState(false);
    const [loggedInNotif, setLoggedIn] = useState(false);
    const [CreateError, setCreateError] = useState("default")
    const [LoginError, setLoginError] = useState(false)
  
    setFinalUserUplandID(currentUserUplandID) 

      
    const handleLogin = async () => {
      let realPassword = (await axios.post('/password', {uplandID})).data;
  
      realPassword = realPassword + ""
  
      if (password === realPassword) {
          
        setLoggedIn(true)
        setTimeout(() => 
          setLoggedIn(false), 3000)      
  
        setCurrentUserUplandID(uplandID)
        setLogoutButton(true)
        closeLoginModal();
      } else {
        setLoginError(true)
        setTimeout(() => setLoginError(false), 3000);
      }
    };
  
    const handleCreateProfile = async () => {
      const res = (await axios.post('/credentials', {uplandID, lichessID, password})).data;
  
      if (res === "profile exists") {
        setCreateError(res)
        setTimeout(() => setCreateError("default"), 3000);
      } else if (res === "wrong password") {
        setProfileCreated(res)
        setTimeout(() => setProfileCreated("default"), 3000);
      } else if (res === "replaced") {
        setProfileCreated(res)
        setTimeout(() => setProfileCreated("default"), 3000);
      } else if (res === "no profile found") {
        setCreateError(res)
        setTimeout(() => setCreateError("default"), 3000);
      } else {
        setProfileCreated("new")
        setTimeout(() => setProfileCreated("default"), 3000);
        closeCreateProfileModal();
      }

      closeCreateProfileModal();
    };
  
    const resetChallenges = async () => {
      setIsDataLoading(true);
      const challengeTableData = await ChallengeDatabase();
      setIsDataLoading(false);

      setChallengesData(challengeTableData);
      console.log(challengeTableData)
    };

    const getAuthCode = async () => {
      const res = (await axios.post('/auth')).data
      setAuth(res)
      setIsGenerate(false)
    }

    const openCreateProfileModal = async () => {
      setLoginOpen(false)
      setCreateOpen(true);
    };
  
    const closeCreateProfileModal = async () => {
      setCreateOpen(false);
      setIsGenerate(true)
    };
  

    const openLoginModal = async () => {
      setLoginOpen(true);
      setCreateOpen(false);
      setIsGenerate(true)
    };
  
    const closeLoginModal = () => {
      setLoginOpen(false);
    };
  
    const Logout = async () => {
      setCurrentUserUplandID("BLANK")  
      setLogoutButton(false)
    }

    return (
      <>
        <div className='userSection'>
          <div className='userButtons'>
            <div>
              <button onClick={openCreateProfileModal} className='createProfButton'>
                Create Profile
              </button>
                
              {LogoutButton ? (
                <button onClick={Logout} className='logButton'>
                  Logout
                </button>
              ) : (
                <button onClick={openLoginModal} className='logButton'>
                  Login
                </button>
              )}
            </div>

            <div >
              <div className="detail detail-box">
                Registered Upland ID:
              </div>
              <div className="detail detail-value">
                {currentUserUplandID}
              </div>
            </div>


            <div>
              <button onClick={resetChallenges} className='resetButton'>
                Reset
              </button>
            </div>
            
          </div>
  
  
  
          {isCreateOpen && (
            <div className='modal modalUser modalCreate'>
              <span className="close" onClick={closeCreateProfileModal}>&times;</span>
              
              <div className='smallHeader'> Create Profile </div>
              <br /> 

              <div style={{display: 'flex'}}>
                <div className="highlightedText"> 
                  FIRST SIGN IN ON UPLAND WITH THIS AUTH KEY: 
                </div>

                {isGenerate ? (
                  <button onClick={getAuthCode} className="generateButton"> Generate Code </button>
                ) : (
                  <div className="highlightedText highlight"> {authKey} </div>
                )}
              </div>
              <br />         
              
              <label className=' important' htmlFor="create-username">Upland ID: </label>
              <input type="text" id="create-username" value={uplandID} className='user-input' onChange={(e) => setUplandID(e.target.value)} />
              <br />
                
              <div style={{display: 'inline-flex', alignItems: 'center'}}>
                <label className='important' htmlFor="create-username">Lichess ID:</label>
                <input type="text" id="create-lichess" value={lichessID} className='user-input' onChange={(e) => setLichessID(e.target.value)} />
                  
                {/* Make this a component */}
                <HoverPopup text="👈👈 If you want to change your LichessID, just resubmit it here">
                  <div  className='infoBox' htmlFor="create-username" style={{marginLeft: '25px'}}>
                    *?
                  </div>
                </HoverPopup>
              </div>
              <br />

              <label className=' important' htmlFor="create-password">Password: </label>
              <input type="password" id="create-password" value={password} className='user-input' onChange={(e) => setPassword(e.target.value)} />
              <br />
              
              <button onClick={handleCreateProfile} className="submitButton"> Submit </button>
            </div>
          )}
  
  
          {isLoginOpen && (
            <div className='modal modalUser modalLogin'>
              <span className="close" onClick={closeLoginModal}>&times;</span>
              <div className='smallHeader'> Login </div>
              <br/>
              
              <label htmlFor="login-username">Upland ID: </label>
              <input type="text" id="login-username" value={uplandID} className='user-input' onChange={(e) => setUplandID(e.target.value)} />
              <br />
              
              <label htmlFor="login-password">Password: </label>
              <input type="password" id="login-password" value={password} className='user-input' onChange={(e) => setPassword(e.target.value)} />
              <br />
              
              <button onClick={handleLogin} className='submitButton' >Submit</button>
            </div>
          )}        
        </div>
  

          {CreateError === "profile exists" && (
            <div className={`notification notification-error`}>
              Profile Already Exists  
            </div>
          )}
  
          {CreateError === "no profile found" && (
            <div className={`notification notification-error`}>
              Your UplandID is not on our record. PLEASE MAKE SURE TO AUTHENTICATE FIRST        
            </div>
          )}
  
          {profileCreated === "new" && (
            <div className={`notification notification-success`}>
              Profile Created!
            </div>
          )}
  
          {profileCreated === "replaced" && (
            <div className={`notification notification-success`}>
              Lichess ID has been replaced!
            </div>
          )}
  
          {profileCreated === "wrong password" && (
            <div className={`notification notification-error`}>
              Can't replace Lichess ID! You need to enter the right password!
            </div>
          )}
  
          {LoginError && (
            <div className={`notification notification-error`}>
              Incorrect UplandID or Password
            </div>
          )}  
  
          {loggedInNotif && (
            <div className={`notification notification-success`}>
              Logged In!
            </div>
          )}
      </>
    )
  }
  
  
  export {UserSection}