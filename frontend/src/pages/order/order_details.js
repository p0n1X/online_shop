import React, { useEffect, useState } from "react";
import { useParams } from 'react-router-dom';
import axios from "axios";
import { Button } from "react-bootstrap";

function OrderDetails() {
  const { id } = useParams();
  const url = process.env.REACT_APP_API_URL + '/api/orders/' + id;
  const [orders, setOrders] = useState([]);
  const tokenApp = sessionStorage.getItem('token');
  const handleOnClick = (event) => {
    event.preventDefault();
    axios.post(process.env.REACT_APP_API_URL + `/api/carts/`, {
      product: event.target.value
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
      setOrders(res.data);
    })
  }, []);

  return <div className="App">
    <h1>Order Detail</h1>
    <table class="table table-striped table-hover" border="1">
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
          <th scope="col" ></th>
        </tr>
      </thead>
      <tbody>
        {orders.map(product =>
          <tr>
            <th scope="row">{product.order_number}</th>
            <th scope="row">{product.name}</th>
            <th scope="row">{product.description}</th>
            <th scope="row">{product.date}</th>
            <th scope="row">{product.sku_number}</th>
            <th scope="row">{product.quantity}</th>
            <th scope="row">{product.category}</th>
            <th scope="row">{product.price}</th>
            <th scope="row"><Button variant="success" value={product.id} onClick={handleOnClick}>Add to Cart</Button></th>
          </tr>
        )}

      </tbody>
    </table>
  </div>
};

export default OrderDetails;