import React from "react";
import { Form, Button, Container, Col, Card } from "react-bootstrap";
import axios from "axios";

function UserLogout() {
    const url = process.env.REACT_APP_API_URL + '/api/users/logout';
    const tokenApp = sessionStorage.getItem('token');
    const handleSubmit = event => {
        event.preventDefault();
        axios.delete(url, {
            headers: {
                'Authorization': `Token ${tokenApp}`
            }
        })
            .then(res => {
                sessionStorage.setItem("token", "");
                window.location.replace("/")
            })
    };

    return (
        <Container>
            <Col md={{ span: 6, offset: 3 }} >
                <Card >
                    <Card.Header className="mb-4">Logout</Card.Header>
                    <Card.Text>
                        <Container className="mb-4">
                            <Col className="mb-4">
                                Are you sure you want to log out?
                            </Col>
                            <Form onSubmit={handleSubmit}>
                                <Button size="lg" type="submit">
                                    Logout
                                </Button>
                            </Form>
                        </Container>
                    </Card.Text>
                </Card>
            </Col>
        </Container>
    )
};

export default UserLogout;