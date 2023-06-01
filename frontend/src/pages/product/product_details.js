import React, { useEffect, useState } from "react";
import { useParams } from 'react-router-dom';
import axios from "axios";
import { Button, Card, Row, Col, Container, Image, Form } from "react-bootstrap";
import not_found from '../../images/not_found.png'

function ProductDetails() {
  const { id } = useParams();
  const url = process.env.REACT_APP_API_URL + '/api/products/' + id;
  const [product, setProduct] = useState([]);
  const [quantity, setQuantity] = useState(1);
  const tokenApp = sessionStorage.getItem('token');
  const rows = [];
  for (let i = 1; i < 10; i++) {
    rows.push(<option value={i}>{i}</option>)
  }

  const handleOnClick = (event) => {
    event.preventDefault();
    axios.post(process.env.REACT_APP_API_URL + `/api/carts/`, {
      product: product.id,
      quantity: quantity
    }, {
      headers: {
        'Authorization': `Token ${tokenApp}`
      }
    })
      .then(res => {
        alert("Product successfully added to cart");
        window.location.reload();
      })
      .catch(error => {
        alert("Please Login!");
      })
  };

  useEffect(() => {
    axios.get(url).then(res => {
      setProduct(res.data);
    })
  }, []);

  return (
    <Container>
      <Row>
        <Col>
          <Card>
            <Card.Img src={not_found} rounded />
          </Card>
          <Image />
        </Col>
        <Col xs={4}>
          <Container>
            <Card>
              <Card.Body>
                <Card.Title>{product.name}</Card.Title>
                <Row className="mb-4">
                  Price: {product.price}
                </Row>
                <Row className="mb-4">
                  Sku Number: {product.sku_number}
                </Row>
                <Row >
                  <Form.Select className="mb-4"
                    type="text"
                    value={quantity}
                    onChange={(e) => setQuantity(e.target.value)}
                  >
                    {rows}
                  </Form.Select>
                  <Button variant="success" onClick={handleOnClick}>Add to Cart</Button>
                </Row>
              </Card.Body>
            </Card>
          </Container>
        </Col>
      </Row>
      <Row>
        <Container >
          <Card>
            <Card.Header>Description</Card.Header>
            <Card.Body>
              {product.description}
            </Card.Body>
          </Card>
        </Container>
      </Row>
    </Container>
  )
};

export default ProductDetails;