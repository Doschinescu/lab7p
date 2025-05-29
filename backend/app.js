const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const workoutRoutes = require('./routes/workouts');
const authMiddleware = require('./middleware/auth');
const jwt = require('jsonwebtoken');
require('dotenv').config();
const swaggerUi = require('swagger-ui-express');
const swaggerDoc = require('./swagger.json');

const app = express();
app.use(cors());
app.use(bodyParser.json());

const PORT = process.env.PORT || 3000;

app.post('/token', (req, res) => {
  const { role = 'VISITOR', permissions = ['READ'] } = req.body;
  const token = jwt.sign({ role, permissions }, process.env.JWT_SECRET, {
    expiresIn: process.env.JWT_EXPIRATION,
  });
  res.json({ token });
});

app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDoc));
app.use('/workouts', authMiddleware, workoutRoutes);

app.listen(PORT, () => console.log(`Backend running on port ${PORT}`));
