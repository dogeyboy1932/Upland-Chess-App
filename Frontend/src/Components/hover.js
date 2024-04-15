import React, { useState } from 'react';
import './../App.css'

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
          <div className='hover'> 
            {text} 
          </div>
        )}

      </div>
    );
  };

export default HoverPopup