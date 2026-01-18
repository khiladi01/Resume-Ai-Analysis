import express from 'express';
// import cors from 'cors';
import dotenv from 'dotenv';

// Load environment variables
dotenv.config();

const app = express();
const PORT = process.env.PORT || 3000;

// Middleware
// app.use(cors());
app.use(express.json());
// app.use(express.urlencoded({ extended: true }));

// Check route
app.get('/', (req, res) => {
  res.send("Server started successfully");
});

// Start server
app.listen(PORT, () => {
  console.log(`Server is running on port http://localhost:${PORT}`);
});

