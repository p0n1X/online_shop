import React, { useEffect, useState } from "react";
import { Button, Card, Container, Form, Col, Row, FloatingLabel } from "react-bootstrap";
import axios from "axios";
import UserLogin from "../../user/user_login";
import { Link, useParams } from 'react-router-dom';
import Sidebar from "../sidebar";

function AdminSupplierEdit() {
    const { id } = useParams();
    const [name, setName] = useState("");
    const [price, setPrice] = useState("");
    const [islogin, setIslogin] = useState(false);
    const url = process.env.REACT_APP_API_URL + '/api/users/login';
    const supplier_url = process.env.REACT_APP_API_URL + '/api/suppliers/' + id;;
    const tokenApp = sessionStorage.getItem('token');

    const handleSubmit = event => {
        event.preventDefault();

        axios.put(supplier_url, {
            name: name,
            price: price,
            supplier_id: id,
        })
            .then(res => {
                window.location.replace("/admin/suppliers/")
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

                axios.get(supplier_url).then(res => {
                    setName(res.data['name']);
                    setPrice(res.data['price']);
                })
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
                            <Card.Header className="py-3"> Edit Supplier</Card.Header>
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
            </Container >
        )

    } else {
        return <UserLogin />;
    }

};

export default AdminSupplierEdit;