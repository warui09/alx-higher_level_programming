#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const len = list.length;

  for (let i = 0, j = len - 1; i < len, j >= 0; i++, j--) {
    newList[i] = list[j];
  }

  return newList;
};
