import React from 'react'
import './Card2.scss'

function Card2({Title,Content}) {
    return (
        <div>
        <div className='card-container-starter'>
        <div className='title-container-starter'>{Title}</div>
        <div className='content-starter'>{Content}</div>
        </div>        
        </div>
    )
}

export default Card2
