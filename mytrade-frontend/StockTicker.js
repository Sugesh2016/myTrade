import React, { useEffect, useState } from "react";
import axios from "axios";

const StockTicker = ({ symbol }) => {
  const [price, setPrice] = useState(null);

  useEffect(() => {
    const fetchStockPrice = async () => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/stock/${symbol}`);
        setPrice(response.data.price);
      } catch (error) {
        console.error("Error fetching stock price:", error);
      }
    };

    fetchStockPrice();
    const interval = setInterval(fetchStockPrice, 5000); // Refresh every 5 sec

    return () => clearInterval(interval);
  }, [symbol]);

  return <h1>{symbol}: ${price || "Loading..."}</h1>;
};

export default StockTicker;
