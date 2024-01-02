import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ChessChallengesTable = ({ challenges, currentUserUplandID}) => {
  const [acceptedChallenge, setAcceptedChallenges] = useState([]);
  const [hasAcceptedChallenge, setHasAcceptedChallenge] = useState(false);

  const AcceptChallenge = async (link, index) => {
    window.open(link, '_blank');
    
    try {
      await axios.post('/accepted', {
        link
      });

      // Update the acceptedChallenge array with the new index
      setAcceptedChallenges([...acceptedChallenge, index]);
      setHasAcceptedChallenge(true);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const CancelChallenge = async (link, index) => {
    // Remove the index from the acceptedChallenge array
    const updatedAcceptedChallenges = acceptedChallenge.filter((acceptedIndex) => acceptedIndex !== index);
    
    try {
      // Call your backend API to cancel the challenge
      await axios.post('/cancel', { link });
      setAcceptedChallenges(updatedAcceptedChallenges);
      setHasAcceptedChallenge(false);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const DeleteChallenge = async (link) => {
    try {
      await axios.post('/delete', { link });
      setHasAcceptedChallenge(true);
    } catch (error) {
      console.error('Error:', error);
    }
  };


  return (
    <table
      style={{
        borderCollapse: 'collapse',
        width: '100%',
        textAlign: 'center',
        border: '3px solid #3498db',
      }}
    >
      <thead>
        <tr>
          <th style={{ border: '3px solid #3498db', padding: '10px' }}>Challenge</th>
          <th style={{ border: '3px solid #3498db', padding: '10px' }}>Upland ID</th>
          <th style={{ border: '3px solid #3498db', padding: '10px' }}>Lichess ID</th>
          <th style={{ border: '3px solid #3498db', padding: '10px' }}>Lichess Rating</th>
          <th style={{ border: '3px solid #3498db', padding: '10px' }}>Wager Amount</th>
          <th style={{ border: '3px solid #3498db', padding: '10px' }}>Link</th>
          <th style={{ border: '3px solid #3498db', padding: '10px' }}>Accept Challenge</th>
        </tr>
      </thead>
      <tbody>
        {challenges.map((challenge, index) => (
          <tr
            key={index}
            style={{
              backgroundColor: index % 2 === 0 ? '#f2f2f2' : '#ffffff',
              borderBottom: '1px solid #3498db', // Border for each row
            }}
          > 
            <td style={{ padding: '10px', borderRight: '2px solid #3498db', borderBottom: '2px solid #3498db' }}>{challenge.name}</td>           
            <td style={{ padding: '10px', borderRight: '2px solid #3498db', borderBottom: '2px solid #3498db' }}>{challenge.uplandID}</td>
            <td style={{ padding: '10px', borderRight: '2px solid #3498db', borderBottom: '2px solid #3498db' }}>{challenge.lichessID}</td>
            <td style={{ padding: '10px', borderRight: '2px solid #3498db', borderBottom: '2px solid #3498db'}}>{challenge.opponentRating}</td>
            <td style={{ padding: '10px', borderRight: '2px solid #3498db', borderBottom: '2px solid #3498db' }}>{challenge.wageramt}</td>
            <td style={{ padding: '10px', borderRight: '2px solid #3498db', borderBottom: '2px solid #3498db' }}>
              <a href={challenge.link} target="_blank" rel="noopener noreferrer">
                {challenge.link}
              </a>
            </td>

            <td style={{ padding: '10px', borderRight: '2px solid #3498db', borderBottom: '2px solid #3498db' }}>
              {!acceptedChallenge.includes(index) && !challenge.accepted && !(currentUserUplandID === challenge.uplandID) && (
                <button
                  onClick={() => AcceptChallenge(challenge.link, index)}
                  style={{ backgroundColor: '#a52a2a', color: '#fff', padding: '5px 10px', border: 'none', cursor: 'pointer' }}
                >
                  Accept
                </button>
              )}

              {!acceptedChallenge.includes(index) && currentUserUplandID === challenge.uplandID && (
                <button
                  onClick={() => DeleteChallenge(challenge.link, index)}
                  style={{ backgroundColor: 'red', color: '#fff', padding: '5px 10px', border: 'none', cursor: 'pointer' }}
                >
                  Delete
                </button>
              )}

              {acceptedChallenge.includes(index) || challenge.accepted && (
                <button
                  onClick={() => CancelChallenge(challenge.link, index)}
                  style={{ backgroundColor: '#3498db', color: '#fff', padding: '5px 10px', border: 'none', cursor: 'pointer' }}
                >
                  Cancel
                </button>
              )}
            </td>

            <td style={{ padding: '10px', borderRight: '2px solid #3498db', borderBottom: '2px solid #3498db' }}>{challenge.accepted.toString()}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};  


const submitDetails = async (rated, wager, upland) => {
  console.log("Submit 2")
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
      console.log("RESET BUTTON CLICKED")
      const response = await axios.post('/database');
      console.log(response)
      
      return response.data.array;
  } catch (error) {
      console.error('Error processing button click:', error);
  }
};




 
const App = () => {

  const [isModalOpen, setModalOpen] = useState(false);
  const [rated, setRated] = useState('');
  const [wager, setWager] = useState('');
  const [uplandID, setUpland] = useState('');
  const [success, setSuccess] = useState(false);
  const [inputValue, setInputValue] = useState('');
  const [currentUserUplandID, setCurrentUserUplandID] = useState('BLANK');

  const openModal = () => {
    setModalOpen(true);
    setSuccess(false);
  };

  const closeModal = () => {
    setModalOpen(false);
  };

  const handleInputChange = (e) => {
    setInputValue(e.target.value);
  };

  const saveVariable = () => {
    setCurrentUserUplandID(inputValue);
    console.log('Variable saved:', inputValue);
  };
  

  const handleDetailsSubmit = async () => {
    const response = await submitDetails(rated, wager, uplandID);
    console.log(response)

    if (response === 1) {
      closeModal();
      setSuccess(true);
      setTimeout(() => setSuccess(false), 5000);
    }
  };

  const challenge_data1 = challengeDatabase();
  const [challengeTable, setChallengeTable] = useState(null);
  
  useEffect(() => {
      challenge_data1.then(challengeTableData => {
      setChallengeTable(challengeTableData);
    });
  }, []); 


  const challenge_data2 = []

  if (challengeTable != null) {
    for (let i = 0; i < challengeTable.length; i++) {
      let data = {
        name: 'Challenge ' + (i + 1),
        link: challengeTable[i][3],
        opponentRating: challengeTable[i][1],
        uplandID: challengeTable[i][4],
        lichessID: challengeTable[i][0],
        wageramt: challengeTable[i][2],
        accepted: challengeTable[i][5]
      }

      challenge_data2.push(data)
    }
  }

  return (
    <>
      <div style={{ textAlign: 'center', margin: '10px' }}>
        <h1 style={{ color: '#333', marginBottom: '0' }}>UPLAND CHESS</h1>
        <h4 style={{ color: '#333', marginTop: '0' }}>by dogeyboy19</h4>
        <h6 style={{ color: '#333', marginTop: '10' }}>**If your chess challenge expires, HIT DELETE and it will be removed from the list and you'll be refunded**</h6>

        
        <div style={{ margin: '10px' }}>
          <span style={{ margin: '5px' }}></span>
          <button onClick={challengeDatabase}>Reset</button>
        </div>
        <div style={{ margin: '20px' }}>
          <label>
            Enter Upland ID:
            <input type="text" value={inputValue} onChange={handleInputChange} />
          </label>
          <button onClick={saveVariable}>Save</button>
        </div>
        <div>
            {currentUserUplandID}
        </div>
      </div>

      <div>
        <ChessChallengesTable challenges={challenge_data2} currentUserUplandID={currentUserUplandID}/>
      </div>
    
      <div style={{ textAlign: 'center', margin: '10px' }}>
        <button 
        onClick={openModal}
        style={{ backgroundColor: '#3498db', color: '#fff', padding: '10px', border: 'none', cursor: 'pointer' }}
        >
          CREATE CHALLENGE
        </button>

        {isModalOpen && (
          <div className="modal">
            <span className="close" onClick={closeModal}>&times;</span>
            <h2>Enter Details</h2>
            <label htmlFor="name">Upland ID? </label>
            <input type="text" id="wager" value={uplandID} onChange={(e) => setUpland(e.target.value)} />
            <br />
            <label htmlFor="name">Rated? </label>
            <input type="text" id="name" value={rated} onChange={(e) => setRated(e.target.value)} />
            <br />
            <label htmlFor="name">Wager? </label>
            <input type="text" id="wager" value={wager} onChange={(e) => setWager(e.target.value)} />
            <br />
            <button onClick={handleDetailsSubmit}>Submit</button>
          </div>
        )}
        
        {success && (
            <div className="success-popup" style={{ backgroundColor: '#2ecc71', color: '#fff', padding: '10px', margin: '10px', borderRadius: '5px' }}>
              Challenge Submitted!
            </div>
        )}
      </div>        
    </>
  );
};


export default App;


      /* <div> {challengeTable} </div> */

      // console.log(challengeTableData);

      // console.log(response.data);
      // console.log(response.data.array);

// console.log("THIS");
  // console.log(challenge_data2);
  
  // challenge_data2.then(challengeTable => {
  //   console.log(challengeTable);
  // });

    // console.log(challengeTable);
  // console.log(challengeTable.length);

  // console.log(challengeTable[0][0])
  // console.log(challengeTable[0][1])
  // console.log(challengeTable[0][2])
  // console.log(challengeTable[0][3])

    //   challenge_data2.
  // }  

  // const challenge_data = [
  //   {
  //     name: 'Challenge 1',
  //     link: 'testlink.com',
  //     opponentRating: 1500,
  //     uplandID: 346462367,
  //     lichessID: 23671273,
  //     wageramt: '$134',
  //   },
  //   {
  //     name: 'Challenge 2',
  //     link: 'testlink.com',
  //     opponentRating: 1600,
  //     uplandID: 346462367,
  //     lichessID: 23671273,
  //     wageramt: '$432',
  //   },
  // ];

        // <><div> {challengeTable} </div>
      /* // <> */
      /* <div>
        <RawDataToTable rawData={challengeTable} />
      </div> */
      /* <div>
        <ColorfulTable dataArray={challengeTable} />
      </div> */