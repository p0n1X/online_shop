import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import { Col, Card, Button, Row, Container } from 'react-bootstrap';
import Sidebar from "../sidebar";


function AdminSupplier() {
  const url = process.env.REACT_APP_API_URL + '/api/suppliers/';
  const [suppliers, setSuppliers] = useState([]);
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
      window.location.replace("/admin/suppliers")
    })

  };

  useEffect(() => {
    axios.get(url).then(res => {
      setSuppliers(res.data);
    })
  }, [])
  // You do not have permission to view this directory or page.
  return (
    <Container>
      <Row>
        <Sidebar />
        <Col>
          <Card>
            <Card.Header className="py-3">List of Supplier <Link style={{ float: 'right' }} to={`/admin/supplier/create/`}><Button variant="success">Add new Supplier</Button></Link></Card.Header>
            <Card.Body>
              <Container>
                <table class="table table-striped table-hover table-bordered">
                  <thead>
                    <tr>
                      <th scope="col">Name</th>
                      <th scope="col">Price</th>
                      <th scope="col" colSpan="2"></th>
                    </tr>
                  </thead>
                  <tbody>
                    {suppliers.map(supplier =>
                      <tr>
                        <th scope="row">{supplier.name}</th>
                        <th scope="row">{supplier.price}</th>
                        <th scope="row"><Link to={`/admin/supplier/edit/${supplier.id}`}><Button variant="warning">Edit</Button></Link></th>
                        <th scope="row"><Button variant="danger" value={supplier.id} onClick={handleDeleteClick}>Delete</Button></th>
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
};

export default AdminSupplier;