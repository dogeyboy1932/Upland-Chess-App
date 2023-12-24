import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ChessChallengesTable = ({ challenges }) => {
  return (
    <table
      style={{
        borderCollapse: 'collapse',
        width: '100%',
        textAlign: 'center',
        border: '3px solid #ddd',
      }}
    >
      <thead>
        <tr>
          <th style={{ border: '3px solid #ddd', padding: '10px' }}>Lichess Rating</th>
          <th style={{ border: '3px solid #ddd', padding: '10px' }}>Upland ID</th>
          <th style={{ border: '3px solid #ddd', padding: '10px' }}>Lichess ID</th>
          <th style={{ border: '3px solid #ddd', padding: '10px' }}>Wager Amount</th>
          <th style={{ border: '3px solid #ddd', padding: '10px' }}>Link</th>
        </tr>
      </thead>
      <tbody>
        {challenges.map((challenge, index) => (
          <tr
            key={index}
            style={{
              backgroundColor: index % 2 === 0 ? '#f2f2f2' : '#ffffff',
              borderBottom: '1px solid #ddd', // Border for each row
            }}
          >
            <td style={{ padding: '10px', borderRight: '2px solid #ddd', borderBottom: '2px solid #ddd'}}>{challenge.name}</td>
            <td style={{ padding: '10px', borderRight: '2px solid #ddd', borderBottom: '2px solid #ddd' }}>{challenge.uplandID}</td>
            <td style={{ padding: '10px', borderRight: '2px solid #ddd', borderBottom: '2px solid #ddd' }}>{challenge.lichessID}</td>
            <td style={{ padding: '10px', borderRight: '2px solid #ddd', borderBottom: '2px solid #ddd' }}>{challenge.wageramt}</td>
            <td style={{ padding: '10px', borderBottom: '2px solid #ddd' }}>
              <a href={challenge.link} target="_blank" rel="noopener noreferrer">
                {challenge.link}
              </a>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};  


const createChallengeButton = async () => {
  try {
      await axios.post('/test');
      console.log("CHALLENGE BUTTON CLICKED")

  } catch (error) {
      console.error('Error processing button click:', error);
  }
};


const challengeDatabase = async () => {
  try {
      const response = await axios.post('/database');
      console.log("RESET BUTTON CLICKED")
      console.log(response)
      
      return response.data.array;
  } catch (error) {
      console.error('Error processing button click:', error);
  }
};


 
const App = () => {

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
      }
      challenge_data2.push(data)
    }
  }
    

  return (
    <>
      <div style={{ textAlign: 'center', margin: '10px' }}>
        <h1 style={{ color: '#333', marginBottom: '0' }}>UPLAND CHESS</h1>
        <h4 style={{ color: '#333', marginTop: '0' }}>by dogeyboy19</h4>

        
        <div style={{ margin: '10px' }}>
          <button onClick={createChallengeButton}>Create Challenge</button>
          <span style={{ margin: '5px' }}></span>
          <button onClick={challengeDatabase}>Reset</button>
        </div>
        <div style={{ margin: '20px' }}>
          <label>
            Enter Lichess ID:
            <input
              type="text" />
          </label>
        </div>
      </div>

      <div>
        
        


        <ChessChallengesTable challenges={challenge_data2} />

      </div>
    </>

  );
};


export default App;


      {/* <div> {challengeTable} </div> */}

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