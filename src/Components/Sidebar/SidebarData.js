import React from 'react';
import * as BiIcons from 'react-icons/bi';
import * as FiIcons from 'react-icons/fi';
import * as RiIcons from 'react-icons/ri';

export const SidebarData = [
  {
    title: 'User',
    path: '/',
    icon: <FiIcons.FiHome />,
    cName: 'nav-text'
  },
  {
    title: 'Miner',
    path: '/miner',
    icon: <RiIcons.RiBitCoinLine />,
    cName: 'nav-text'
  },
  {
    title: 'Nft',
    path: '/nft',
    icon: <FiIcons.FiImage />,
    cName: 'nav-text'
  },
  {
    title: 'CrowdSourcing',
    path: '/crowdSourcing',
    icon: <BiIcons.BiDonateHeart />,
    cName: 'nav-text'
  }
];