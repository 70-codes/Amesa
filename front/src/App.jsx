import { Outlet } from "react-router-dom";
import Sidebar from "./components/common/sidebar";

function App() {
  return (
    <div className="flex h-screen bg-slate-900 text-gray-100 overflow-hidden">
      {/* BG */}
      <div className="fixed inset-0 z-0">
        <div className="absolute inset-0 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 opacity-80" />
        <div className="absolute inset-0 backdrop-blur-sm " />
      </div>
      <Sidebar />
      <Outlet />
    </div>
  );
}

export default App;
