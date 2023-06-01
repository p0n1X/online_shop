import React, { useEffect, useState } from "react";
import { Button, Card, Container, Form, Col, Row, FloatingLabel, Alert } from "react-bootstrap";
import axios from "axios";
import { Link, useParams } from 'react-router-dom';
import Sidebar from "../sidebar";

function AdminCategoryEdit() {
    const { id } = useParams();
    const [name, setName] = useState("");
    const [islogin, setIslogin] = useState(false);
    const login_url = process.env.REACT_APP_API_URL + '/api/users/login';
    const category_url = process.env.REACT_APP_API_URL + '/api/categories/' + id;;
    const tokenApp = sessionStorage.getItem('token');

    const handleSubmit = event => {
        event.preventDefault();

        axios.put(category_url, {
            name: name,
            category_id: id,
        })
            .then(res => {
                window.location.replace("/admin/categories/")
            })
    };

    useEffect(() => {
        if (tokenApp) {
            axios.get(login_url, {
                headers: {
                    'Authorization': `Token ${tokenApp}`
                }
            }).then(res => {
                setIslogin(res.data['login'])
            })
        }
        axios.get(category_url).then(res => {
            setName(res.data['name']);
        })
    }, []);

    if (islogin) {
        return (
            <Container>
                <Row>
                    <Sidebar />
                    <Col>
                        <Card>
                            <Card.Header className="py-3"> Edit Product</Card.Header>
                            <Card.Body>
                                <Container>
                                    <Form onSubmit={handleSubmit}>
                                        <Form.Group size="lg" controlId="name" className="mb-3">
                                            <FloatingLabel label="Category Name">
                                                <Form.Control
                                                    autoFocus
                                                    type="name"
                                                    value={name}
                                                    onChange={(e) => setName(e.target.value)}
                                                />
                                            </FloatingLabel>
                                        </Form.Group>
                                        <Button type="submit">
                                            Submit
                                        </Button>
                                        <Link style={{ float: 'right' }} to={`/admin/categories`}><Button variant="secondary">Back</Button></Link>
                                    </Form>
                                </Container>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        )

    } else {
        return (
            <Alert key="danger" variant="danger">
                You do not have permission to view this page!
            </Alert>
        )
    };

};

export default AdminCategoryEdit;