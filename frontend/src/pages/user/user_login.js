import React, { useEffect, useState } from "react";
import { Form, FloatingLabel, Button, Container, Card, Col } from "react-bootstrap";
import axios from "axios";
import UserLogout from "./user_logout";

function UserLogin() {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
    const [islogin, setIslogin] = useState(false);
    const url = process.env.REACT_APP_API_URL + '/api/users/login';
    const tokenApp = sessionStorage.getItem('token');
    const handleSubmit = event => {
        event.preventDefault();

        axios.post(url, {
            username: username,
            password: password
        })
            .then(res => {
                if (res.data['message']) {
                    alert(res.data['message'])
                } else {
                    sessionStorage.setItem("token", res.data['token']);
                    window.location.replace("/")
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
        }
    }, []);

    if (islogin) {
        return <UserLogout />;
    } else {
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
                                        Login
                                    </Button>
                                </Form>
                            </Container>
                        </Card.Text>
                    </Card>
                </Col>
            </Container>
        )
    }

};

export default UserLogin;