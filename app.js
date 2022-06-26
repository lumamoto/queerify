const express = require("express");
const morgan = require("morgan");
const cookieParser = require("cookie-parser");
const path = require("path");
const cors = require("cors");
var shelljs = require("shelljs");
const process = require("process");

let app = express();
const port = process.env.PORT || 8001;
const hostname = process.env.HOST || "0.0.0.0";
//middleware
app.use(express.static(__dirname + "/frontend"));
app.use(express.json());
app.use(
  cors({
    origin: "*",
  })
);
//solved cors error
app.use(express.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(morgan("common"));

app.all("/*", function (req, res, next) {
  res.header("Access-Control-Allow-Origin", "*");
  res.header("Access-Control-Allow-Methods", "GET,PUT,POST,DELETE,OPTIONS");
  res.header(
    "Access-Control-Allow-Headers",
    "Content-Type, Authorization, Content-Length"
  );
  next();
});

//uses the routes defined in the router in index.js

// app.get("/", (req, res) => {
//   res.writeHead(200);
//   res.end("Hello");
// });
// app.post("/", (req, res) => {
//   res.send("Post here");
// });
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname + "/frontend/index.html"));
});
app.listen(port, hostname, () => {
  console.log(`Server running at http://${hostname}:${port}/`);
});
module.exports = app;
