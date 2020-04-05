import React from 'react'
import { Link } from 'react-router-dom';
import './Header.css';

const Header = () => {
  return(
    <div className="home">
      <span>
        <Link id="click" to="/home">Home</Link>
        <Link id="click" to="/manage">Manage Teams</Link>
        <Link id="click" to="/teams">View Teams</Link>
        <Link id="click" to="/players">View Players By Team</Link>
        {/* Utilizes Link to re-route to other components, which are then rendered in App.js */}
      </span>
    </div>
  )
}

export default Header;