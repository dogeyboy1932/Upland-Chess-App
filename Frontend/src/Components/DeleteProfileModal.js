import React, { useState} from 'react';
import axios from 'axios';
import Modal from 'react-modal';

import {BASE_URL as baseUrl} from "../FIXED_FRONTEND_VARIABLES"


Modal.setAppElement('#root');

const DeleteProfileModal = ({isDeleteOpen, setIsDeleteOpen}) => {

    const [uplandIDRemove, setUplandID] = useState('');
    const [passwordRemove, setPassword] = useState('');
    
    const [invalidPassword, setInvalidPassword] = useState(false)
    const [deleteError, setDeleteError] = useState(false)

    const openDeleteProfileModal = () => {
        setIsDeleteOpen(!isDeleteOpen);
    };

    const deleteProfile = async () => {
        const res = (await axios.post(baseUrl + '/deleteProfile', {uplandIDRemove, passwordRemove})).data;

        if (res === -1) {
            setDeleteError(true)
            setTimeout(() => setDeleteError(false), 3000);
        } else if (res === "Incorrect Password") {
            setInvalidPassword(true)
            setTimeout(() => setInvalidPassword(false), 3000);
        }

        setIsDeleteOpen(!isDeleteOpen);
    }

    return (
        <>
            <Modal
                isOpen={isDeleteOpen}
                onRequestClose={deleteProfile}
                contentLabel="Delete Profile Modal"
                className="modal-content"
            >
                <span className="close" onClick={openDeleteProfileModal}> &times; </span>
                <div className="smallHeader">Delete Profile</div>
                <br/>

                <label className=' important' htmlFor="create-username">Upland ID: </label>
                <input type="text" id="create-username" value={uplandIDRemove} className='user-input' onChange={(e) => setUplandID(e.target.value)} />
                <br />

                <label className=' important' htmlFor="login-password">Password: </label>
                <input type="password" id="login-password" value={passwordRemove} className='user-input' onChange={(e) => setPassword(e.target.value)} />
                <br />

                <button onClick={deleteProfile} className="submitButton"> Submit </button>
            </Modal>


            {deleteError && (
                <div className={`notification notification-error`}>
                    Invalid UplandID
                </div>
            )}

            {invalidPassword && (
                <div className={`notification notification-error`}>
                    Invalid Password
                </div>
            )}
        </>
  );
};

export {DeleteProfileModal}