const { v4: uuid } = require('uuid');
let workouts = [];

exports.getAll = (req, res) => {
  const { skip = 0, limit = 10 } = req.query;
  res.json(workouts.slice(Number(skip), Number(skip) + Number(limit)));
};

exports.create = (req, res) => {
  const workout = { ...req.body, id: uuid(), date: new Date().toISOString() };
  workouts.push(workout);
  res.status(201).json(workout);
};

exports.remove = (req, res) => {
  const { id } = req.params;
  workouts = workouts.filter(w => w.id !== id);
  res.status(204).end();
};

exports.update = (req, res) => {
  const { id } = req.params;
  const index = workouts.findIndex(w => w.id === id);
  if (index === -1) return res.status(404).json({ error: 'Not found' });
  workouts[index] = { ...workouts[index], ...req.body };
  res.json(workouts[index]);
};
