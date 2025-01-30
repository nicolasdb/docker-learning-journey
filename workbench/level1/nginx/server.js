const express = require('express');
const fs = require('fs');
const path = require('path');
const app = express();
const logFilePath = path.join(__dirname, 'data', 'log.txt');

app.use(express.urlencoded({ extended: true }));

app.post('/log', (req, res) => {
    const entry = req.body.entry;
    fs.appendFileSync(logFilePath, `${entry}\n`);
    res.redirect('/');
});

app.get('/log', (req, res) => {
    if (fs.existsSync(logFilePath)) {
        const logContent = fs.readFileSync(logFilePath, 'utf-8');
        res.send(logContent);
    } else {
        res.send('');
    }
});

app.use(express.static(path.join(__dirname)));

app.listen(3000, () => {
    console.log('Server is running on port 3000');
});