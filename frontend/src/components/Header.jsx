import React from 'react'
import { Link, useNavigate } from 'react-router-dom'
import { useContext } from 'react'
import { AuthContext } from '../AuthProvider.jsx'


const header = () => {
  const {isLoggedIn, setIsLoggedIn} = useContext(AuthContext)
  const navigate = useNavigate();

   const handleLogout = () =>{
    localStorage.removeItem('accessToken')
    localStorage.removeItem('refreshToken')
    setIsLoggedIn(false)
    console.log('Logged out');
    navigate('/login')
  }

  return (
    <>
    <nav className="navbar bg-body-tertiary">
        <div className="container-fluid">

            <a className="navbar-brand">Stock Predictor</a>
            <form className="d-flex" role="search">

             {isLoggedIn ? (
              <Link className="btn btn-outline-success" to={"/login"}>Logout</Link>
             ):(
              <>
              <Link className="btn btn-outline-success" to={"/login"}>Login</Link>
              <Link className="btn btn-outline-success" to={"/register"}>Sign-up</Link>
              </>
             )}
            </form>
        </div>
        </nav>
               
    </>
  )
}

export default header