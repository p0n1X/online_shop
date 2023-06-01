import React from "react";
import { Link } from 'react-router-dom';
import { Nav, Navbar, NavDropdown, Container } from 'react-bootstrap';
import UserLoginMenu from "./user/user_login_menu"
import Cart from "./cart/cart"
import Category from "./category/category";


function Header() {
  return (
    <Navbar bg="dark" variant="dark" expand="lg" className="mb-4">
      <Container>
        <Navbar.Brand as={Link} to={"/"}>Online Shop</Navbar.Brand>
        <Navbar.Toggle aria-controls="basic-navbar-nav" />
        <Navbar.Collapse id="basic-navbar-nav">
          <Nav className="me-auto">
            <Nav.Link as={Link} to={"/"}>Home</Nav.Link>
            <NavDropdown title="Categories" id="basic-nav-dropdown">
              <Category />
            </NavDropdown>
          </Nav>
          <Nav>
            <Nav.Link as={Link} to={"/cart/details"}><Cart /></Nav.Link>
            <NavDropdown title="User" id="basic-nav-dropdown">
              <UserLoginMenu />
            </NavDropdown>
          </Nav>
        </Navbar.Collapse>
      </Container>
    </Navbar>
  );
};

export default Header;