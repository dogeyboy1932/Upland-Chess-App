import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './App.css'

const HoverPopup = ({ text, children }) => {
    const [isHovered, setHovered] = useState(false);
  
    const handleMouseEnter = () => {
      setHovered(true);
    };
  
    const handleMouseLeave = () => {
      setHovered(false);
    };
  
    return (
      <div
      onMouseEnter={handleMouseEnter}
      onMouseLeave={handleMouseLeave}
      style={{ position: 'relative', display: 'inline-block', backgroundColor: 'red'}}
    >
      {children}
      {isHovered && (
        <div
          style={{
            position: 'absolute',
            top: '50%',
            left: '50%',
            backgroundColor: 'tan',
            padding: '8px',
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