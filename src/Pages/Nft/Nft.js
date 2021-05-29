import React, {useState, useEffect} from 'react';
import Carousel from 'react-elastic-carousel';
import Nftcard from '../../Components/Cards/Nftcard';
import Coin from '../../Components/Coin/Coin'
import axios from 'axios'
import Modal from 'react-modal'

const breakPoints = [
    { width: 1, itemsToShow: 1 },
    { width: 550, itemsToShow: 2 },
    { width: 768, itemsToShow: 3 },
    { width: 1200, itemsToShow: 4 },
  ];

function Nft() {
    const [coins, setcoins] = useState([])
    const [Search, SetSearch] = useState('')
    const [ModalOpen2, setModalOpen2] = useState(false)
    
    
    useEffect(()=>{
      axios.get('https://api.coingecko.com/api/v3/coins/markets?vs_currency=inr&order=market_cap_desc&per_page=100&page=1&sparkline=false')
      .then(res=>{
        setcoins(res.data)
        console.log(res.data)
      }).catch(error=>alert('Issue Loading Api'))
    },[])
  
    const handleChange = e =>{
      SetSearch(e.target.value)
    }
    
  
    const SearchFilter = coins.filter(coins =>
      coins.name.toLowerCase().includes(Search.toLowerCase())
      )
    
    return (
        <div className='user'>        
        <div className='Heading'>NFT Dashboard</div>
        <Carousel breakPoints={breakPoints}>
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        <Nftcard Name='Image' Price='1.5ETH' Img="" />
        </Carousel>


        
        <form className='Modal1Display'>
            <h2 class="fs-title">Make your own NFTs</h2>
            <input type="file" id="myFile" name="filename"/>
            <input type="submit" className='submit-button'/>
        </form>
        

        {/* <div>
      
       <div className='title'>CRYPTOTRACKER</div>
       <form>
       <input type='text' placeholder='search coin' onChange={handleChange} />
       </form>
       {SearchFilter.map(coins=> {
         return(
           <Coin 
           key={coins.id}
           name={coins.name}
           img={coins.image}
           symbol={coins.symbol}
           price={coins.current_price}
           Cap={coins.market_cap}
           priceChange={coins.price_change_percentage_24h}
           
           />
            
         )
       })}
      <br/>
    </div>
    */}
    
        </div>
    
    )
}

export default Nft