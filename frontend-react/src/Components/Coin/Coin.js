import React from 'react'
import './Coin.scss'

const Coin = ({name, img,symbol,price,Cap,priceChange}) => {
    return (
        <div>
        <table>
        <tr>
        <th><img src={img} alt='Logo' /></th>
        <th>{name}</th>
        <th>{symbol}</th>
        <th>₹{price}</th>
        
        {priceChange<0?(
           <th>{priceChange.toFixed(2)}%</th>
        ):(
           <th>{priceChange.toFixed(2)}%</th>
        )}
        <th>₹{Cap.toLocaleString()}</th>
        </tr>
        </table>
        </div>
    )
}

export default Coin;