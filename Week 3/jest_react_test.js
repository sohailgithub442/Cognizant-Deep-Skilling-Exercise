import React from "react";
import { render, screen } from "@testing-library/react";
import "@testing-library/jest-dom";
import axios from "axios";

// React Component
function App() {
  return <h1>Hello, CTS!</h1>;
}

// Test React Component
test("renders React component", () => {
  render(<App />);
  expect(screen.getByText("Hello, CTS!")).toBeInTheDocument();
});


// Mock API Call
jest.mock("axios");

test("mock API call", async () => {
  axios.get.mockResolvedValue({
    data: {
      id: 1,
      name: "Alice"
    }
  });

  const response = await axios.get("https://api.example.com/user");

  expect(response.data.name).toBe("Alice");
});
