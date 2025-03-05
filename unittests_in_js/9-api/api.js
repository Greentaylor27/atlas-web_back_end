const express = require('express');
const app = express();
const port = 7865
const welcomeMessage = `Welcome to the payment system`;
const portMessage = `API available on localhost port ${port}`

app.get('/', (req, res) => {
    res.send(welcomeMessage);
});

app.get('/cart/:id', (req, res) => {
    const id = req.params.id;

    if (/^\d+$/.test(id)) {
        res.status(200).send(`Payment methods for cart ${id}\n`);
    }
    else {
        res.status(404).send('id must be a number\n');
    }
});

app.listen(port, () => {
    console.log(portMessage)
});
