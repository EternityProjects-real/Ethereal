import React from 'react'
import './Nftcard.scss'

function Nftcard({Name,Price,Img}) {
    return (
        
        <div class="card">
        <div class="card__image-holder">
          <img class="card__image" src={Img} alt="Nft" />
        </div>
        <div class="card-title">
          <h2>
             {Name}
              <small>{Price}</small>
          </h2>
        </div>
    
      </div>
        
    )
}

export default Nftcard
