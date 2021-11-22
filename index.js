const express = require('express');
const cors = require('cors');
const app = express();
const http = require('http').createServer(app);
const path = require('path');
const multer = require('multer');

const conexion = require('./BD/conexion.js');
const profile = require('./Profile/profile.js');
const chats = require('./chat/chat.js');

const pool  = conexion();

const io = require('socket.io')(http, {
    cors: {
        origin: '*'
    }
});

app.get('/', (req, res) => {
    res.send('Heello world');
})

app.use(function(req, res, next) {
    res.header("Access-Control-Allow-Origin", "*");
    res.header("Access-Control-Allow-Headers", "X-Requested-With");
    res.header("Access-Control-Allow-Headers", "Content-Type");
    res.header("Access-Control-Allow-Methods", "PUT, GET, POST, DELETE, OPTIONS");
    next();
 });

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/Archivo',express.static(path.join(__dirname,'/Archivo')));

profile(app,pool);
chats(app,pool,io);

http.listen(process.env.PORT || 3000, () => {
    console.log(`Server is running ${process.env.PORT || 3000}`);
});