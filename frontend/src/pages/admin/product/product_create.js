import React, { useEffect, useState } from "react";
import { Button, Container, Card, Form, Row, Col, FloatingLabel, Alert } from "react-bootstrap";
import axios from "axios";
import { Link } from 'react-router-dom';
import Sidebar from "../sidebar";


function ProductCreate() {
    const [name, setName] = useState("");
    const [number, setNumber] = useState("");
    const [description, setDescription] = useState("");
    const [quantity, setQuantity] = useState("");
    const [category, setCategory] = useState("");
    const [categories, setCategories] = useState([]);
    const [price, setPrice] = useState("");
    const [islogin, setIslogin] = useState(false);
    const url = process.env.REACT_APP_API_URL + '/api/users/login';
    const category_url = process.env.REACT_APP_API_URL + '/api/categories/';
    const product_url = process.env.REACT_APP_API_URL + '/api/products/';
    const tokenApp = sessionStorage.getItem('token');

    if (category === "" && categories.length > 0) {
        setCategory(categories[0]['id'])
    }

    const handleSubmit = event => {
        event.preventDefault();

        axios.post(product_url, {
            name: name,
            description: description,
            quantity: quantity,
            category: category,
            price: parseFloat(price).toFixed(2),
            sku_number: number
        })
            .then(res => {
                if (res.data['message']) {
                    alert(res.data['message'])
                    window.location.replace("/admin")
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

            axios.get(category_url).then(res => {
                setCategories(res.data);
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
                            <Card.Header className="py-3">Create new product</Card.Header>
                            <Card.Body>
                                <Container>
                                    <Form onSubmit={handleSubmit}>
                                        <Form.Group size="lg" className="mb-3" controlId="name">
                                            <FloatingLabel label="Product Name">
                                                <Form.Control
                                                    autoFocus
                                                    type="name"
                                                    value={name}
                                                    onChange={(e) => setName(e.target.value)}
                                                />
                                            </FloatingLabel>
                                        </Form.Group>
                                        <Form.Group size="lg" className="mb-3" controlId="number">
                                            <FloatingLabel label="Sku Number">
                                                <Form.Control
                                                    type="number"
                                                    value={number}
                                                    onChange={(e) => setNumber(e.target.value)}
                                                />
                                            </FloatingLabel>
                                        </Form.Group>
                                        <Form.Group size="lg" className="mb-3" controlId="description">
                                            <FloatingLabel label="Description">
                                                <Form.Control
                                                    as="textarea"
                                                    style={{ height: '200px' }}
                                                    value={description}
                                                    onChange={(e) => setDescription(e.target.value)}
                                                />
                                            </FloatingLabel>
                                        </Form.Group>
                                        <Form.Group size="lg" className="mb-3" controlId="quantity">
                                            <FloatingLabel label="Quantity">
                                                <Form.Control
                                                    type="number"
                                                    value={quantity}
                                                    onChange={(e) => setQuantity(e.target.value)}
                                                />
                                            </FloatingLabel>
                                        </Form.Group>
                                        <Form.Group size="lg" className="mb-3" controlId="category">
                                            <FloatingLabel label="Category">
                                                <Form.Select
                                                    type="text"
                                                    value={category}
                                                    onChange={(e) => setCategory(e.target.value)}
                                                >
                                                    {categories.map((cat) => (
                                                        <option value={cat.id}>{cat.name}</option>
                                                    ))}
                                                </Form.Select>
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
                                        <Link style={{ float: 'right' }} to={`/admin`}><Button variant="secondary">Back</Button></Link>
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
    }

};

export default ProductCreate;