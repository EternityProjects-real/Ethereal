import React from 'react'
import CrowdFunding from '../../Components/Cards/CrowdFundingCard';
import './CrowdSourcing.scss'
function CrowdSourcing() {
    return (
        <div>
            <CrowdFunding Title='Covid-19' desc='Need Help' but='Support people' />
            <form className='Modal1Display'>
            <h2 class="fs-title">Make your own Fundraiser</h2>
            <input type="text" id="text" placeholder="Title"/>
            <input type="text" id="text" placeholder="Decription"/>
            <input type="text" id="text" placeholder="Value "/>
            <input type="submit" className='submit-button'/>
        </form>
        </div>
    )
}

export default CrowdSourcing
 