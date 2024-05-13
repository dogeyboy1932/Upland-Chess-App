import axios from 'axios';
import React, { useState, useEffect} from 'react';

import {BASE_URL as baseUrl} from "../FIXED_FRONTEND_VARIABLES.js"
import './../App.css'


import { HoverPopup } from '../Components/hover';

import { SubmitChallenge } from './SubmitChallenge.js';
import { RenderDatabase } from '../Helpers/RenderDatabase.js';

import { DeleteProfileModal } from '../Components/DeleteProfileModal';
import { UserDetails } from '../Components/UserDetails';


const UserSection = ({setFinalUserUplandID, setChallengesData}) => {
    // const [isDataLoading, setIsDataLoading] = useState(false); // Need to work on 
  
    const [authKey, setAuth] = useState('')
    const [uplandID, setUplandID] = useState('');
    const [lichessID, setLichessID] = useState('');
    const [password, setPassword] = useState('');

    const [currentUserUplandID, setCurrentUserUplandID] = useState('BLANK');
    const [currentUserLichessID, setCurrentUserLichessID] = useState('BLANK');

    const [isChallengeOpen, setChallengeOpen] = useState(false);
    const [isDeleteOpen, setIsDeleteOpen] = useState(false);
    const [isLoginOpen, setLoginOpen] = useState(false);
    const [isCreateOpen, setCreateOpen] = useState(false);

    const [LogoutButton, setLogoutButton] = useState(false)
    const [isGenerate, setIsGenerate] = useState(true)

    const [profileCreated, setProfileCreated] = useState(false);
    const [loggedInNotif, setLoggedIn] = useState(false);
    const [CreateError, setCreateError] = useState("default")
    const [LoginError, setLoginError] = useState(false)
    const [LichessError, setLichessError] = useState(false)

    setFinalUserUplandID(currentUserUplandID)

    
    // Create Profile
    const handleCreateProfile = async () => {
      const res = (await axios.post(baseUrl + '/credentials', {uplandID, lichessID, password})).data;
  
      if (res === "same") {
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
      } else if (res === "success") {
        setProfileCreated(res)
        setTimeout(() => setProfileCreated("default"), 3000);
        closeCreateProfileModal();
        handleLogin()
      }
    };

    // Delete Profile
    const deleteProfile = () => {
      setIsDeleteOpen(!isDeleteOpen);
    };



    // Login
    const handleLogin = async () => {
      let realPassword = (await axios.post(baseUrl +'/password', {uplandID})).data;

      if (password === realPassword && realPassword !== -1) {
          
        setLoggedIn(true)
        setTimeout(() => setLoggedIn(false), 3000)      

        let lichessID = (await axios.post(baseUrl + '/getLichessID', {uplandID})).data;
  
        setCurrentUserUplandID(uplandID)
        setCurrentUserLichessID(lichessID)

        setLogoutButton(true)///
        closeLoginModal();

      } else {
        setLoginError(true)
        setTimeout(() => setLoginError(false), 3000);
      }

      setPassword("")
      setUplandID("")
      setLichessID("")
    };

    // Logout
    const Logout = async () => {
      setCurrentUserUplandID("BLANK") 
      setCurrentUserLichessID("BLANK") 
      setLogoutButton(false)
      setPassword("")
      setUplandID("")
    }


    // Generate "Authentication Code"
    const getAuthCode = async () => {      
      const res = (await axios.post(baseUrl + "/auth"))

      setAuth(res.data)
      setIsGenerate(false)
    }


    // Open & Close Modals
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
  


    // Change Reset Button Color On Click (FIX THIS: Make this a component)
    const [resetColor, setResetColor] = useState(false)

    const handleMouseDown = () => {
      setResetColor(!resetColor)
    };
  
    const handleMouseUp = () => {
      setResetColor(!resetColor)
    };



    // FIX THIS [Spinning Thing]
    const resetChallenges = async () => {
      // setIsDataLoading(true);
      const challengeTableData = await RenderDatabase();
      // setIsDataLoading(false);

      setChallengesData(challengeTableData);
      // console.log(challengeTableData)
    };


    // FIX THIS : LOCAL STORAGE
    useEffect(() => {
        // Retrieve state variables from localStorage when component mounts
        
        const storedUplandID = JSON.parse(localStorage.getItem('UplandID'));
        if (storedUplandID) {
          setUplandID(storedUplandID);
        }

        const storedPassword = JSON.parse(localStorage.getItem('Password'));
        if (storedPassword) {
          setPassword(storedPassword);
        }

        console.log(storedUplandID)
        
        if (storedUplandID) {
          handleLogin()
        }

    }, []); // Empty dependency array to run only once on mount

    useEffect(() => {
        // Store state variables in localStorage when component unmounts
        
        localStorage.setItem('UplandID', JSON.stringify(uplandID));
        localStorage.setItem('Password', JSON.stringify(password));
        
    }, [uplandID, password]);
    
    // FIX THIS ^

    
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
                  
                  <span style={{justifyContent: 'space-between', display: 'flex'}}>
                    <button onClick={handleCreateProfile} className="submitButton"> Submit </button>
                    <button onClick={deleteProfile} className="deleteButton"> DELETE PROFILE </button>
                  </span>

                  <DeleteProfileModal  
                    isDeleteOpen={isDeleteOpen}
                    setIsDeleteOpen={setIsDeleteOpen}
                    uplandID={uplandID}
                    setUplandID={setUplandID}
                    password={password}
                    setPassword={setPassword}
                  />

                </div>
              )}
            </div>
            

            {/* USER DETAILS */}
            <div style={{marginRight: '20%', justifyContent: 'space-between'}}>
              <UserDetails
                currentUserUplandID={currentUserUplandID}
                currentUserLichessID={currentUserLichessID}
              />
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


        {CreateError === "same" && (
          <div className={`notification notification-error`}>
            This is already your lichess profile!  
          </div>
        )}

        {CreateError === "no profile found" && (
          <div className={`notification notification-error`}>
            Your UplandID is not on our record. PLEASE MAKE SURE TO AUTHENTICATE FIRST        
          </div>
        )}

        {profileCreated === "success" && (
          <div className={`notification notification-success`}>
            Profile Created!
          </div>
        )}

        {profileCreated === "success" && (
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