import React, { useState} from 'react';
import axios from 'axios';
import Modal from 'react-modal';

import {BASE_URL as baseUrl} from "../../FIXED_FRONTEND_VARIABLES"


// FIX THIS: CLEAN THIS PAGE UP
Modal.setAppElement('#root');

const DeleteProfileModal = ({isDeleteOpen, setIsDeleteOpen}) => {

    const [uplandIDRemove, setUplandID] = useState('');
    const [passwordRemove, setPassword] = useState('');

    const openDeleteProfileModal = () => {
        setIsDeleteOpen(!isDeleteOpen);
    };

    const deleteProfile = async () => {
        await axios.post(baseUrl + '/deleteProfile', {uplandIDRemove, passwordRemove});
        
        setIsDeleteOpen(!isDeleteOpen);
    }

    return (
        <Modal
            isOpen={isDeleteOpen}
            onRequestClose={deleteProfile}
            contentLabel="Create Profile Modal"
            style={{
            overlay: {
                backgroundColor: 'rgba(0, 0, 0, 0.5)',
            },
            content: {
                top: '50%',
                left: '50%',
                right: 'auto',
                bottom: 'auto',
                marginRight: '-50%',
                transform: 'translate(-50%, -50%)',
                width: '500px', // Adjust the width as needed
                height: '500px', // Adjust the height as needed
            },
            }}
        >
            <span className="close" onClick={openDeleteProfileModal}>
            &times;
            </span>
            <div className="smallHeader">Delete Profile</div>

            <br/>
            <label className=' important' htmlFor="create-username">Upland ID: </label>
            <input type="text" id="create-username" value={uplandIDRemove} className='user-input' onChange={(e) => setUplandID(e.target.value)} />
            <br />

            <label htmlFor="login-password">Password: </label>
            <input type="password" id="login-password" value={passwordRemove} className='user-input' onChange={(e) => setPassword(e.target.value)} />
            <br />

            <button onClick={deleteProfile} className="submitButton"> Submit </button>

        </Modal>
  );
};

export {DeleteProfileModal}