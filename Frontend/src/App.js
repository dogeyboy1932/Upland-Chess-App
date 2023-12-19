import React from 'react';

const ChessChallengesTable = ({ challenges }) => {
  return (
    <table>
      <thead>
        <tr>
          <th>Opponent Name</th>
          <th>Details</th>
        </tr>
      </thead>
      <tbody>
        {challenges.map((challenge, index) => (
          <tr key={index}>
            <td>{challenge.name}</td>
            <td>
              <div>
                <strong>Link:</strong>{' '}
                <a href={challenge.link} target="_blank" rel="noopener noreferrer">
                  {challenge.link}
                </a>
              </div>
              <div>
                <strong>Lichess Rating:</strong> {challenge.opponentRating}
              </div>
              <div>
                <strong>Upland ID:</strong> {challenge.uplandID}
              </div>
              <div>
                <strong>Lichess ID:</strong> {challenge.lichessID}
              </div>
              <div>
                <strong>Wager Amt:</strong> {challenge.wageramt}
              </div>
            </td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

const addNewChallenge = () => {
  //catch a new challenge, package into a challenge object and append to challenge_data
};

const reload = () => {
  //reload function
};

const App = () => {
  const challenge_data = [
    {
      name: 'Challenge 1',
      link: 'testlink.com',
      opponentRating: 1500,
      uplandID: 346462367,
      lichessID: 23671273,
      wageramt: '$134',
    },
    {
      name: 'Challenge 2',
      link: 'testlink.com',
      opponentRating: 1600,
      uplandID: 346462367,
      lichessID: 23671273,
      wageramt: '$432',
    },
  ];

  return (
    <div>
      <h1>Chess Challenges</h1>
      <ChessChallengesTable challenges={challenge_data} />
      <br />
      <br />
      <button onClick={addNewChallenge}>Add New Challenge</button>
      <br />
      <button onClick={reload}>Reload</button>
      <br />
      <br />
      <label>
          Enter Lichess ID
          <br />
          <input
            type="text"
          />
        </label>
    </div>
  );
};



export default App;
