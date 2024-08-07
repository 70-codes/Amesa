const Authwrapper = ({ icon: Icon, headtext, children }) => {
  return (
    <div className="flex h-screen bg-slate-900 text-gray-100 overflow-hidden">
      {/* BG */}
      <div className="fixed inset-0 z-0">
        <div className="absolute inset-0 bg-gradient-to-br from-slate-900 via-slate-800 to-slate-900 opacity-80" />
        <div className="absolute inset-0 backdrop-blur-sm " />
      </div>
      <div
        className="flex items-center justify-center z-10 flex-col mx-auto my-auto w-96
       bg-slate-800 border-2 border-slate-700 h-auto p-2 rounded-lg bg-opacity-50 backdrop-blur-lg
       shadow-xl shadow-slate-700 hover:shadow-slate-600 transition-all duration-200
       "
      >
        <Icon className="size-12 text-purple-500 mr-4 bg-fuchsia-200 bg-opacity-25 p-2 rounded-full" />
        <div className="p-4 space-y-4 md:space-y-6 sm:p-8">
          <h1 className="text-xl font-bold leading-tight tracking-tight text-slate-300 md:text-2xl text-center ">
            {headtext}
          </h1>
        </div>

        {children}
      </div>
    </div>
  );
};

export default Authwrapper;
