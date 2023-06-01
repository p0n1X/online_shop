import React, { useState } from "react";
import { Form, FloatingLabel, Button, Container, Card, Col } from "react-bootstrap";
import axios from "axios";

function Register() {
    const [username, setUsername] = useState("");
    const [firstname, setFirstname] = useState("");
    const [lastname, setLastname] = useState("");
    const [address, setAddress] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const url = process.env.REACT_APP_API_URL + '/api/users/';

    const handleSubmit = event => {
        event.preventDefault();

        axios.post(url, {
            username: username,
            firstname: firstname,
            lastname: lastname,
            address: address,
            email: email,
            password: password
        })
            .then(res => {
                if (res.data['message']) {
                    alert(res.data['message'])
                    window.location.replace("/")
                }
            })
    };

    return (
        <Container>
            <Col md={{ span: 6, offset: 3 }}>
                <Card >
                    <Card.Header className="mb-4">Login</Card.Header>
                    <Card.Text>
                        <Container className="mb-4">
                            <Form onSubmit={handleSubmit}>
                                <Form.Group controlId="username" className="mb-4">
                                    <FloatingLabel label="Username">
                                        <Form.Control
                                            autoFocus
                                            type="username"
                                            value={username}
                                            onChange={(e) => setUsername(e.target.value)}
                                        />
                                    </FloatingLabel>
                                </Form.Group>
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
                                <Form.Group controlId="password" className="mb-4">
                                    <FloatingLabel label="Password">
                                        <Form.Control
                                            type="password"
                                            value={password}
                                            onChange={(e) => setPassword(e.target.value)}
                                        />
                                    </FloatingLabel>
                                </Form.Group>
                                <Button type="submit" className="mb-4">
                                    Register
                                </Button>
                            </Form>
                        </Container>
                    </Card.Text>
                </Card>
            </Col>
        </Container>
    )

};

export default Register;