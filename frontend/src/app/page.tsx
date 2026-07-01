"use client";
import { useState } from "react";
import Head from "next/head";

export default function Home() {
  const [status, setStatus] = useState("Idle");
  
  const handleUpload = async (e: React.ChangeEvent<HTMLInputElement>) => {
    if (!e.target.files) return;
    setStatus("Uploading...");
    // Mock upload logic
    setTimeout(() => {
      setStatus("Processing Interpolation...");
      setTimeout(() => setStatus("Completed!"), 2000);
    }, 1000);
  };

  return (
    <div className="min-h-screen bg-gray-900 text-white p-8">
      <Head>
        <title>Fill in the Frames</title>
      </Head>
      <header className="mb-8">
        <h1 className="text-4xl font-bold bg-clip-text text-transparent bg-gradient-to-r from-blue-400 to-emerald-400">
          Fill in the Frames Seamlessly
        </h1>
        <p className="text-gray-400 mt-2">Enhancing Temporal Resolution of Satellite Imagery</p>
      </header>

      <main className="grid grid-cols-1 md:grid-cols-2 gap-8">
        <section className="bg-gray-800 p-6 rounded-xl shadow-lg border border-gray-700">
          <h2 className="text-2xl font-semibold mb-4">Control Panel</h2>
          <div className="flex flex-col gap-4">
            <label className="block">
              <span className="text-gray-300">Upload Dataset (.nc, .h5)</span>
              <input type="file" className="mt-2 block w-full text-sm text-gray-400 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-600 file:text-white hover:file:bg-blue-700" onChange={handleUpload}/>
            </label>
            <div className="p-4 bg-gray-700 rounded-lg mt-4">
              <p>Status: <span className="font-bold text-emerald-400">{status}</span></p>
            </div>
          </div>
        </section>

        <section className="bg-gray-800 p-6 rounded-xl shadow-lg border border-gray-700">
          <h2 className="text-2xl font-semibold mb-4">Visualization</h2>
          <div className="w-full h-64 bg-black rounded-lg flex items-center justify-center border border-gray-600 overflow-hidden relative">
             {status === "Completed!" ? (
                <div className="text-center text-emerald-400">
                   <p className="mb-2">Interpolation Generated</p>
                   <p className="text-sm text-gray-500">SSIM: 0.95 | PSNR: 32.4 dB</p>
                </div>
             ) : (
                <p className="text-gray-500">Awaiting Data...</p>
             )}
          </div>
        </section>
      </main>
    </div>
  );
}
