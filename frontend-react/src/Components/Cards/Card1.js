import React from 'react';
import './Card1.scss';

function Card1({Title,Content}) {
    return (
        <div>
        <div className='card-container-dashboard'>
        <div className='title-container-dashboard'>
        <span className='title-dashboard'>{Title}</span>
        </div>
        <div className='content-dashboard'>
        <span>{Content}</span>
        </div>
        </div>
        </div>
    )
}

export default Card1
