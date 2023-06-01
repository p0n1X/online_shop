import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";
import { NavDropdown } from 'react-bootstrap';

function Category() {
  const url = process.env.REACT_APP_API_URL + '/api/categories/';
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    axios.get(url).then(res => {
      setCategories(res.data);
    })
  }, [])

  return (
    <div>
      {categories.map(category =>
        <NavDropdown.Item as={Link} to={`/products/${category.id}`}>
          {category.name}
        </NavDropdown.Item>
      )}
    </div>
  );
};

export default Category;