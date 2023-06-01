import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import { Card, Button, Container } from 'react-bootstrap';

function Orders() {
  const orders_url = process.env.REACT_APP_API_URL + '/api/orders/';
  const [orders, setOrders] = useState([]);
  const tokenApp = sessionStorage.getItem('token');

  useEffect(() => {
    if (tokenApp) {
      axios.get(orders_url, {
        headers: {
          'Authorization': `Token ${tokenApp}`
        }
      }).then(res => {
        setOrders(res.data);
      })
    }
  }, [])

  return (
    <Card>
      <Card.Header className="py-3">List of Orders</Card.Header>
      <Card.Text>
        <Container>
          <table class="table table-striped table-hover" border="1">
            <thead>
              <tr>
                <th scope="col">Order Number</th>
                <th scope="col">Date</th>
                <th scope="col">Price</th>
                <th scope="col"></th>
              </tr>
            </thead>
            <tbody>
              {orders.map(order =>
                <tr>
                  <th scope="row">{order.id}</th>
                  <th scope="row">{order.date}</th>
                  <th scope="row">{order.total_price}</th>
                  <th scope="row"><Link to={`details/${order.id}`}><Button variant="success">Details</Button></Link></th>
                </tr>
              )}
            </tbody>
          </table>
        </Container>
      </Card.Text>
    </Card>
  );
};

export default Orders;