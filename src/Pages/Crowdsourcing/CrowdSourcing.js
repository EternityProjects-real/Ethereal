import React from 'react'
import CrowdFunding from '../../Components/Cards/CrowdFundingCard';
import './CrowdSourcing.scss'
function CrowdSourcing() {
    return (
        <div>
            <CrowdFunding Title='Covid-19' desc='Need Help' but='Support people' />
            <form className='Modal1Display' method="post" action="http://127.0.0.1:5000/crowdsourcing">
            <h2 class="fs-title">Make your own Fundraiser</h2>
            <input type="text" id="text" placeholder="Title" name="title_desc"/>
            <input type="text" id="text" placeholder="Decription" name="problem_desc"/>
            <input type="text" id="text" placeholder="Value " name="target_required"/>
            <input type="text" id="text" placeholder="Private Key" name="private_key"/>
            <input type="submit" className='submit-button'/>
        </form>
        </div>
    )
}

export default CrowdSourcing
 