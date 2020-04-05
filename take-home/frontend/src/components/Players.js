import React, { useState } from 'react';
import './Players.css';

function Players() {
  const [teamName, setTeamName] = useState("");
  const [players, setPlayers] = useState([]);
  // States used to store teamName (input variable) and array of player names (obtained from flask route and set in getPlayers below).

  const getPlayers = async () => {
    const data = JSON.stringify({team:teamName});
    const players = await fetch('http://localhost:5000/api/players', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body:data
    })
    // Sends team name to flask route (obtained from input field and set in teamName state).
      const output = await players.json();
      // Gets data sent from flask route.
      setPlayers(output.players);
  }
  // Function to output all players from given team. 
  // Sends post request with desired team name to Flask route, then retrieves output from SQL database (returned from flask in JSON form).

  const player_list = players.map(player => {
    return (
      <div>
        <h3>{player}</h3>
      </div>
    )
  })
  // Map (iterate) through player name array once obtained through Flask route and display them on screen in h tags. 

  return (
    <div>
      <h1>Please type in a name to see its players!</h1>
      <h3>Please type the correct team name. View team list to confirm.</h3>
      <input id="name" type="text" placeholder="Team Name Here" onChange={e => setTeamName(e.target.value)}/><br></br>
      {/* Sets team name state through input field */}
      <button id="btn" onClick={e => getPlayers()}>View Players</button>
      {/* Button calls getPlayers function, which sends to and receives data from Flask route. */}
      <div className="list">
        {player_list}
        {/* Mapped players list */}
      </div>
    </div>
  )
}

export default Players;