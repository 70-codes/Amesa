import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App.jsx";
import "./index.css";

import { createBrowserRouter, RouterProvider } from "react-router-dom";
import Login from "./pages/auth/login/index.jsx";
import Register from "./pages/auth/register/index.jsx";
import Products from "./pages/products/index.jsx";

const router = createBrowserRouter([
  {
    element: <App />,
    children: [
      {
        path: "/products",
        element: <Products />,
      },
    ],
  },
  {
    path: "/",
    element: <Login />,
  },
  {
    path: "/login",
    element: <Login />,
  },
  {
    path: "/register",
    element: <Register />,
  },
]);

ReactDOM.createRoot(document.getElementById("root")).render(
  <React.StrictMode>
    <RouterProvider router={router} />
  </React.StrictMode>
);
