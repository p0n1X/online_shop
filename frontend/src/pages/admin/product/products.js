import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import { Col, Card, Button, Row, Container, Alert } from 'react-bootstrap';
import Sidebar from "../sidebar";


function AdminProducts() {
  const url = process.env.REACT_APP_API_URL + '/api/products/';
  const [products, setProducts] = useState([]);
  const login_url = process.env.REACT_APP_API_URL + '/api/users/login';
  const [islogin, setIslogin] = useState(false);
  const tokenApp = sessionStorage.getItem('token');

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
      window.location.replace("/admin")
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
    axios.get(url).then(res => {
      setProducts(res.data);
    })
  }, [])

  if (islogin) {
    return (
      <Container>
        <Row>
          <Sidebar />
          <Col>
            <Card>
              <Card.Header className="py-3">List of Products <Link style={{ float: 'right' }} to={`/admin/create`}><Button variant="success">Add new product</Button></Link></Card.Header>
              <Card.Body>
                <Container>
                  <table class="table table-striped table-hover table-bordered">
                    <thead>
                      <tr>
                        <th scope="col">#</th>
                        <th scope="col">Name</th>
                        <th scope="col">Description</th>
                        <th scope="col">Date</th>
                        <th scope="col">SKU Number</th>
                        <th scope="col">Quantity</th>
                        <th scope="col">Category</th>
                        <th scope="col">Price</th>
                        <th scope="col" colSpan="2"></th>
                      </tr>
                    </thead>
                    <tbody>
                      {products.map(product =>
                        <tr>
                          <th scope="row">{product.id}</th>
                          <th scope="row">{product.name}</th>
                          <th scope="row">{product.description.substring(0, 200)}</th>
                          <th scope="row">{product.date}</th>
                          <th scope="row">{product.sku_number}</th>
                          <th scope="row">{product.quantity}</th>
                          <th scope="row">{product.category}</th>
                          <th scope="row">{product.price}</th>
                          <th scope="row"><Link to={`/admin/edit/${product.id}`}><Button variant="warning">Edit</Button></Link></th>
                          <th scope="row"><Button variant="danger" value={product.id} onClick={handleDeleteClick}>Delete</Button></th>
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
    )
  };
};

export default AdminProducts;