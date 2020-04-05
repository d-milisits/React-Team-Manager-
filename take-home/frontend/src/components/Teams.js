import React, {useState} from 'react';
import './Teams.css';

function Teams() {
  const [teams, setTeams] = useState([]);
  // No inputs required, as this page just displays all teams currently in the league. 

  const getTeams = async () => {
    try{
      const teams = await fetch("http://localhost:5000/api/teams");
      const output = await teams.json();
      setTeams(output.teams);
      // Obtains list of teams through Flask route and sets teams state (array of player names)
      console.log(teams);
    } catch(err) {
      console.error(err)
    }
  }

  const team_list = teams.map(team => {
    return (
      <div>
        <h3>{team}</h3>
      </div>
    )
  })
  // Map through team name array in order to output to screen below.

  return (
    <div>
      <h1>Please click the button below to view the current list of teams:</h1>
      <button id="btn" onClick={e => getTeams()}>View Teams</button>
      {/* Button calls getTeams function */}
      <div className="list">
        {team_list}
        {/* Mapped team list */}
      </div>
    </div>
  )

}

export default Teams;