import React from 'react';

const UserDetails = ({ currentUserUplandID, currentUserLichessID }) => {
  return (
    <div style={{ marginRight: '20%', justifyContent: 'space-between' }}>
      <div className="detail">
        <div className="detail detail-box">
          Registered Upland ID:
        </div>
        <div className="detail detail-value" style={{ marginRight: '25px' }}>
          {currentUserUplandID}
        </div>
      </div>

      <div className="detail">
        <div className="detail detail-box">
          Registered Lichess ID:
        </div>
        <div className="detail detail-value">
          {currentUserLichessID}
        </div>
      </div>
    </div>
  );
};

export {UserDetails};