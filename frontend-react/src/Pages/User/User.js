import React, { useState } from 'react';
import './User.scss'
import Modal from 'react-modal'

import Card1 from '../../Components/Cards/Card1'


function User() {
    const [ModalOpen2, setModalOpen2] = useState(false)
    const [ModalOpen1, setModalOpen1] = useState(false)

    return (
        <div className='user'>
            <div className='Heading'>User Dashboard</div>
            <div className='cardlayout'>
                <Card1 Title='Public Key' Content= '0x18***d7f' />
                <Card1 Title='Eternity Coins' Content='10.1505' />
                <Card1 Title='Eternity Credits' Content='10' />
            </div>
            <div className='buttonalign'>
                <div>

                    <span className='modal-initbuttonsspan'><button onClick={() => setModalOpen1(true)} className='modal-initbuttons'>Login</button></span>

                    <Modal isOpen={ModalOpen1} onRequestClose={() => setModalOpen1(false)} className='modal'>
                        <form className='Modal1Display' method="post" action="http://127.0.0.1:5000/login">
                            <h2 class="fs-title">Login</h2>
                            <input type="text" name="name" placeholder="Name" /><br />
                            <input type="password" name="private_key" placeholder="Private Key" /><br />
                            <button className='button-modal'><input type="submit" value="Submit" /></button>
                            <button onClick={() => setModalOpen1(false)} className='button-modal'>Close</button>
                        </form>
                    </Modal>
                </div>

                <div>

                    <span className='modal-initbuttonsspan'><button onClick={() => setModalOpen2(true)} className='modal-initbuttons'>Payments</button></span>

                    <Modal isOpen={ModalOpen2} onRequestClose={() => setModalOpen2(false)}>
                        <form className='Modal1Display' method="post" action="http://127.0.0.1:5000/makepayment">
                            <h2 class="fs-title">Make Payment</h2>
                            <input type="text" name="addres_key" placeholder="Sender Private Key" /><br />
                            <input type="text" name="private_key" placeholder="Reciever Addres Key" /><br />
                            <input type="text" name="amount" placeholder="Amount" /><br />
                            <button className='button-modal'><input type="submit" value="Submit" /></button>
                            <button onClick={() => setModalOpen2(false)} className='button-modal'>Close</button>
                        </form>
                    </Modal>

                </div>
            </div>
            <div className='table-blocks'>
                <div>
                    <header class="projects-header">
                        <div class="title">Latest Blocks</div>

                    </header>
                    <table class="projects-table">
                        <thead>
                            <tr>
                                {/* Aryan Edit the Title in this*/}
                                <th>Address</th>
                                <th> Hash</th>
                                <th>Previous Hash</th>
                                <th>Amount</th>

                            </tr>
                        </thead>


                        {/* Edit the api in this*/}
                        <tr>
                            <td>
                                <p>0x539cC27538ccA760e11260cb7e60505279ff9339</p>
                                <p></p>
                            </td>
                            <td>
                                <p>5957b313c1653a9fdf97e25373bd7641a456e4d75789110c7092a71a03a67c33</p>
                                <p></p>
                            </td>
                            <td class="member">
                                <div class="member-info">
                                    <p>0c08c0d223af7f43cbf3543b4a3559cd0cc0b37893c38a2fc8319e204e80c2c2</p>
                                    <p></p>
                                </div>
                            </td>
                            <td>
                                <p>1</p>
                                <p></p>
                            </td>

                        </tr>
                    </table>
                </div>
            </div>
        </div>

    )
}

export default User
