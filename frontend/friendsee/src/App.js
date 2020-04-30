import React, { useState } from 'react';
import axios from 'axios'

function App() {
  const api = axios.create({baseURL:'http://localhost:5000'})
  const [movie, setMovie] = useState([])

  function getMovies(){   
    
    api.get('/api/movie/',{})
    .then(response =>{      
      setMovie(response.data)
    })
    .catch((error) => {
      alert(error)
    })

  }

  return (
    <div className="App">
        <p>OI</p>
        <button onClick={getMovies}>click me</button>
        
        <p>Movies encontrados: {movie.length}</p>

        <ul>
          {movie.map(o => (
            <li key={o.titleOriginal}>
              <p> {o.titleOriginal}</p>
            </li>
          ))}          
        </ul>
    </div>
  );
}

export default App;
