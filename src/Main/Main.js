import React from 'react'
import { BrowserRouter as Router, Route } from 'react-router-dom';


import Sidebar from '../Components/Sidebar/Sidebar'

import User from '../Pages/User/User'
import Miner from '../Pages/Miner/Miner'
import Nft from '../Pages/Nft/Nft'
import CrowdSourcing from '../Pages/Crowdsourcing/CrowdSourcing'

function Main() {
    return (
        <div>
            <Router>
            <Sidebar/>
            <Route path='/' exact component={User} />
            <Route path='/miner' exact component={Miner} />
            <Route path='/crowdSourcing' exact component={CrowdSourcing} />
            <Route path='/nft' component={Nft} />
            </Router>
        </div>
    )
}

export default Main