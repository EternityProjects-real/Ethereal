import React, {useState} from 'react'
import './CrowdFunding.scss'
import Modal from 'react-modal'

function CrowdFunding({Title, desc,but}) {
    const [ModalOpen3, setModalOpen3] = useState(false)
    return (
        <div className='user'>
        <div className='container-donation'>
        <div className='title-donation'>{Title}</div>
        <div className='content-donation'>{desc}</div>
        <button className='button-donation' onClick={()=>setModalOpen3(true)}>{but}</button>
        </div>
        

        
        
        <Modal isOpen={ModalOpen3} onRequestClose={()=>setModalOpen3(false)}>
        <form className='Modal1Display'>
            <h2 class="fs-title">{Title}</h2>
            <input type="text" name="senderKey" placeholder="Sender Key" /><br/>
            <input type="text" name="recieverKey" placeholder="Reciever Key"/><br/>
            <input type="text" name="recieverKey" placeholder="Amount"/><br/>
            <button className='button-modal'>VERIFY</button>
            <button onClick={()=>setModalOpen3(false)} className='button-modal'>Close</button>
            </form>
        </Modal>
        
        </div>
    ) 
}

export default CrowdFunding
