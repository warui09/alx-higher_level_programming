#!/usr/bin/node
exports.converter = function (base) {
  function toDecimal (num) {
    return Math.floor(parseFloat(num));
  }

  function toHex (num) {
    return num.toString(16);
  }

  switch (base) {
    case 10:
      return toDecimal;
      break;
    case 16:
      return toHex;
      break;
    default:
  }
};
