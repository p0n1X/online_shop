import React, { useEffect, useState } from "react";
import { Link, useParams } from 'react-router-dom';
import axios from "axios";
import { Button, Container, Row, Col, Card, Alert } from "react-bootstrap";
import Sidebar from "../sidebar";


function AdminOrderDetails() {
  const { id } = useParams();
  const url = process.env.REACT_APP_API_URL + '/api/orders/' + id;
  const [orders, setOrders] = useState([]);
  const login_url = process.env.REACT_APP_API_URL + '/api/users/login';
  const [islogin, setIslogin] = useState(false);
  const tokenApp = sessionStorage.getItem('token');

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

    axios.get(url).then(res => {
      setOrders(res.data);
    })
  }, []);

  if (islogin) {
    return (
      <Container>
        <Row>
          <Sidebar />
          <Col>
            <Card>
              <Card.Header className="py-3">Order Detail</Card.Header>
              <Card.Body>
                <Container>
                  <table className="table table-striped table-hover table-bordered rounded-circle">
                    <thead>
                      <tr>
                        <th scope="col">Order Number</th>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col">Date</th>
                        <th scope="col">SKU Number</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Category</th>
                        <th scope="col">Price</th>
                      </tr>
                    </thead>
                    <tbody>
                      {orders.map(product =>
                        <tr>
                          <th scope="row">{product.order_number}</th>
                          <th scope="row">{product.name}</th>
                          <th scope="row">{product.description.substring(0, 200)}</th>
                          <th scope="row">{product.date}</th>
                          <th scope="row">{product.sku_number}</th>
                          <th scope="row">{product.quantity}</th>
                          <th scope="row">{product.category}</th>
                          <th scope="row">{product.price}</th>
                        </tr>
                      )}

                    </tbody>
                  </table>
                  <Link style={{ float: 'right' }} to={`/admin/orders`}><Button variant="secondary">Back</Button></Link>
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

export default AdminOrderDetails;