import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import { Col, Card, Button, Row, Container } from 'react-bootstrap';
import not_found from '../../images/not_found.png'

function Products() {
  const url = process.env.REACT_APP_API_URL + '/api/products/';
  const [products, setProducts] = useState([]);

  useEffect(() => {
    axios.get(url).then(res => {
      setProducts(res.data);
    })
  }, [])

  return (
    <Container>
      <Card>
        <Card.Header className="py-3 mb-4" >Products</Card.Header>
        <Card.Text>
          <Container>
            <Row className="mb-4">
              {products.map(c =>
                <Col xs="4">
                  <Card className="mb-4">
                    <Card.Img variant="top" src={not_found} />
                    <Card.Body>
                      <Card.Title>{c.name}</Card.Title>
                      <Card.Text>
                        {c.description.substring(0, 200)}
                      </Card.Text>
                      <Link variant="primary" to={`details/${c.id}`}><Button>View Details</Button></Link>
                    </Card.Body>
                  </Card>
                </Col>
              )}
            </Row>
          </Container>
        </Card.Text>
      </Card>
    </Container>
  );
};

export default Products;