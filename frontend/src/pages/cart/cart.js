import React, { useEffect, useState } from "react";
import { Link } from 'react-router-dom';
import axios from "axios";

const Cart = () => {
    const url = process.env.REACT_APP_API_URL + '/api/carts/';
    const [cartCount, setCartCount] = useState(0);
    const tokenApp = sessionStorage.getItem('token');

    useEffect(() => {
        if(tokenApp){
            axios.get(url, {
                headers: {
                    'Authorization': `Token ${tokenApp}`
                }
            }).then(res => {
                setCartCount(res.data.length);
            })
        } else {
            axios.get(url).then(res => {
                setCartCount(0);
            })
        }
        
    }, [])

    return <div className="App">
        Cart (<Link to={`/cart/details`}>{cartCount}</Link>)
    </div>
};

export default Cart;