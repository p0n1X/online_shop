import './App.css';
import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Products from "./pages/product/products";
import ProductDetails from "./pages/product/product_details";
import ProductCreate from "./pages/admin/product/product_create";
import Cart from "./pages/cart/cart";
import CartDetails from "./pages/cart/cart_details";
import UserLogin from "./pages/user/user_login";
import UserLogout from "./pages/user/user_logout";
import Orders from "./pages/order/orders";
import OrderDetails from "./pages/order/order_details";
import 'bootstrap/dist/css/bootstrap.min.css';
import Header from './pages/header';
import { Container, Row } from 'react-bootstrap';
import AdminProducts from './pages/admin/product/products';
import ProductEdit from './pages/admin/product/product_edit';
import AdminOrders from './pages/admin/order/orders';
import AdminOrderDetails from './pages/admin/order/order_details';
import AdminCategory from './pages/admin/category/category';
import AdminCategoryEdit from './pages/admin/category/category_edit';
import CategoryCreate from './pages/admin/category/category_create';
import AdminSupplier from './pages/admin/supplier/supplier';
import AdminSupplierEdit from './pages/admin/supplier/supplier_edit';
import SupplierCreate from './pages/admin/supplier/supplier_create';
import Category from './pages/category/category';
import CategoryProducts from './pages/category/products';
import Profile from './pages/user/profile';
import Register from './pages/user/register';
import ProfileEdit from './pages/user/edit_profile';

function App() {
  return (
    <Router>
      <Header />
      <Container>
        <Row>
          <Routes>
            <Route path="/" element={<Products />} />
            <Route path="/products/:id" element={<CategoryProducts />}></Route>
            <Route path="/details/:id" element={<ProductDetails />}></Route>
            <Route path="/admin/edit/:id" element={<ProductEdit />}></Route>
            <Route path="/admin/category/:name" element={<Category />}></Route>
            <Route path="/cart/" element={<Cart />}></Route>
            <Route path="/cart/details" element={<CartDetails />}></Route>
            <Route path="/login/" element={<UserLogin />}></Route>
            <Route path="/logout/" element={<UserLogout />}></Route>
            <Route path="/orders/" element={<Orders />}></Route>
            <Route path="/orders/details/:id" element={<OrderDetails />}></Route>
            <Route path="/admin" element={<AdminProducts />}></Route>
            <Route path="/admin/create" element={<ProductCreate />}></Route>
            <Route path="/admin/orders" element={<AdminOrders />}></Route>
            <Route path="/admin/orders/details/:id" element={<AdminOrderDetails />}></Route>
            <Route path="/admin/categories" element={<AdminCategory />}></Route>
            <Route path="/admin/category/edit/:id" element={<AdminCategoryEdit />}></Route>
            <Route path="/admin/category/create" element={<CategoryCreate />}></Route>
            <Route path="/admin/suppliers" element={<AdminSupplier />}></Route>
            <Route path="/admin/supplier/edit/:id" element={<AdminSupplierEdit />}></Route>
            <Route path="/admin/supplier/create" element={<SupplierCreate />}></Route>
            <Route path="/profile" element={<Profile />}></Route>
            <Route path="/profile/edit" element={<ProfileEdit />}></Route>
            <Route path="/register" element={<Register />}></Route>
          </Routes>
        </Row>
      </Container>
    </Router>
  );
}


export default App;