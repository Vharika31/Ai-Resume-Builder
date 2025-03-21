import Link from "next/link";
import Navbar from "@/app/components/Navbar";

export default function Home() {
  return (
    <div className="min-h-screen bg-gray-100">
      <Navbar />
      <main className="flex flex-col items-center justify-center py-10">
        <h1 className="text-4xl font-bold text-gray-900 mb-6">AI Resume Generator</h1>
        <p className="text-lg text-gray-600 mb-8">Create professional AI-powered resumes in seconds.</p>
        <div className="flex space-x-4">
          <Link href="/auth">
            <button className="bg-blue-600 text-white px-6 py-3 rounded-lg shadow-md hover:bg-blue-700">
              Get Started
            </button>
          </Link>
          <Link href="/dashboard">
            <button className="bg-gray-700 text-white px-6 py-3 rounded-lg shadow-md hover:bg-gray-800">
              Go to Dashboard
            </button>
          </Link>
        </div>
      </main>
    </div>
  );
}
