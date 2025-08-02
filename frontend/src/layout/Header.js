import React from "react";
import { link } from 'react-router-dom';

export default function header(){
    
    return(
      <header>
        <nav>
         <link to="/">Home</link>
         <link to="/login">Login</link>
         <link to="/profile">profile</link>
        </nav>
      </header>
    );
}
