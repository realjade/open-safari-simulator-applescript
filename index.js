/*
 * @Author: jade
 * @Date:   2016-08-16 10:01:46
 * @Last Modified by:   jade
 * @Last Modified time: 2016-08-16 10:07:19
 */

'use strict';
var exec = require('child_process').exec;
exec('osascript ' + __dirname + '/simulator.scpt', function(err, stdout, stderr) {
    console.log(stdout)
    if (err) throw new Error(err);
});
