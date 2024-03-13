#!/usr/bin/node
const OldSquare = require('./5-square');
class Square extends OldSquare {
	charPrint(c) {
		let k = 'X';
		if (c !== undefined)
			k = c;
		for (let i = 0 ; i < this.width ; i++) {
			let s = ''
			for (let j = 0; j < this.height ; j++) {
				s += k;
			}
			console.log(s);
		}
	}
}
module.exports = Square;
