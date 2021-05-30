import React from 'react'

function Wallet() {
    return (

        <div className='user'>
        <div className='Heading'>Merchant Transaction</div>
        <form className='Modal1Display' method="post" action="http://127.0.0.1:5000/sellwallet">
        <h2 class="fs-title">Merchant Transactions</h2>
        <input type="Text" placeholder="Phone No" name="mobile_no"/>
        <input type="Text" placeholder="Amount" name="amount"/>
        <input type="submit" className='submit-button' value="Submit"/>
        </form>
        </div>
    )
}

export default Wallet