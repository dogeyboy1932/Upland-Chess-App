import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'
import ChessChallengesTable from './challenges.js'


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

const challengeDatabase = async () => {
  try {
    const response = await axios.post('/database');
      
    const challengeTable = response.data.array;
    const challengeData = []

    if (challengeTable != null) {
      for (let i = 0; i < challengeTable.length; i++) {
        let data = {
          name: 'Challenge ' + (i + 1),
          link: challengeTable[i][3],
          opponentRating: challengeTable[i][1],
          uplandID: challengeTable[i][4],
          lichessID: challengeTable[i][0],
          wageramt: challengeTable[i][2],
          accepted: challengeTable[i][5],
          accepter: challengeTable[i][6]
        }

        challengeData.push(data)
      }
    }

    console.log(challengeData)  
    return challengeData
  } catch (error) {
    console.error('Error processing button click:', error);
  }
};



const MainPage = () => {
  const [authKey, setAuth] = useState('')
  const [uplandID, setUplandID] = useState('');
  const [lichessID, setLichessID] = useState('');
  const [password, setPassword] = useState('');

  const [isChallengeOpen, setChallengeOpen] = useState(false);
  const [challengeSubmitted, setChallengeSubmitted] = useState(false);
  const [challengeError, setChallengeError] = useState("-1");

  const [isCreateOpen, setCreateOpen] = useState(false);
  const [isLoginOpen, setLoginOpen] = useState(false);
  const [profileCreated, setProfileCreated] = useState(false);
  const [loggedInNotif, setLoggedIn] = useState(false);
  const [CreateError, setCreateError] = useState("default")
  const [LoginError, setLoginError] = useState(false)

  const [LogoutButton, setLogoutButton] = useState(false)
  const [needLogin, setNeedLogin] = useState(false)
  
  const [rated, setRated] = useState('');
  const [wager, setWager] = useState('');
  
  const [currentUserUplandID, setCurrentUserUplandID] = useState('BLANK');
  const [challengeData, setChallengesData] = useState([]);



  const openChallengeModal = () => {
    if (currentUserUplandID == "BLANK") {
      setNeedLogin(true)
      setTimeout(() => setNeedLogin(false), 3000);
      return 
    }
    setChallengeOpen(true);
  };

  const closeChallengeModal = () => {
    setChallengeOpen(false);
  };

  const openCreateProfileModal = async () => {
    setLoginOpen(false)
    setCreateOpen(true);

    const res = (await axios.post('/auth')).data
    setAuth(res)
  };

  const closeCreateProfileModal = () => {
    setCreateOpen(false);
  };

  const handleCreateProfile = async () => {
    const res = (await axios.post('/credentials', {uplandID, lichessID, password})).data;

    if (res == "profile exists") {
      setCreateError(res)
      setTimeout(() => setCreateError("default"), 3000);
    } else if (res == "wrong password") {
      setProfileCreated(res)
      setTimeout(() => setProfileCreated("default"), 3000);
    } else if (res == "replaced") {
      setProfileCreated(res)
      setTimeout(() => setProfileCreated("default"), 3000);
    } else if (res == "no profile found") {
      setCreateError(res)
      setTimeout(() => setCreateError("default"), 3000);
    } else {
      setProfileCreated("new")
      setTimeout(() => setProfileCreated("default"), 3000);
      closeCreateProfileModal();
    }
  };

  const openLoginModal = () => {
    setLoginOpen(true);
    setCreateOpen(false);
  };

  const closeLoginModal = () => {
    setLoginOpen(false);
  };

  const handleLogin = async () => {
    const realPassword = (await axios.post('/password', {uplandID})).data;

    if (password == realPassword) {
      setLoggedIn(true)
      setTimeout(() => setLoggedIn(false), 3000);      
      setCurrentUserUplandID(uplandID)
      setLogoutButton(true)
      closeLoginModal();

    } else {
      setLoginError(true)
      setTimeout(() => setLoginError(false), 3000);
    }
  };

  const Logout = async () => {
    setCurrentUserUplandID("BLANK")

    setLogoutButton(false)
    setTimeout(() => setLogoutButton(true), 5000);
  }

  const handleChallengeSubmit = async () => {
    const res = await submitDetails(rated, wager, uplandID);

    if (res === 1) {
      setChallengeSubmitted(true);
      setTimeout(() => setChallengeSubmitted(false), 5000);
      closeChallengeModal();
    } else if (res === -1 || res === -2 || res === -3 || res === -4) {
      setChallengeError(res);
      setTimeout(() => setChallengeError(1), 5000);
    }
  }; 

  const resetChallenges = async () => {
    const challengeTableData = await challengeDatabase();
    setChallengesData(challengeTableData);
  };

  useEffect(() => {
    resetChallenges();
  }, []);


  return (
    <>
      <div style={{ textAlign: 'center', padding: '2px', backgroundColor: '#daa520', borderBottom: '3.5px solid black' }}>
        <div>
          <h2 style={{ fontFamily: 'cursive', fontSize: '4em', backgroundColor: '#adff2f', color: '#e22a22', margin: '0px', display: 'inline-block', border: '4px solid #000'}}>
            UPLAND CHESS
          </h2>
        </div>
        
        <div style={{padding: '15px', borderBottom: '4px solid #000', backgroundColor: '#f0e68c', borderLeft: '4px solid #000', borderRight: '4px solid #000', display: 'inline-block', marginBottom: "10px"}}>
          by dogeyboy19
        </div>
        
        <div style={{padding: '15px', border: '4px solid #000', backgroundColor: '#f8f8ff', display: 'block' }}>
          <h3 style={{ fontFamily: 'monospace', fontSize: '1.35em', marginTop: '10px', color: '#000'}}>
            <span style={{ color: '#ff6347' }}>**</span>If your chess challenge expires, HIT DELETE and it will be removed from the list and you'll be refunded
            <span style={{ color: '#ff6347' }}>**</span>
          </h3>
        </div>
      </div>


      <div style={{backgroundColor: '#40e0d0', border: '2px solid black'}}>
        <div style={{ display: 'flex', justifyContent: 'space-between'}}>
          <div style={{ display: 'flex', marginTop: '20px'  }}>
            <button onClick={openCreateProfileModal} style={{ backgroundColor: 'orange', marginLeft: '20px', color: '#000000', padding: '10px 22px', border: '5px solid black'}}>
              Create Profile
            </button>

            {LogoutButton ? (
              <button onClick={Logout} style={{ backgroundColor: '#7fffd4', marginLeft: '70px', color: '#000000', padding: '10px 22px', border: '5px solid black'}}>
                Logout
              </button>
            ) : (
              <button onClick={openLoginModal} style={{ backgroundColor: '#7fffd4', marginLeft: '70px', color: '#000000', padding: '10px 22px', border: '5px solid black'}}>
                Login
              </button>
            )}
          </div>

          <button onClick={resetChallenges} style={{ backgroundColor: 'green', color: '#fff', marginRight: '40px', padding: '10px 22px', border: '5px solid black', marginTop: '20px' }}>
            Reset
          </button>
        </div>


        {isCreateOpen && (
          <div style={{marginLeft: "10px",  marginTop: "10px"}}>
            <div>
              FIRST SIGN IN ON UPLAND WITH THIS AUTH KEY: {authKey}
            </div>
                
            <div style={{marginLeft: "20px",  marginTop: "10px", display: 'inline-block'}}>
              <span className="close" onClick={closeCreateProfileModal}>&times;</span>
              <h2>Create Profile</h2>
              
              <label htmlFor="create-username">Upland ID: </label>
              <input type="text" id="create-username" value={uplandID} onChange={(e) => setUplandID(e.target.value)} />
              <br />

              <label htmlFor="create-username">Lichess ID: </label>
              <input type="text" id="create-username" value={lichessID} onChange={(e) => setLichessID(e.target.value)} />
              (👈👈 If you want to change your LichessID, just resubmit it here)
              <br />

              <label htmlFor="create-password">Password: </label>
              <input type="password" id="create-password" value={password} onChange={(e) => setPassword(e.target.value)} />
              <br />
              
              <button onClick={handleCreateProfile} style={{marginTop: "5px"}}> Submit </button>
            </div>
          </div>
        )}


        {isLoginOpen && (
          <div style={{marginLeft: "20px",  marginTop: "10px", display: 'inline-block'}}>
            <span className="close" onClick={closeLoginModal}>&times;</span>
            <h2>Login</h2>
            
            <label htmlFor="login-username">Upland ID: </label>
            <input type="text" id="login-username" value={uplandID} onChange={(e) => setUplandID(e.target.value)} />
            <br />
            
            <label htmlFor="login-password">Password: </label>
            <input type="password" id="login-password" value={password} style={{ marginTop: "5px"}} onChange={(e) => setPassword(e.target.value)} />
            <br />
            
            <button onClick={handleLogin} style={{ marginTop: "5px", border: '5px solid black'}}>Submit</button>
          </div>
        )}

        <div>
          <div
            style={{
              marginTop: '30px',
              marginLeft: '20px',
              padding: '15px',
              borderRight: '1px solid #000',
              borderLeft: '4px solid #000',
              borderTop: '4px solid #000',
              borderBottom: '4px solid #000',
              backgroundColor: '#b9afca',
              display: 'inline-block',
              marginBottom: '30px'
            }}
          >
            Registered Upland ID: 
          </div>

          <div
            style={{
              marginTop: '30px',
              padding: '15px',
              borderRight: '4px solid #000',
              borderLeft: '1px solid #000',
              borderTop: '4px solid #000',
              borderBottom: '4px solid #000',
              backgroundColor: 'yellow',
              display: 'inline-block',
              marginBottom: '30px'
            }}
          >
            {currentUserUplandID}
          </div>
        </div>
      </div>
      
      <div>
        <ChessChallengesTable challenges={challengeData} currentUserUplandID={currentUserUplandID}/>
      </div>
  
      <div style={{ backgroundColor: '#f5deb3', textAlign: 'center', padding: "20px", border: '3.5px solid black'}}>
        <button onClick={openChallengeModal} style={{ backgroundColor: '#008080', color: '#fff', padding: '10px', border: '4px solid #000'}}> 
          CREATE CHALLENGE 
        </button>
      </div>

      <div style={{ textAlign: 'center'}}>
        {isChallengeOpen && (
          <div>
            <span className="close" onClick={closeChallengeModal}> &times; </span>
            <h2 style={{ marginRight: '240px' }}>Enter Details</h2>
            
            <label htmlFor="name">Rated? </label>
            <input type="text" id="name" value={rated} style={{border: '5px solid black'}} onChange={(e) => setRated(e.target.value)} />
            <br />
            
            <label htmlFor="name">Wager? </label>
            <input type="text" id="wager" value={wager} style={{ marginTop: "5px", border: '5px solid black'}} onChange={(e) => setWager(e.target.value)} />
            <br />
            
            <button onClick={handleChallengeSubmit} style={{ marginTop: "5px", border: '5px solid black'}}>Submit</button>
          </div>
        )}
      </div>
      
      
      {CreateError == "profile exists" && (
        <div className={`notification notification-error`}>
          <div className="notification-content">
            Profile Already Exists          
          </div>
        </div>
      )}

      {CreateError == "no profile found" && (
        <div className={`notification notification-error`}>
          <div className="notification-content">
            Your UplandID is not on our record. PLEASE MAKE SURE TO AUTHENTICATE FIRST        
          </div>
        </div>
      )}

      {profileCreated == "new" && (
        <div className={`notification notification-success`}>
          <div className="notification-content">
            Profile Created!
          </div>
        </div>
      )}

      {profileCreated == "replaced" && (
        <div className={`notification notification-success`}>
          <div className="notification-content">
            Lichess ID has been replaced!
          </div>
        </div>
      )}

      {profileCreated == "wrong password" && (
        <div className={`notification notification-error`}>
          <div>
            Can't replace Lichess ID! You need to enter the right password!
          </div>
        </div>
      )}

      {needLogin && (
        <div className={`notification notification-error`}>
          <div backgroundColor="blue">
            Need to be logged in!
          </div>
        </div>
      )}

      {LoginError && (
        <div className={`notification notification-error`}>
          <div className="notification-content" backgroundColor="red">
            Incorrect UplandID or Password
          </div>
        </div>
      )}  

      {loggedInNotif && (
        <div className={`notification notification-success`}>
          <div className="notification-content">
            Logged In!
          </div>
        </div>
      )}
      
      {challengeSubmitted && (
        <div className={`notification notification-success`}>
          <div className="notification-content">
            Challenge Submitted!!
          </div>
        </div>
      )}

      {challengeError === -1 && (
        <div style={{ backgroundColor: 'red', color: '#fff', padding: '10px', margin: '10px', borderRadius: '5px' }}>
          Invalid Upland ID...
        </div>
      )}

      {challengeError === -2 && (
        <div style={{ backgroundColor: 'red', color: '#fff', padding: '10px', margin: '10px', borderRadius: '5px' }}>
          Invalid Rating...
        </div>
      )}

      {challengeError === -3 && (
        <div style={{ backgroundColor: 'red', color: '#fff', padding: '10px', margin: '10px', borderRadius: '5px' }}>
          Invalid Wager...
        </div>
      )}

      {challengeError === -4 && (
        <div style={{ backgroundColor: 'red', color: '#fff', padding: '10px', margin: '10px', borderRadius: '5px' }}>
          Sorry, but the amount you wagered exceeds your balance!
        </div>
      )}



      
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
    </>
  );
};


export default MainPage;