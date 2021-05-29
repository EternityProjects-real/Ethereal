import React, { useState } from 'react';
import * as FaIcons from 'react-icons/fa';  
import { Link } from 'react-router-dom';
import { SidebarData } from './SidebarData';
import './Sidebar.scss';
import { IconContext } from 'react-icons';
import logo from '../../Assets/logo.png';

function Sidebar() {
  const [sidebar, setSidebar] = useState(false);

  const showSidebar = () => setSidebar(!sidebar);

  return (
    <>
      <IconContext.Provider value={{ color: '#f1f1f1' }}>
        <div className='navbar'>
          <Link to='#' className='menu-bars'>
            <FaIcons.FaBars onClick={showSidebar} />
          </Link>
        </div>
        <nav className={sidebar ? 'nav-menu' : 'nav-menu active'}>
          <ul className='nav-menu-items' >
            <li className='navbar-toggle'>
              <Link to='#' className='menu-bars2' onClick={showSidebar}>
                <FaIcons.FaBars />
              </Link>
            </li>
            {SidebarData.map((item, index) => {
              return (
                <li key={index} className={item.cName}>
                  <Link to={item.path}>
                    <span className='icons'>{item.icon}</span>
                    <span className='text'>{item.title}</span>
                  </Link>
                </li>
              );
            })}
            <div className='img'><a href="https://www.github.com"><img src={logo}/></a></div>
          </ul>
        </nav>
      </IconContext.Provider>
    </>
  );
}

export default Sidebar;