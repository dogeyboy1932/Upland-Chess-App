import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'

const ChessChallengesTable = ({ challenges, currentUserUplandID}) => {
  const [acceptedChallenge, setAcceptedChallenges] = useState([]);
  const [successfullyDeleted, setsuccessfullyDeleted] = useState(false);
  

  const AcceptChallenge = async (UplandID, link, index) => {
    window.open(link, '_blank');
    
    try {
      await axios.post('/accepted', {
        link,
        currentUserUplandID,
        UplandID
      });

      setAcceptedChallenges([acceptedChallenge, index]);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const CancelChallenge = async (link, index) => {
    const updatedAcceptedChallenges = acceptedChallenge.filter((acceptedIndex) => acceptedIndex !== index);
    
    try {
      await axios.post('/cancel', { link });
      setAcceptedChallenges(updatedAcceptedChallenges);

    } catch (error) {
      console.error('Error:', error);
    }
  };

  const DeleteChallenge = async (link, accepted) => {
    try {
      const res = await axios.post('/delete', { link });
      
      if (res.data == 'Success') {
        setsuccessfullyDeleted(true)
        setTimeout(() => setsuccessfullyDeleted(false), 5000);
      } 

    } catch (error) {
      console.error('Error:', error);
    }
  };


  return (
    <>
      <table>
        <thead>
          <tr>
            <th>Challenge</th>
            <th>Upland ID</th>
            <th>Lichess ID</th>
            <th>Lichess Rating</th>
            <th>Wager Amount</th>
            <th>Link</th>
            <th>Availability</th>
            <th>Accept Challenge</th>
          </tr>
        </thead>

        <tbody>
          {challenges.map((challenge, index) => (
            <tr key={index}> 
              <td> {challenge.name} </td>           
              <td> {challenge.uplandID} </td>
              <td> {challenge.lichessID} </td>
              <td> {challenge.opponentRating} </td>
              <td> {challenge.wageramt} </td>

              <td>
                <a href={challenge.link} target="_blank" rel="noopener noreferrer">
                  {challenge.link}
                </a>
              </td>

              <td>
                {(acceptedChallenge.includes(index) || challenge.accepted) ? (
                  <span style={{ display: 'inline-block', backgroundColor: 'Purple', color: 'white'}}>
                    Accepted
                  </span>
                ) : (
                  <span style={{ display: 'inline-block', backgroundColor: '#00ffff', color: '#000000'}}>
                    Available
                  </span>
                )}
              </td>

              <td>
                {!acceptedChallenge.includes(index) && !challenge.accepted && !(currentUserUplandID === challenge.uplandID) && (
                  <button
                    onClick={() => AcceptChallenge(challenge.uplandID, challenge.link, index)}
                    style={{backgroundColor: '#a52a2a'}}
                  >
                    Accept
                  </button>
                )}

                {!acceptedChallenge.includes(index) && !challenge.accepted && challenge.uplandID === currentUserUplandID && (
                  <button
                    onClick={() => DeleteChallenge(challenge.link, challenge.accepted, index)}
                    style={{backgroundColor: 'red'}}
                  >
                    Delete
                  </button>
                )}

                {(acceptedChallenge.includes(index) || challenge.accepted) && challenge.accepter === currentUserUplandID && (
                  <button
                    onClick={() => CancelChallenge(challenge.link, index)}
                    style={{backgroundColor: '#3498db'}}
                  >
                    Cancel
                  </button>
                )}
              </td>

            </tr>
          ))} 
        </tbody>
      </table>

      {successfullyDeleted && (
        <div className={`notification notification-success`}>
          <div className="notification-content">
            Challenge Successfully Deleted & Escrow Refunded!
          </div>
        </div>
      )}
    </>
  );
};  


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
  console.log("RESET BUTTON CLICKED")
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



const App = () => {
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

    // console.log(res)

    if (res == "profile exists") {
      setCreateError(res)
      setTimeout(() => setCreateError("default"), 3000);
    } else if (res == "no profile found") {
      setCreateError(res)
      setTimeout(() => setCreateError("default"), 3000);
    } else {
      setProfileCreated(true)
      setTimeout(() => setProfileCreated(false), 3000);
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

      // console.log("HERE")
      // console.log(LogoutButton)
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
      <div style={{ textAlign: 'center', }}>
        <h1 style={{ color: '#333', marginBottom: '0' }}>UPLAND CHESS</h1>
        <h3 style={{ color: '#333', marginTop: '0' }}>by dogeyboy19</h3>
        <h4 style={{ color: '#333', marginTop: '10' }}>**If your chess challenge expires, HIT DELETE and it will be removed from the list and you'll be refunded**</h4>
      </div>


      <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '20px' }}>
        <div style={{ display: 'flex' }}>
          <button onClick={openCreateProfileModal} style={{ backgroundColor: 'orange', marginLeft: '10px', color: '#000000'}}>
            Create Profile
          </button>

          {LogoutButton ? (
            <button onClick={Logout} style={{ backgroundColor: '#7fffd4', marginLeft: '70px', color: '#000000' }}>
              Logout
            </button>
          ) : (
            <button onClick={openLoginModal} style={{ backgroundColor: '#7fffd4', marginLeft: '70px', color: '#000000' }}>
              Login
            </button>
          )}
          
        </div>

        <button onClick={resetChallenges} style={{ backgroundColor: 'green', color: '#fff' }}>
          Reset
        </button>
      </div>


      {isCreateOpen && (
        <div style={{marginLeft: "20px"}}>
          <div>
            FIRST SIGN IN ON UPLAND WITH THIS AUTH KEY: {authKey}
          </div>
              
          <div style={{marginLeft: "20px"}}>
            <span className="close" onClick={closeCreateProfileModal}>&times;</span>
            <h2>Create Profile</h2>
            
            <label htmlFor="create-username">Upland ID: </label>
            <input type="text" id="create-username" value={uplandID} onChange={(e) => setUplandID(e.target.value)} />
            <br />

            <label htmlFor="create-username">Lichess ID: : </label>
            <input type="text" id="create-username" value={lichessID} onChange={(e) => setLichessID(e.target.value)} />
            <br />

            <label htmlFor="create-password">Password: </label>
            <input type="password" id="create-password" value={password} onChange={(e) => setPassword(e.target.value)} />
            <br />
            
            <button onClick={handleCreateProfile}>Submit</button>
          </div>
        </div>
      )}


      {isLoginOpen && (
        <div style={{marginLeft: "20px"}}>
          <span className="close" onClick={closeLoginModal}>&times;</span>
          <h2>Login</h2>
          
          <label htmlFor="login-username">Upland ID: </label>
          <input type="text" id="login-username" value={uplandID} onChange={(e) => setUplandID(e.target.value)} />
          <br />
          
          <label htmlFor="login-password">Password: </label>
          <input type="password" id="login-password" value={password} onChange={(e) => setPassword(e.target.value)} />
          <br />
          
          <button onClick={handleLogin}>Submit</button>
        </div>
      )}


      <div style={{ marginTop: '30px' }}>
        <ChessChallengesTable challenges={challengeData} currentUserUplandID={currentUserUplandID}/>
      </div>
    

      <div style={{ textAlign: 'center', margin: '10px' }}>
        <button onClick={openChallengeModal} style={{ backgroundColor: 'orange', color: '#fff', padding: '10px'}}> CREATE CHALLENGE </button>

        {isChallengeOpen && (
          <div>
            <span className="close" onClick={closeChallengeModal}> &times; </span>
            <h2>Enter Details</h2>
            
            <label htmlFor="name">Rated? </label>
            <input type="text" id="name" value={rated} onChange={(e) => setRated(e.target.value)} />
            <br />
            
            <label htmlFor="name">Wager? </label>
            <input type="text" id="wager" value={wager} onChange={(e) => setWager(e.target.value)} />
            <br />
            
            <button onClick={handleChallengeSubmit}>Submit</button>
          </div>
        )}
      </div>

      <div style={{ marginTop: '70px', marginLeft: '20px'}}>
        Registered Upland ID: {currentUserUplandID}
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

      {profileCreated && (
        <div className={`notification notification-success`}>
          <div className="notification-content">
            Profile Created
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
      


      <div style={{ marginTop: '20px', marginLeft: '20px'}}>
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


export default App;