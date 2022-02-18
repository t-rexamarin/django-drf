import React from 'react';
import {Link} from 'react-router-dom';

const MenuItem = ({menuLink, i}) => {
    return (
        <li className="nav-item">
            <Link key={i} className="nav-link" to={menuLink.href}>{menuLink.name}</Link>
        </li>
    )
}

const Menu = ({menuLinks}) => {
    return (
        <header>
            <nav className="navbar navbar-expand-lg navbar-light bg-white fixed-top">
                <div className="container-fluid">
                    <button
                            className="navbar-toggler"
                            type="button"
                            data-mdb-toggle="collapse"
                            data-mdb-target="#navbarExample01"
                            aria-controls="navbarExample01"
                            aria-expanded="false"
                            aria-label="Toggle navigation"
                    >
                        <i className="fas fa-bars"></i>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarExample01">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            {menuLinks.map((menuLink, i) => <MenuItem menuLink={menuLink} key={i}/>)}
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
    )
}

/*
const Menu = () => {
    return (
        <header>
            <nav className="navbar navbar-expand-lg navbar-light bg-white fixed-top">
                <div className="container-fluid">
                    <button
                            className="navbar-toggler"
                            type="button"
                            data-mdb-toggle="collapse"
                            data-mdb-target="#navbarExample01"
                            aria-controls="navbarExample01"
                            aria-expanded="false"
                            aria-label="Toggle navigation"
                    >
                        <i className="fas fa-bars"></i>
                    </button>
                    <div className="collapse navbar-collapse" id="navbarExample01">
                        <ul className="navbar-nav me-auto mb-2 mb-lg-0">
                            <li className="nav-item active">
                                <a className="nav-link" aria-current="page" href="/">Users list</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Project 2</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Project 3</a>
                            </li>
                            <li className="nav-item">
                                <a className="nav-link" href="#">Project 4</a>
                            </li>
                        </ul>
                    </div>
                </div>
            </nav>
        </header>
    )
}
*/

export default Menu;