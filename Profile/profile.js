const express = require('express');
const path = require('path');
const multer = require('multer');


let storage = multer.diskStorage({
    destination: (req, file, cb) => {
        cb(null, './Archivo')
    },
    
    filename: (req, file, cb) => {
        cb(null, file.fieldname+ '_'+Date.now()+path.extname(file.originalname))
    }
});

const subir = multer({ storage });

function profile(app,pool){
    const router = express.Router();
    app.use('/api', router);

    router.put('/foto/:id', subir.single('file'),async (req, res,next) =>{
        try {
            const file = req.file;
            if(!file){
              const error = new Error('No File')
              error.httpStatusCode = 400
              return next(error)
            }

            try {
                var photo = file.path.replace("\\", "/");
                var id = parseInt(req.params.id);
                const users = await pool.query('UPDATE "Profile" SET  photo=$1 WHERE user_id =$2',[photo,id]);
                return res.send("ya quedo")
            } catch (error) {
                return res.send("i am sorry");
            }
        } catch (e) {
            console.log(e);
            return res.send("i am sorry");
        }
    });

    router.put('/fotoGrupo/:id', subir.single('file'),async (req, res,next) =>{
        try {
            const file = req.file;
            if(!file){
              const error = new Error('No File')
              error.httpStatusCode = 400
              return next(error)
            }

            try {
                var photo = file.path.replace("\\", "/");
                var id = parseInt(req.params.id);
                const users = await pool.query('UPDATE "Chat" SET  photo=$1 WHERE id =$2',[photo,id]);
                return res.send("ya quedo")
            } catch (error) {
                return res.send("i am sorry");
            }
        } catch (e) {
            console.log(e);
            return res.send("i am sorry");
        }
    });
}

module.exports = profile;
