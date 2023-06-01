import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import { Container, Card, Col, Button } from 'react-bootstrap';
import UserLogout from "./user_logout";

function Profile() {
    const [islogin, setIslogin] = useState(false);
    const url = process.env.REACT_APP_API_URL + '/api/users/login';
    const tokenApp = sessionStorage.getItem('token');
    const user_url = process.env.REACT_APP_API_URL + '/api/users/info';
    const [username, setUsername] = useState("");
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [address, setAddress] = useState("")
    const [email, setEmail] = useState("");

    useEffect(() => {
        if (tokenApp) {
            axios.get(url, {
                headers: {
                    'Authorization': `Token ${tokenApp}`
                }
            }).then(res => {
                setIslogin(res.data['login'])
            })
            axios.get(user_url, {
                headers: {
                    'Authorization': `Token ${tokenApp}`
                }
            }).then(res => {
                setUsername(res.data['username'])
                setFirstname(res.data['first_name'])
                setLastname(res.data['last_name'])
                setAddress(res.data['address'])
                setEmail(res.data['email'])
            })
        }
    }, []);

    if (islogin) {
        return (
            <Container>
                <Col md={{ span: 6, offset: 3 }}>
                    <Card>
                        <Card.Header>Welcome, {username}</Card.Header>
                        <Card.Body>
                            <Card.Title>{firstname} {lastname}</Card.Title>
                            Address: {address}
                            <br />
                            Email: {email}
                            <Link style={{ float: 'right' }} to={`/profile/edit`}><Button variant="primary">Edit</Button></Link>
                        </Card.Body>
                    </Card>
                </Col>
            </Container>
        )
    } else {
        return <UserLogout />;
    }

};

export default Profile;