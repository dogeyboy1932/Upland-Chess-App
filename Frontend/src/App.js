import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import { MainPage } from './Pages/MainPage';
import { LichessPage } from './Pages/LichessInfo';
import { EscrowPage } from './Pages/EscrowInfo';

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<MainPage />} />
          <Route path="/lichess" element={<LichessPage />} />
          <Route path="/escrow" element={<EscrowPage />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;