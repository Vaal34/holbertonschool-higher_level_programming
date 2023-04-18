#!/usr/bin/node

const request = require('request');
const argv = process.argv
const url = argv[2]
let dict = {}

request(url, function (err, content, body) {
    let count = 0
    if (err) {
        console.log(err)
    } else {
        let data = JSON.parse(body)
        
            for (value of data) {
                if (value["completed"] == true)
                    count += 1
        }
    }
    console.log(count)
})