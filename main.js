const express = require('express')
var fs = require('fs')
const {URLSearchParams} = require('url')
const sqlite3 = require('sqlite3')

const app = express()
const port = 80
const host = '0.0.0.0'

app.use(express.static('public'))

var db = new sqlite3.Database("database.db")

app.get("/", (req, res) => {
	res.sendFile("public/templates/main.html", {root: __dirname})
})

app.get("/root/:root", (req, res) => {
	res.sendFile("public/templates/root.html", {root: __dirname})
})

app.get("/root/:root/req", (req, res) => {
	var root = req.params.root

	var command = "select * from roots where root='" + root + "'"

	var run = db.all(command, (err, rows) => {
		if (err){
			console.log(err)
			res.send("{error: " + err + "}")
			return
		}
		if (rows == undefined){
			console.log("COMMAND " + command + " returned UNDEFINED")
			res.send("{error: undefined}")
			return
		}
		if (rows.length == 0){
			console.log("COMMAND " + command + " returned EMPTY")
			res.send("{error: empty result}")
			return
		}
		var response = ''
		//we will use a loop here even though we know that technically, for
		//this specific query, there will only be one row given that the root
		//field is a unique key
		for (var row of rows){
			response = response + JSON.stringify(row) + "\n"
		}
		res.send(response)
	})
})

app.get("/query/:item", (req, res) => {
	var item = req.params.item

	var command = "select * from roots where "
	command = command + "root like '%" + item + "%' or "
	command = command + "definition like '%" + item + "%'"
	//command = command + "derivation like '%" + item + "%'"

	var run = db.all(command, (err, rows) => {
		if (err){
			console.log(err)
			res.send("{error: " + err + "}")
			return
		}
		if (rows == undefined){
			console.log("COMMAND " + command + " returned UNDEFINED")
			res.send("{error: undefined}")
			return
		}
		if (rows.length == 0){
			console.log("COMMAND " + command + " returned EMPTY")
			res.send("{error: empty result}")
			return
		}
		var response = ''
		//we will use a loop here even though we know that technically, for
		//this specific query, there will only be one row given that the root
		//field is a unique key
		for (var row of rows){
			response = response + JSON.stringify(row) + "\n"
		}
		res.send(response)
	})
})

app.listen(process.env.PORT || port, host)