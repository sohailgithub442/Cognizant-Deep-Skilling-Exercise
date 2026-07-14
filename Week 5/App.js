import React, { useState, useEffect } from "react";
import {
  BrowserRouter as Router,
  Routes,
  Route,
  Link
} from "react-router-dom";

// Home Component
function Home() {
  return (
    <div>
      <h2>Home</h2>
      <p>Welcome to the Home Page.</p>
    </div>
  );
}

// About Component
function About() {
  return (
    <div>
      <h2>About</h2>
      <p>This is a React Single Page Application using React Router.</p>
    </div>
  );
}

// Contact Component
function Contact() {
  return (
    <div>
      <h2>Contact</h2>
      <p>Email: demo@example.com</p>
    </div>
  );
}

// Main App Component
function App() {
  const [count, setCount] = useState(0);

  // useEffect Hook
  useEffect(() => {
    document.title = `Counter: ${count}`;
  }, [count]);

  return (
    <Router>
      <div style={{ fontFamily: "Arial", padding: "20px", textAlign: "center" }}>
        <h1>React SPA Demo</h1>

        {/* Navigation */}
        <nav>
          <Link to="/">Home</Link> |{" "}
          <Link to="/about">About</Link> |{" "}
          <Link to="/contact">Contact</Link>
        </nav>

        <hr />

        {/* useState Example */}
        <h2>Counter: {count}</h2>
        <button onClick={() => setCount(count + 1)}>
          Increment
        </button>

        <hr />

        {/* React Router */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about" element={<About />} />
          <Route path="/contact" element={<Contact />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
