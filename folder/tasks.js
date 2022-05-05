const express = require("express")
const app = express()

app.get("/download", (req, res)=>{
    const file = `${__dirname}/test.txt`
    res.download(file)
})

app.listen(3333, ()=>{
    console.log('App listening on port 3333')
})