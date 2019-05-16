const express = require('express')
const path = require('path')

var cors = require('cors')
const pathToSwaggerUi = require('swagger-ui-dist').absolutePath()

const app = express()

app.use(cors())
app.use(express.static(pathToSwaggerUi))
app.listen(3000)

const app2 = express()
app2.use(cors())
app2.use(express.static(__dirname))
app2.listen(4000)
