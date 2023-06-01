import React, { useEffect, useState } from "react";
import axios from "axios";
import { Col, Card, Button, Row, Container, Form, FloatingLabel, Alert, Image } from 'react-bootstrap';
import not_found from '../../images/not_found.png'

function CartDetails() {
  const url = process.env.REACT_APP_API_URL + '/api/carts/';
  const [products, setProducts] = useState([]);
  const [total_product_price, setTotalProductPrice] = useState(0);
  const [total_price, setTotalPrice] = useState(0);
  const [shipment, setShipment] = useState(0);
  const tokenApp = sessionStorage.getItem('token');
  const order_url = process.env.REACT_APP_API_URL + '/api/orders/';
  const supplier_url = process.env.REACT_APP_API_URL + '/api/suppliers/';
  const [firstname, setFirstname] = useState("");
  const [lastname, setLastname] = useState("");
  const [address, setAddress] = useState("");
  const [email, setEmail] = useState("");
  const [suppliers, setSuppliers] = useState([]);
  const [supplier, setSupplier] = useState("");
  const [isNotSelectShipment, setIsNotSelectShipment] = useState(true);

  const handleClick = event => {
    event.preventDefault();
    axios.post(order_url, {
      token: tokenApp,
      supplier: supplier
    })
      .then(res => {
        if (res.data['message']) {
          alert(res.data['message'])
          window.location.replace("/")
        }
      })
  };

  const handleDeleteClick = event => {
    event.preventDefault();
    axios.delete(url, {
      headers: {
        'Authorization': `Token ${tokenApp}`
      },
      data: {
        id: event.target.value
      }
    }).then(res => {
      window.location.replace("/cart/details")
    })

  };

  const onChangeShipment = event => {
    var shipment_price = Number(event.target.options[event.target.selectedIndex].dataset.price)
    setSupplier(event.target.value);
    setShipment(shipment_price);
    setTotalPrice(total_product_price + shipment_price)
    setIsNotSelectShipment(false)
  };

  useEffect(() => {
    if (tokenApp){
      axios.get(url, {
        headers: {
          'Authorization': `Token ${tokenApp}`
        }
      }).then(res => {
        var products_price = 0
        for (let i = 0; i < res.data.length; i++) {
          setFirstname(res.data[i]['firstname'])
          setLastname(res.data[i]['lastname'])
          setAddress(res.data[i]['address'])
          setEmail(res.data[i]['email'])
          products_price = products_price + res.data[i]['total_price']
        }
        setTotalProductPrice(products_price)
        setTotalPrice(products_price + shipment)
        setProducts(res.data);
      })
  
      axios.get(supplier_url).then(res => {
        setSuppliers(res.data);
      })
    }
  }, [])

  if (products.length === 0) {
    return (
      <Alert key="warning" variant="warning">
        Your cart is currently empty!!!
      </Alert>
    )
  } else {
    return (
      <Container>
        <Row>
          <Col>
            <Row className="mb-3">
              <Col>
                <Card>
                  <Card.Header className="py-3">Products</Card.Header>
                  <Card.Body>
                    <Container>
                      <table class="table table-striped table-hover table-bordered">
                        <thead>
                          <tr>
                            <th></th>
                            <th>Name</th>
                            <th>Price</th>
                            <th>Quantity</th>
                            <th>Total Price</th>
                            <th></th>
                          </tr>
                        </thead>
                        <tbody>
                          {products.map(c =>
                            <tr>
                              <td><Image src={not_found} height={100} width={150} /></td>
                              <td>{c.product}</td>
                              <td>{c.price}</td>
                              <td>{c.quantity}</td>
                              <td>{c.total_price}</td>
                              <td><Button variant="danger" value={c.id} onClick={handleDeleteClick}>Delete</Button></td>
                            </tr>
                          )}
                        </tbody>
                      </table>
                    </Container>
                  </Card.Body>
                </Card>
              </Col>
            </Row>
            <Row>
              <Col>
                <Card>
                  <Card.Header className="py-3">Biling details</Card.Header>
                  <Card.Body>
                    <Container>
                      <h5 className="mb-4">Address</h5>
                      <Form.Group size="lg" className="mb-3" controlId="firstname">
                        <FloatingLabel label="First Name">
                          <Form.Control
                            readOnly
                            autoFocus
                            type="name"
                            value={firstname}
                            onChange={(e) => setFirstname(e.target.value)}
                          />
                        </FloatingLabel>
                      </Form.Group>
                      <Form.Group size="lg" className="mb-3" controlId="lastname">
                        <FloatingLabel label="Last Name">
                          <Form.Control
                            autoFocus
                            type="lastname"
                            value={lastname}
                            onChange={(e) => setLastname(e.target.value)}
                            readOnly
                          />
                        </FloatingLabel>
                      </Form.Group>
                      <Form.Group size="lg" className="mb-3" controlId="address">
                        <FloatingLabel label="Address">
                          <Form.Control
                            autoFocus
                            type="name"
                            value={address}
                            onChange={(e) => setAddress(e.target.value)}
                            readOnly
                          />
                        </FloatingLabel>
                      </Form.Group>
                      <Form.Group size="lg" className="mb-3" controlId="email">
                        <FloatingLabel label="Email">
                          <Form.Control
                            autoFocus
                            type="name"
                            value={email}
                            onChange={(e) => setEmail(e.target.value)}
                            readOnly
                          />
                        </FloatingLabel>
                      </Form.Group>
                      <hr className="my-2"></hr>
                      <h5 className="mb-4">Payment</h5>
                      <Form.Check type="radio" label="Pay on delivery" checked />
                      <hr className="my-2"></hr>
                      <h5 className="mb-4">Supplier</h5>
                      <FloatingLabel label="Supplier">
                        <Form.Select
                          type="text"
                          value={supplier}
                          data-price={shipment}
                          onChange={onChangeShipment}
                        >
                          <option selected disabled></option>
                          {suppliers.map((sup) => (
                            <option value={sup.id} data-price={sup.price}>{sup.name}&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;TAX: {sup.price}</option>
                          ))}
                        </Form.Select>
                      </FloatingLabel>
                    </Container>
                    <Container className="mb-4">
                    </Container>
                  </Card.Body>
                </Card>
              </Col>
            </Row>
          </Col>
          <Col xs={2}>
            <Card>
              <Card.Header className="py-3">Summary</Card.Header>
              <Card.Body >
                <Container className="mb-4">
                  <Row>
                    <Col>
                      Products
                    </Col>
                    <Col>
                      {total_product_price}
                    </Col>
                  </Row>
                  <Row>
                    <Col>
                      Shipment
                    </Col>
                    <Col>
                      {shipment}
                    </Col>
                  </Row>
                  <hr className="my-2"></hr>
                  <Row >
                    <Col>
                      <strong>Total amount</strong>
                    </Col>
                    <Col>
                      {total_price}
                    </Col>
                  </Row>
                  <Alert variant='warning'show={isNotSelectShipment ? true : false}>Please select shipping method!</Alert>
                  <Button disabled={isNotSelectShipment ? true : false} style={{ float: 'right' }} variant="success" onClick={handleClick}>Finish</Button>
                </Container>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    )
  }
};

export default CartDetails;