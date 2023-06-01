import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import { Form, FloatingLabel, Button, Container, Card, Col } from "react-bootstrap";
import UserLogout from "./user_logout";

function ProfileEdit() {
    const [islogin, setIslogin] = useState(false);
    const url = process.env.REACT_APP_API_URL + '/api/users/login';
    const tokenApp = sessionStorage.getItem('token');
    const user_url = process.env.REACT_APP_API_URL + '/api/users/info';
    const [userId, setUserId] = useState("");
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [address, setAddress] = useState("")
    const [email, setEmail] = useState("");

    const handleSubmit = event => {
        event.preventDefault();
        axios.put(user_url, {
            firstname: firstname,
            lastname: lastname,
            address: address,
            email: email,
            id: userId
        })
            .then(res => {
                if (res.data['message']) {
                    alert(res.data['message'])
                    window.location.replace("/profile")
                }
            })
    };
    
    
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
                setFirstname(res.data['first_name'])
                setLastname(res.data['last_name'])
                setAddress(res.data['address'])
                setEmail(res.data['email'])
                setUserId(res.data['id'])
            })
        }
    }, []);

    if (islogin) {
        return (
            <Container>
            <Col md={{ span: 6, offset: 3 }}>
                <Card >
                    <Card.Header className="mb-4">Edit profile</Card.Header>
                    <Card.Text>
                        <Container className="mb-4">
                            <Form onSubmit={handleSubmit}>
                                <Form.Group controlId="firstname" className="mb-4">
                                    <FloatingLabel label="First name">
                                        <Form.Control
                                            autoFocus
                                            type="text"
                                            value={firstname}
                                            onChange={(e) => setFirstname(e.target.value)}
                                        />
                                    </FloatingLabel>
                                </Form.Group>
                                <Form.Group controlId="lastname" className="mb-4">
                                    <FloatingLabel label="Last name">
                                        <Form.Control
                                            autoFocus
                                            type="text"
                                            value={lastname}
                                            onChange={(e) => setLastname(e.target.value)}
                                        />
                                    </FloatingLabel>
                                </Form.Group>
                                <Form.Group controlId="address" className="mb-4">
                                    <FloatingLabel label="Address">
                                        <Form.Control
                                            autoFocus
                                            type="text"
                                            value={address}
                                            onChange={(e) => setAddress(e.target.value)}
                                        />
                                    </FloatingLabel>
                                </Form.Group>
                                <Form.Group controlId="email" className="mb-4">
                                    <FloatingLabel label="Email">
                                        <Form.Control
                                            autoFocus
                                            type="email"
                                            value={email}
                                            onChange={(e) => setEmail(e.target.value)}
                                        />
                                    </FloatingLabel>
                                </Form.Group>
                                <Button type="submit" className="mb-4">
                                    Update
                                </Button>
                                <Link style={{ float: 'right' }} to={`/profile/`}><Button variant="secondary">Back</Button></Link>
                            </Form>
                        </Container>
                    </Card.Text>
                </Card>
            </Col>
        </Container>
        )
    } else {
        return <UserLogout />;
    }

};

export default ProfileEdit;