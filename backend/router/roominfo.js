const express = require('express');
const router = express.Router();

router.post('/roominfo', function(req,res){
    var topic = req.body.topics;
    console.log( topic);
    return res.status(200).json(req.topics);
});

module.exports = router;