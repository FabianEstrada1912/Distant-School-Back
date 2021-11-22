const express = require('express');
const {Pool} = require('pg');
require('dotenv').config();

const config = {
    user: process.env.DB_USER,
    password: process.env.DB_PASSWORD,
    host: process.env.DB_HOST,
    database: process.env.DB_NAME,
    port:5432,
};

const pool = new Pool(config);

if(pool.connect){
    console.log("si hay conexion con BD");
}else{
    console.log("no hay conexion con BD");
}

function conexion(){
   return pool;
}

module.exports = conexion;