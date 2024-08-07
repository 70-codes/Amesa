import Authwrapper from "../Authwrapper";
import { UserCircleIcon } from "lucide-react";
import { Link } from "react-router-dom";
import { normalAxios, axiosWithHeader } from "../../../api/axios";
import { useState, useEffect } from "react";
import { Navigate } from "react-router-dom";

const Login = () => {
  const [userData, setUserData] = useState({ username: "", password: "" });
  // eslint-disable-next-line no-unused-vars
  const [error, setError] = useState(null);
  const [loginSuccess, setLoginSuccess] = useState(false);
  // eslint-disable-next-line no-unused-vars
  const [currentUser, setCurrentUser] = useState(null);

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent default form submission behavior

    try {
      const response = await normalAxios.post("/auth/login/", userData);
      const { access, refresh } = response.data;

      localStorage.setItem("access", access);
      localStorage.setItem("refresh", refresh);

      setLoginSuccess(true); // Set login success state to true
      setError(null); // Clear any previous errors
    } catch (error) {
      setError(
        error.response ? error.response.data.detail : "An error occurred"
      );
      console.error(
        "Error logging in:",
        error.response ? error.response.data : error.message
      );
    }
  };
  useEffect(() => {
    const getCurrentUser = async () => {
      try {
        const response = await axiosWithHeader.get(
          "/user/get-current-user/",
          localStorage.getItem("access")
        );
        localStorage.setItem("currentUser", JSON.stringify(response.data));
        setCurrentUser(response.data);
      } catch (error) {
        console.error(
          "Error fetching current user:",
          error.response ? error.response.data : error.message
        );
      }
    };

    if (loginSuccess) {
      getCurrentUser();
    }
  }, [loginSuccess]);

  const handleChange = (e) => {
    setUserData((oldData) => ({ ...oldData, [e.target.name]: e.target.value }));
  };

  if (loginSuccess) {
    return <Navigate to="/products" />;
  }

  return (
    <Authwrapper icon={UserCircleIcon} headtext={"Login"}>
      <form className="space-y-4 md:space-y-6 w-[80%]" onSubmit={handleSubmit}>
        <div>
          <label className="block mb-2 text-sm font-medium text-slate-900 dark:text-white">
            Username
          </label>
          <input
            type="username"
            name="username"
            id="username"
            onChange={handleChange}
            className="w-full p-2.5  bg-slate-700 rounded-lg focus:outline-none focus:bg-slate-600 focus:ring-1 focus:ring-purple-500"
            placeholder="Johndoe"
            required
          />
        </div>
        <div>
          <label className="block mb-2 text-sm font-medium text-slate-900 dark:text-white">
            Password
          </label>
          <input
            type="password"
            name="password"
            id="password"
            onChange={handleChange}
            placeholder="••••••••"
            className="w-full p-2.5  bg-slate-700 rounded-lg focus:outline-none focus:bg-slate-600 focus:ring-1 focus:ring-purple-500"
            required
          />
        </div>
        <button
          type="submit"
          className="w-full text-white bg-gradient-to-tr from-purple-600 to-fuchsia-600 hover:bg-gradient-to-tr
             hover:from-purple-500 hover:to-fuchsia-500 hover:translate-y-1 focus:ring-4 focus:outline-none
              font-medium rounded-lg text-sm px-5 py-2.5 text-center transition-all duration-200"
        >
          Sign in
        </button>
        <p className="text-sm font-light text-slate-500 dark:text-slate-400">
          Don’t have an account yet?{" "}
          <Link to={"/register"}>
            <a className="font-medium text-purple-600 hover:underline dark:text-purple-500">
              Sign up
            </a>
          </Link>
        </p>
      </form>
    </Authwrapper>
  );
};

export default Login;
