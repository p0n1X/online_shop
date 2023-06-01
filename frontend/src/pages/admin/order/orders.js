import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import { Col, Card, Button, Row, Container, Alert } from 'react-bootstrap';
import Sidebar from "../sidebar";

function AdminOrders() {
  const orders_url = process.env.REACT_APP_API_URL + '/api/orders/';
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

    axios.get(orders_url, {
      headers: {
        'Authorization': `Token ${tokenApp}`
      }
    }).then(res => {
      setOrders(res.data);
    })
  }, [])

  if (islogin) {
    return (
      <Container>
        <Row>
          <Sidebar />
          <Col>
            <Card>
              <Card.Header className="py-3">List of Orders</Card.Header>
              <Card.Body>
                <Container>
                  <table class="table table-striped table-hover table-bordered" >
                    <thead>
                      <tr>
                        <th scope="col">Order Number</th>
                        <th scope="col">Date</th>
                        <th scope="col">Price</th>
                        <th scope="col">Supplier</th>
                        <th scope="col"></th>
                      </tr>
                    </thead>
                    <tbody>
                      {orders.map(order =>
                        <tr>
                          <th scope="row">{order.id}</th>
                          <th scope="row">{order.date}</th>
                          <th scope="row">{order.total_price}</th>
                          <th scope="row">{order.supplier}</th>
                          <th scope="row"><Link to={`/admin/orders/details/${order.id}`}><Button variant="success">Details</Button></Link></th>
                        </tr>
                      )}
                    </tbody>
                  </table>
                </Container>
              </Card.Body>
            </Card>
          </Col>
        </Row>
      </Container>
    );
  } else {
    return (
      <Alert key="danger" variant="danger">
        You do not have permission to view this page!
      </Alert>
    );
  };
};

export default AdminOrders;