import Link from "next/link";

export default function Navbar() {
  return (
    <nav className="bg-gray-900 text-white py-4 px-6 flex justify-between items-center">
      <h1 className="text-xl font-semibold">AI Resume Generator</h1>
      <div className="space-x-4">
        <Link href="/">
          <button className="bg-blue-600 px-4 py-2 rounded-lg hover:bg-blue-700">
            Home
          </button>
        </Link>
        <Link href="/dashboard">
          <button className="bg-gray-700 px-4 py-2 rounded-lg hover:bg-gray-800">
            Dashboard
          </button>
        </Link>
        <Link href="/auth">
          <button className="bg-green-600 px-4 py-2 rounded-lg hover:bg-green-700">
            Login
          </button>
        </Link>
      </div>
    </nav>
  );
}
