import React from 'react';
import { Link } from 'react-router-dom';
import { Col, ListGroup, Card } from 'react-bootstrap';

function Sidebar() {
  return (
    <Col xs={2}>
      <Card border="secondary">
        <Card.Header className="py-3">Menu</Card.Header>
        <Card.Text>
          <ListGroup>
            <ListGroup.Item action as={Link} to={'/admin'}>
              Products
            </ListGroup.Item>
            <ListGroup.Item action as={Link} to={'/admin/orders'}>
              Orders
            </ListGroup.Item>
            <ListGroup.Item action as={Link} to={'/admin/categories'}>
              Categories
            </ListGroup.Item>
            <ListGroup.Item action as={Link} to={'/admin/suppliers'}>
              Suppliers
            </ListGroup.Item>
          </ListGroup>
        </Card.Text>
      </Card>
    </Col>
  );
}

export default Sidebar;