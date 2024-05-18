import axios from 'axios';
import './../App.css'

import {BASE_URL as baseUrl} from "../FIXED_FRONTEND_VARIABLES"


const RenderDatabase = async () => {
    try {
      const response = await axios.post(baseUrl + '/database');
      // console.log(response);
      
      const challengeTable = response.data.array;
      const challengeData = []

      if (challengeTable != null) {
        for (let i = 0; i < challengeTable.length; i++) {
          let data = {
            name: 'Challenge ' + (i + 1),
            
            lichessID: challengeTable[i][0],
            opponentRating: challengeTable[i][1],
            wageramt: challengeTable[i][2],
            link: challengeTable[i][3],
            uplandID: challengeTable[i][4],
            accepted: challengeTable[i][5],
            accepter: challengeTable[i][6],
            readyStatus: challengeTable[i][7],
            escrowId: challengeTable[i][8]
          }
  
          challengeData.push(data)
        }
      }
  
      return challengeData
    } catch (error) {
      console.error('Error processing button click:', error);
      // return RenderDatabase()
    }
  };

export {RenderDatabase};
