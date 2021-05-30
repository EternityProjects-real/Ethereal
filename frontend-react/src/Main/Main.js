import React from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom';


import Sidebar from '../Components/Sidebar/Sidebar'

import User from '../Pages/User/User'
import Miner from '../Pages/Miner/Miner'
import Nft from '../Pages/Nft/Nft'
import CrowdSourcing from '../Pages/Crowdsourcing/CrowdSourcing'
import Wallet from '../Pages/Wallet/Wallet'

function Main() {
    return (
        <div>
            <Router>
            <Sidebar/>
            <Route path='/' exact component={User} />
            <Route path='/miner' exact component={Miner} />
            <Route path='/crowdSourcing' exact component={CrowdSourcing} />
            <Route path='/nft' component={Nft} />
            <Route path='/wallet' component={Wallet} />
            </Router>
        </div>
    )
}

export default Main