import Authwrapper from "../Authwrapper";
import { UserPlus2Icon } from "lucide-react";
import { Link } from "react-router-dom";

const Register = () => {
  return (
    <Authwrapper icon={UserPlus2Icon} headtext={"Register"}>
      <form className="space-y-4 md:space-y-6 w-[80%]" action="">
        <div>
          <label className="block text-sm font-medium text-slate-900 dark:text-white">
            Username
          </label>
          <input
            type="username"
            name="username"
            id="username"
            className="w-full p-2.5  bg-slate-700 rounded-lg focus:outline-none focus:bg-slate-600 focus:ring-1 focus:ring-purple-500"
            placeholder="Johndoe"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-900 dark:text-white">
            Email
          </label>
          <input
            type="email"
            name="email"
            id="email"
            className="w-full p-2.5  bg-slate-700 rounded-lg focus:outline-none focus:bg-slate-600 focus:ring-1 focus:ring-purple-500"
            placeholder="Johndoe@gmail.com"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-900 dark:text-white">
            First Name
          </label>
          <input
            type="fname"
            name="fname"
            id="fname"
            className="w-full p-2.5  bg-slate-700 rounded-lg focus:outline-none focus:bg-slate-600 focus:ring-1 focus:ring-purple-500"
            placeholder="John"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-900 dark:text-white">
            Last Name
          </label>
          <input
            type="lname"
            name="lname"
            id="lname"
            className="w-full p-2.5  bg-slate-700 rounded-lg focus:outline-none focus:bg-slate-600 focus:ring-1 focus:ring-purple-500"
            placeholder="JDoe"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-900 dark:text-white">
            Password
          </label>
          <input
            type="password"
            name="password"
            id="password"
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
          Login
        </button>
        <p className="text-sm font-light text-slate-100 dark:text-slate-400 text-center">
          Have an account?{" "}
          <Link to={"/login"}>
            <a className="font-medium text-purple-600 hover:underline dark:text-purple-500">
              Login
            </a>
          </Link>
        </p>
      </form>
    </Authwrapper>
  );
};

export default Register;
