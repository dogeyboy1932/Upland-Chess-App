import axios from 'axios';
import './../App.css'

const ChallengeDatabase = async () => {
    try {
      const response = await axios.post('/database');
      // console.log(response)
    
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
  
      // console.log(challengeData)  
      return challengeData
    } catch (error) {
      console.error('Error processing button click:', error);
      return ChallengeDatabase()
    }
  };

export {ChallengeDatabase};
