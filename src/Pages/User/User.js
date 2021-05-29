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
            <Card1 Title='TOTAL' Content='$45353'/>
            <Card1 Title='TOTAL' Content='$45353'/>
            <Card1 Title='TOTAL' Content='$45353'/>
            </div>
            <div className='buttonalign'>
            <div>
            
            <span className='modal-initbuttonsspan'><button onClick={()=>setModalOpen1(true)} className='modal-initbuttons'>Authenticate</button></span>
            
            <Modal isOpen={ModalOpen1} onRequestClose={()=>setModalOpen1(false)} className='modal'>
            <form className='Modal1Display'>
            <h2 class="fs-title">Authenticate</h2>
            <input type="text" name="email" placeholder="Email" /><br/>
            <input type="password" name="pass" placeholder="Password"/><br/>
            <button className='button-modal'>VERIFY</button>
            <button onClick={()=>setModalOpen1(false)} className='button-modal'>Close</button>
            </form>
            </Modal>
            </div> 
             
            <div>
            
            <span className='modal-initbuttonsspan'><button onClick={()=>setModalOpen2(true)} className='modal-initbuttons'>Payments</button></span>
            
            <Modal isOpen={ModalOpen2} onRequestClose={()=>setModalOpen2(false)}>
            <form className='Modal1Display'>
            <h2 class="fs-title">Authenticate</h2>
            <input type="text" name="senderKey" placeholder="Sender Key" /><br/>
            <input type="text" name="recieverKey" placeholder="Reciever Key"/><br/>
            <input type="text" name="recieverKey" placeholder="Amount"/><br/>
            <button className='button-modal'>VERIFY</button>
            <button onClick={()=>setModalOpen2(false)} className='button-modal'>Close</button>
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

export default User
