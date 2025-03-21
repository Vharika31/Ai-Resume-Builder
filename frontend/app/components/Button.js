export default function Button({ children, onClick, className = "" }) {
    return (
      <button
        className={`bg-blue-600 text-white hover:bg-blue-700 ${className}`}
        onClick={onClick}
      >
        {children}
      </button>
    );
  }
  