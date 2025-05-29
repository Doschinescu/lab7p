const express = require('express');
const router = express.Router();
const controller = require('../controllers/workoutController');

router.get('/', controller.getAll);
router.post('/', controller.create);
router.delete('/:id', controller.remove);
router.put('/:id', controller.update);

module.exports = router;
