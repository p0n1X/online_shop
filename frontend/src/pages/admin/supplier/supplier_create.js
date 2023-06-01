import React, { useEffect, useState } from "react";
import { Button, Container, Card, Form, Row, Col, FloatingLabel } from "react-bootstrap";
import axios from "axios";
import UserLogin from "../../user/user_login";
import { Link } from 'react-router-dom';
import Sidebar from "../sidebar";


function SupplierCreate() {
    const [name, setName] = useState("");
    const [price, setPrice] = useState("");
    const [islogin, setIslogin] = useState(false);
    const url = process.env.REACT_APP_API_URL + '/api/users/login';
    const supplier_url = process.env.REACT_APP_API_URL + '/api/suppliers/';
    const tokenApp = sessionStorage.getItem('token');

    const handleSubmit = event => {
        event.preventDefault();

        axios.post(supplier_url, {
            name: name,
            price: price,
        })
            .then(res => {
                if (res.data['message']) {
                    alert(res.data['message'])
                    window.location.replace("/admin/suppliers")
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
        return (
            <Container>
                <Row>
                    <Sidebar />
                    <Col>
                        <Card>
                            <Card.Header className="py-3">Create new supplier</Card.Header>
                            <Card.Body>
                                <Container>
                                    <Form onSubmit={handleSubmit}>
                                        <Form.Group size="lg" controlId="name" className="mb-3">
                                            <FloatingLabel label="Supplier Name">
                                                <Form.Control
                                                    autoFocus
                                                    type="name"
                                                    value={name}
                                                    onChange={(e) => setName(e.target.value)}
                                                />
                                            </FloatingLabel>
                                        </Form.Group>
                                        <Form.Group size="lg" className="mb-3" controlId="price">
                                            <FloatingLabel label="Price">
                                                <Form.Control
                                                    type="number"
                                                    value={price}
                                                    onChange={(e) => setPrice(e.target.value)}
                                                />
                                            </FloatingLabel>
                                        </Form.Group>
                                        <Button type="submit">
                                            Submit
                                        </Button>
                                        <Link style={{ float: 'right' }} to={`/admin/suppliers`}><Button variant="secondary">Back</Button></Link>
                                    </Form>
                                </Container>
                            </Card.Body>
                        </Card>
                    </Col>
                </Row>
            </Container>
        )
    } else {
        return <UserLogin />;
    }

};

export default SupplierCreate;