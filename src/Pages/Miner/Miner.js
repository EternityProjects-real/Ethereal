import React, { useState } from 'react'
import './Miner.scss'
import Modal from 'react-modal'
import Card1 from '../../Components/Cards/Card1'

function Miner() {
    const [ModalOpen2, setModalOpen2] = useState(false)
    const [ModalOpen1, setModalOpen1] = useState(false)
    return (
        <div className='user'>
            <div className='Heading'>Miner Dashboard</div>
            <div className='cardlayout'>
                <Card1 Title='Public Key' Content='$45353' />
                <Card1 Title='Eternity Coins' Content='$45353' />
                <Card1 Title='Eternity Credits' Content='$45353' />
            </div>
            <div className='buttonalign'>
                <div>

                    <span className='modal-initbuttonsspan'><button onClick={() => setModalOpen1(true)} className='modal-initbuttons'>Authenticate</button></span>

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

                    <span className='modal-initbuttonsspan'><button onClick={() => setModalOpen2(true)} className='modal-initbuttons'>Mine</button></span>

                    <Modal isOpen={ModalOpen2} onRequestClose={() => setModalOpen2(false)}>
                        <form className='Modal1Display' method="post" action="http://127.0.0.1:5000/mine">
                            <h2 class="fs-title">Mine</h2>
                            <input type="text" name="private_key" placeholder="Enter Private Key" /><br />
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
                                <p>177,789</p>
                                <p></p>
                            </td>
                            <td>
                                <p>236x4576567x57</p>
                                <p></p>
                            </td>
                            <td class="member">
                                <div class="member-info">
                                    <p>Random Miner</p>
                                    <p></p>
                                </div>
                            </td>
                            <td>
                                <p>$4,670</p>
                                <p></p>
                            </td>

                        </tr>
                    </table>
                </div>
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
                                <p>177,789</p>
                                <p></p>
                            </td>
                            <td>
                                <p>236x4576567x57</p>
                                <p></p>
                            </td>
                            <td class="member">
                                <div class="member-info">
                                    <p>Random Miner</p>
                                    <p></p>
                                </div>
                            </td>
                            <td>
                                <p>$4,670</p>
                                <p></p>
                            </td>

                        </tr>
                    </table>
                </div>
            </div>

        </div>
    )
}

export default Miner
