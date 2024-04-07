import React, { useState } from 'react';
import './App.css'

const HoverPopup = ({ text, children }) => {
    const [isHovered, setHovered] = useState(false);
  
    const handleMouseEnter = () => { setHovered(true); };
    const handleMouseLeave = () => { setHovered(false); };
  
    return (
      <div
        onMouseEnter={handleMouseEnter}
        onMouseLeave={handleMouseLeave}
        style={{ position: 'relative', cursor: 'pointer'}}
      >
        
        {children}
        {isHovered && (
          <div
            style={{
              position: 'absolute',
              top: '75%',
              left: '110%',
              width: '500px', // Adjust width to your preference
              height: '50%', // Adjust height to your preference
              backgroundColor: 'white',
              padding: '15px 20px',
              borderRadius: '4px',
              boxShadow: '0 0 5px rgba(0, 0, 0, 0.2)',
              zIndex: 1000,
              
            }}
          >
            {text}
          </div>
        )}

      </div>
    );
  };

export default HoverPopup