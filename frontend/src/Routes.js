import React from "react";
import {Routes, Route} from 'react-router-dom';
import Home from './pages/Home';
import Profile from './pages/Profile';
import Login from './pages/Login';

export default function Routing () {
    return(
     <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/profile" element={<Profile />}/>
        <Route path="/login" element={<Login />} />
     </Routes>
    );
}