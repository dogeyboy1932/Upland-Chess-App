import React, { useState} from 'react';
import axios from 'axios';

import HoverPopup from '../Components/hover';
import { RenderDatabase } from '../Helpers/functions';
import { SubmitChallenge } from './SubmitChallenge.js';

import './../App.css'

const UserSection = ({setFinalUserUplandID, setChallengesData}) => {
    // const [isDataLoading, setIsDataLoading] = useState(false); // Need to work on 
  
    const [authKey, setAuth] = useState('')
    const [uplandID, setUplandID] = useState('');
    const [lichessID, setLichessID] = useState('');
    const [password, setPassword] = useState('');
    const [currentUserUplandID, setCurrentUserUplandID] = useState('BLANK');
    const [currentUserLichessID, setCurrentUserLichessID] = useState('BLANK');

    const [isChallengeOpen, setChallengeOpen] = useState(false);
    const [isLoginOpen, setLoginOpen] = useState(false);
    const [isCreateOpen, setCreateOpen] = useState(false);
    const [LogoutButton, setLogoutButton] = useState(false)
    const [isGenerate, setIsGenerate] = useState(true)

    const [profileCreated, setProfileCreated] = useState(false);
    const [loggedInNotif, setLoggedIn] = useState(false);
    const [CreateError, setCreateError] = useState("default")
    const [LoginError, setLoginError] = useState(false)
    const [LichessError, setLichessError] = useState(false)

    const [resetColor, setResetColor] = useState(false)
  
    setFinalUserUplandID(currentUserUplandID) 

    const handleLogin = async () => {
      let realPassword = (await axios.post('/password', {uplandID})).data;

      realPassword = realPassword + ""
  
      if (password === realPassword) {
          
        setLoggedIn(true)
        setTimeout(() => setLoggedIn(false), 3000)      

        let lichessID = (await axios.post('/getLichessID', {uplandID})).data;
  
        setCurrentUserUplandID(uplandID)
        setCurrentUserLichessID(lichessID)

        setLogoutButton(true)
        closeLoginModal();
      } else {
        setLoginError(true)
        setTimeout(() => setLoginError(false), 3000);
      }

      setPassword("")
      setUplandID("")
      setLichessID("")
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
        closeCreateProfileModal();
        handleLogin()
      } else if (res === "no profile found") {
        setCreateError(res)
        setTimeout(() => setCreateError("default"), 3000);
      } else if (res === "invalid lichess") {
        setLichessError(res)
        setTimeout(() => setLichessError("default"), 3000);
      } else {
        setProfileCreated("new")
        setTimeout(() => setProfileCreated("default"), 3000);
        closeCreateProfileModal();
        handleLogin()
      }
    };

    const getAuthCode = async () => {
      const res = (await axios.post('/auth'))

      setAuth(res.data)
      setIsGenerate(false)
    }

    const openCreateProfileModal = async () => {
      setCreateOpen(!isCreateOpen);
      setIsGenerate(true)
      
      setLoginOpen(false)
      setChallengeOpen(false)
    };
  
    const closeCreateProfileModal = async () => {
      setCreateOpen(false);
      setIsGenerate(true)
    };
  

    const openLoginModal = async () => {
      setLoginOpen(!isLoginOpen);
      setCreateOpen(false);
      setIsGenerate(true)

      setChallengeOpen(false)
    };
  
    const closeLoginModal = () => {
      setLoginOpen(false);
    };
  
    const Logout = async () => {
      setCurrentUserUplandID("BLANK") 
      setCurrentUserLichessID("BLANK") 
      setLogoutButton(false)
      setPassword("")
      setUplandID("")
    }



    // FIX THIS [Spinning Thing]
    const resetChallenges = async () => {
      // setIsDataLoading(true);
      const challengeTableData = await RenderDatabase();
      // setIsDataLoading(false);

      setChallengesData(challengeTableData);
      // console.log(challengeTableData)
    };



    const handleMouseDown = () => {
      setResetColor(!resetColor)
    };
  
    const handleMouseUp = () => {
      setResetColor(!resetColor)
    };
    
    
    return (
      <>
        <div className='userSection'>
          <div className='userButtons'>

            {/* PROFILE AND CHALLENGE BUTTONS */}
            <div style={{marginRight: '3%'}}>
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
              
              <SubmitChallenge finalUserUplandID={currentUserUplandID} setLoginOpen = {setLoginOpen} setCreateOpen = {setCreateOpen} setIsGenerate={setIsGenerate} setChallengeOpen={setChallengeOpen} isChallengeOpen={isChallengeOpen}/>

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

              {isCreateOpen && (
                <div className='modal modalUser modalCreate'>
                  <span className="close" onClick={closeCreateProfileModal}>&times;</span>
                  
                  <div className='smallHeader'> Create Profile </div>
                  <br /> 

                  <div style={{display: 'flex'}}>
                    <div className="highlightedText" style={{marginRight: '20px'}}> 
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
                      
                    <HoverPopup text=
                      "👈👈 If you want to change your LichessID, reach @icebear120 for help"
                    >
                      <div className='infoBox' htmlFor="create-username" style={{marginLeft: '25px'}}>
                        *Replace?
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
            </div>
            

            {/* USER DETAILS */}
            <div classNamee="smallHeader" style={{marginRight: '20%', justifyContent: 'space-between'}}>
              <div className="detail">
                <div className="detail detail-box">
                  Registered Upland ID:
                </div>
                <div className="detail detail-value" style={{marginRight: '25px'}}>
                  {currentUserUplandID}
                </div>
              </div>

              <div className="detail">
                <div className="detail detail-box" >
                  Registered Lichess ID:
                </div>
                <div className="detail detail-value">
                  {currentUserLichessID}
                </div>
              </div>
            </div>


            {/* RESET BUTTON */}
            <div>
              <button 
                onClick={resetChallenges}
                onMouseDown={handleMouseDown}
                onMouseUp={handleMouseUp}
                style={{ backgroundColor: resetColor ? '#005c00' : ''}}
                className='resetButton'
              >
                Reset
              </button>              
            </div>   
          </div>
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

        
        {LichessError === "invalid lichess" && (
          <div className={`notification notification-error`}>
            Can't replace LichessID! If you need to change, DM @icebear120 on discord for help
          </div>
        )}
      </>
    )
  }
  
  
  export {UserSection}