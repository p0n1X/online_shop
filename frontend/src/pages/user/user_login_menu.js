import React, { useEffect, useState } from "react";
import axios from "axios";
import { Link } from 'react-router-dom';
import { NavDropdown } from 'react-bootstrap';

function UserLoginMenu() {
    const [islogin, setIslogin] = useState(false);
    const url = process.env.REACT_APP_API_URL + '/api/users/login';
    const tokenApp = sessionStorage.getItem('token');

    useEffect(() => {
        if (tokenApp) {
            axios.get(url, {
                headers: {
                    'Authorization': `Token ${tokenApp}`
                }
            }).then(res => {
                setIslogin(res.data['login'])
            })
        }
    }, []);

    if (islogin) {
        return (
            <div>
                <NavDropdown.Item as={Link} to={`/admin`}>Admin panel</NavDropdown.Item>
                <NavDropdown.Item as={Link} to={`/profile`}>Profile</NavDropdown.Item>
                <NavDropdown.Divider />
                <NavDropdown.Item as={Link} to={`/logout`}>Logout</NavDropdown.Item>
            </div>
        )
    } else {
        return (
            <div>
                <NavDropdown.Item as={Link} to={`/register`}>Register</NavDropdown.Item>
                <NavDropdown.Item as={Link} to={`/login`}>Login</NavDropdown.Item>
            </div>
        )
    }

};

export default UserLoginMenu;