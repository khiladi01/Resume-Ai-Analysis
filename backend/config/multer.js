import express from "express"
import multer from "multer"
const upload = multer({ storage: 'uploads/' })

const app = express()

app.post('/resume', upload.single('pdf'), function (req, res, next) {
  // req.file is the `avatar` file
  // req.body will hold the text fields, if there were any
})

const uploadMiddleware = upload.fields({ name: 'pdf', maxCount: 1 })
app.post('/cool-profile', uploadMiddleware, function (req, res, next) {
  // req.files is an object (String -> Array) where fieldname is the key, and the value is array of files
  //
  // e.g.
  //  req.files['avatar'][0] -> File
  //  req.files['gallery'] -> Array
  //
  // req.body will contain the text fields, if there were any
})