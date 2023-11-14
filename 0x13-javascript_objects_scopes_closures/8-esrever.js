#!/usr/bin/node
exports.esrever = function (list) {
  const newList = [];
  const len = list.length;
  let i = 0;
  let j = len - 1;

  while (i < len) {
    newList[i] = list[j];
    i++;
    j--;
  }

  return newList;
};
