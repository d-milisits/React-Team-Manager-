import React, { useState } from 'react';
import './Manage.css';

function Manage() {

  const [coachName, setCoach] = useState("");
  const [teamName, setName] = useState("");
  const [playerName, setPlayerName] = useState("");
  const [playerTeam, setPlayerTeam] = useState("");
  const [removePlayer, setRemovePlayer] = useState("");
  // All states used to fetch & store data from input fields. 

  const createTeam = async () => {
    const data = JSON.stringify({coach:coachName, name:teamName});
    await fetch('http://localhost:5000/api/add', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: data
    });
  }
  // Sends post JSON data including coach & team state values, obtained by input fields below.

  const addToTeam = async () => {
    const data = JSON.stringify({player:playerName, team:playerTeam});
    await fetch('http://localhost:5000/api/add_player', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: data
    });
  }
  // Sends post JSON data including player & team name state values, obtained by input fields below.


  const removePlayerFrom = async () => {
    const data = JSON.stringify({player:removePlayer});
    await fetch('http://localhost:5000/api/remove_player', {
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/json'
      },
      body: data
    });
  }
  // Sends post JSON data of desired player (to be removed) name, obtained by input field below.

  return (
    <div>
      <h1>Create a new team!</h1>
      <label for="coach">Coach name: </label>
      <input type="text" id="coach" placeholder="Coach Name" onChange={e => setCoach(e.target.value)}/><br></br>
      <label for="team">Team name: </label>
      <input type="text" id="team" placeholder="Team Name" onChange={e => setName(e.target.value)}/><br></br>
      <button id="btn" onClick={e => createTeam()}>Create</button>
      {/* Store data in states and calls create team function, which sends data to flask route. */}
      <br></br><br></br>
      <h1>Add players to team:</h1>
      <label for="player">Player name: </label>
      <input type="text" id="player" placeholder="Player Name" onChange={e => setPlayerName(e.target.value)}/><br></br>
      <label for="playerTeam">Team name: </label>
      <input type="text" id="playerTeam" placeholder="Team Name" onChange={e => setPlayerTeam(e.target.value)}/><br></br>
      <button id="btn" onClick={e => addToTeam()}>Add</button>
      {/* Store data in states and calls add to team function, which sends data to flask route. */}
      <h1>Remove player from the league:</h1>
      <label for="player">Player name: </label>
      <input type="text" id="remove" placeholder="Player Name" onChange={e => setRemovePlayer(e.target.value)}/><br></br>
      <button id="btn" onClick={e => removePlayerFrom()}>Remove</button>
      {/* Store data in states and calls remove from league function, which sends data to flask route. */}
    </div>
  )
}

export default Manage;
