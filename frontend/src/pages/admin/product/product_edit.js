import React, { useEffect, useState } from "react";
import { Button, Card, Container, Form, Col, Row, FloatingLabel, Alert } from "react-bootstrap";
import axios from "axios";
import { Link, useParams } from 'react-router-dom';
import Sidebar from "../sidebar";

function ProductEdit() {
    const { id } = useParams();
    const [name, setName] = useState("");
    const [number, setNumber] = useState("");
    const [description, setDescription] = useState("");
    const [quantity, setQuantity] = useState("");
    const [category, setCategory] = useState("");
    const [categories, setCategories] = useState([]);
    const [price, setPrice] = useState("");
    const [islogin, setIslogin] = useState(false);
    const url = process.env.REACT_APP_API_URL + '/api/users/login';
    const product_url = process.env.REACT_APP_API_URL + '/api/products/' + id;
    const category_url = process.env.REACT_APP_API_URL + '/api/categories/';
    const tokenApp = sessionStorage.getItem('token');


    const handleSubmit = event => {
        event.preventDefault();

        axios.put(product_url, {
            name: name,
            description: description,
            quantity: quantity,
            category: category,
            price: parseFloat(price).toFixed(2),
            sku_number: number
        })
            .then(res => {
                window.location.replace("/admin")
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

            axios.get(product_url).then(res => {
                setName(res.data['name']);
                setNumber(res.data['sku_number']);
                setDescription(res.data['description']);
                setQuantity(res.data['quantity']);
                setCategory(res.data['category_id']);
                setPrice(res.data['price']);
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
                            <Card.Header className="py-3">Edit Product</Card.Header>
                            <Card.Body>
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

export default ProductEdit;