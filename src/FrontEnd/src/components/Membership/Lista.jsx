import React, { useState, useEffect } from 'react';
import './Lista.css'; // Importa tu archivo CSS
import { BASE_API_URL } from "../../constants";

export default function Lista() {
  const [Listas, setListas] = useState([]);

  useEffect(() => {
    fetch(`${BASE_API_URL}/api/Lista/`)
      .then(response => response.json())
      .then(data => setListas(data))
      .catch(error => console.error(error));
    
  }, []);

  return (
    <div>
      <h2>Lista</h2>
      <table className="Lista-table">
        <thead>
          <tr>
            <th>Usuario</th>
            <th>Contenido</th>
            <th>Pago</th>
            <th>Pagado</th>
          </tr>
        </thead>
        <tbody>
        {Listas.map(Lista => (
            <tr key={Lista.id}>
              <td>{Lista.nombre_usuario}</td>
              <td>{Lista.contenido}</td>
              <td>{Lista.pago}</td>
              <td>{Lista.pagado ? 'Si' : 'No'}</td>
            </tr>
          ))} 
        </tbody>
      </table>
    </div>
  );
  
}
