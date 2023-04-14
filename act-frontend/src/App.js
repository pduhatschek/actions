import './App.css';
import usersData from './users.json';
import { useState } from 'react';

function App() {
  const [users, setUsers] = useState(usersData.users);

  return (
    <div>
      <h1>Lista de usuários</h1>
      <ul>
        {users.map(user => (
          <li key={user.id}>
            <img src={user.avatar_url} alt={`Avatar de ${user.login}`} />
            <a href={user.html_url}>{user.login}</a>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
