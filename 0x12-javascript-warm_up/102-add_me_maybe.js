#!/usr/bin/node
exports.addMeMaybe = function (x, fun) {
  fun(++x);
};
