"use client";
import { useState, useEffect } from "react";
import Head from "next/head";

export default function Home() {
  const [status, setStatus] = useState("Idle");
  const [taskId, setTaskId] = useState<string | null>(null);
  const [results, setResults] = useState<any>(null);

  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files || e.target.files.length === 0) return;
    setStatus("Uploading...");
    
    // In production we would FormData and POST to /api/upload
    // For now we trigger the interpolate directly to showcase the integration
    try {
        const response = await fetch("http://localhost:8000/api/interpolate", {
            method: "POST"
        });
        const data = await response.json();
        setTaskId(data.task_id);
        setStatus("Processing Interpolation...");
    } catch (err) {
        setStatus("Error communicating with Backend");
    }
  };

  useEffect(() => {
      if (!taskId) return;
      const interval = setInterval(async () => {
          try {
              const res = await fetch(`http://localhost:8000/api/status/${taskId}`);
              const data = await res.json();
              if (data.status === "completed") {
                  setResults(data.results);
                  setStatus("Completed!");
                  clearInterval(interval);
              }
          } catch (e) {
              console.error(e);
          }
      }, 2000);
      return () => clearInterval(interval);
  }, [taskId]);

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8 font-sans">
      <Head>
        <title>Fill in the Frames</title>
      </Head>
      <header className="mb-8 border-b border-gray-700 pb-4">
        <h1 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400 tracking-tight">
          Fill in the Frames Seamlessly
        </h1>
        <p className="text-gray-400 mt-2 text-lg">AI-Powered Temporal Resolution Enhancement of Satellite Imagery (RIFE/Optical Flow)</p>
      </header>

      <main className="grid grid-cols-1 lg:grid-cols-3 gap-8">
        <section className="bg-gray-800 p-6 rounded-xl shadow-2xl border border-gray-700 lg:col-span-1 flex flex-col justify-between hover:border-blue-500 transition-colors">
          <div>
              <h2 className="text-2xl font-semibold mb-6 flex items-center">
                  <span className="bg-blue-500 w-2 h-6 mr-3 rounded-full"></span>
                  Control Panel
              </h2>
              <div className="flex flex-col gap-6">
                <label className="block">
                  <span className="text-gray-300 font-medium mb-2 block">Upload Dataset (.nc, .h5)</span>
                  <input type="file" className="block w-full text-sm text-gray-400 file:mr-4 file:py-3 file:px-6 file:rounded-lg file:border-0 file:text-sm file:font-semibold file:bg-blue-600 file:text-white hover:file:bg-blue-700 cursor-pointer transition-all" onChange={handleUpload}/>
                </label>
                
                <div className="p-4 bg-gray-900 rounded-lg mt-4 border border-gray-700 shadow-inner">
                  <p className="text-gray-400 text-sm uppercase tracking-wider mb-1">System Status</p>
                  <p className={`font-bold text-lg ${status === 'Error communicating with Backend' ? 'text-red-500' : 'text-emerald-400'}`}>
                      {status}
                  </p>
                  {taskId && <p className="text-xs text-gray-500 mt-2 font-mono break-all">Task ID: {taskId}</p>}
                </div>
              </div>
          </div>
          <div className="mt-8 pt-4 border-t border-gray-700 text-xs text-gray-500">
              <p>Model Architecture: RIFE</p>
              <p>Precision: Mixed (FP16/FP32)</p>
          </div>
        </section>

        <section className="bg-gray-800 p-6 rounded-xl shadow-2xl border border-gray-700 lg:col-span-2">
          <h2 className="text-2xl font-semibold mb-6 flex items-center">
              <span className="bg-emerald-500 w-2 h-6 mr-3 rounded-full"></span>
              Visualization & Analysis
          </h2>
          
          <div className="w-full min-h-[400px] bg-gray-900 rounded-xl flex items-center justify-center border border-gray-700 overflow-hidden relative shadow-inner">
             {status === "Completed!" && results ? (
                <div className="w-full h-full flex flex-col items-center justify-center p-6">
                   <div className="w-full flex justify-between px-8 mb-4">
                       <div className="text-center">
                           <p className="text-gray-400 uppercase text-xs tracking-wider">SSIM</p>
                           <p className="text-3xl font-bold text-emerald-400">{results.ssim}</p>
                       </div>
                       <div className="text-center">
                           <p className="text-gray-400 uppercase text-xs tracking-wider">PSNR</p>
                           <p className="text-3xl font-bold text-blue-400">{results.psnr} dB</p>
                       </div>
                   </div>
                   
                   {/* Load the actual plot generated by matplotlib on the backend */}
                   <img 
                       src={results.plot_url} 
                       alt="Evaluation Plot" 
                       className="max-w-full rounded-lg shadow-lg object-contain border border-gray-700 hover:scale-[1.02] transition-transform duration-300"
                   />
                   
                   <div className="mt-6 flex gap-4">
                       <button className="px-6 py-2 bg-gray-700 hover:bg-gray-600 rounded-lg font-medium transition-colors border border-gray-600">
                           Download NetCDF
                       </button>
                       <button className="px-6 py-2 bg-blue-600 hover:bg-blue-500 rounded-lg font-medium transition-colors">
                           View Optical Flow
                       </button>
                   </div>
                </div>
             ) : (
                <div className="text-center flex flex-col items-center">
                   {status.includes("Processing") ? (
                       <div className="w-12 h-12 border-4 border-blue-500 border-t-transparent rounded-full animate-spin mb-4"></div>
                   ) : (
                       <svg className="w-16 h-16 text-gray-700 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path strokeLinecap="round" strokeLinejoin="round" strokeWidth="2" d="M4 16l4.586-4.586a2 2 0 012.828 0L16 16m-2-2l1.586-1.586a2 2 0 012.828 0L20 14m-6-6h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z"></path></svg>
                   )}
                   <p className="text-gray-500 font-medium tracking-wide">
                       {status.includes("Processing") ? "Running PyTorch Inference..." : "Awaiting Data..."}
                   </p>
                </div>
             )}
          </div>
        </section>
      </main>
    </div>
  );
}
