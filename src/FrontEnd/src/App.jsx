import { useState } from 'react'

import './App.css'
import Lista from './components/Membership/Lista'
import CreateAdmin from './components/Membership/admin'

function App() {


  return (
    <>
      <div>
        <Lista/>
        <CreateAdmin/>
      </div>
    </>
  )
}

export default App
