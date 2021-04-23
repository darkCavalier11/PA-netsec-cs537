/**
 * provide text and offset it returns the encrypted text
 * @param {String} text
 * @param {Number} offset
 */
const encrypt = function (text, offset) {
  let encText = "";
  for (let i = 0; i < text.length; i++) {
    /** if current letter >= ascii a i.e. 97 it will 
    offset it by first beinging it to 0 level and then adding the offset*/
    if (text[i] >= "a") {
      let c = ((text.charCodeAt(i) - 97 + offset) % 26) + 97;
      encText += String.fromCharCode(c);
    /** if current letter is between ASCII of 'A' to 'Z' it simmply
    brings it to 0 level and the applying the offset */
    } else if (text[i] >= "A" && text[i] <= "Z") {
      let c = ((text.charCodeAt(i) - 65 + offset) % 26) + 65;
      encText += String.fromCharCode(c);
    } else {
      encText += text[i];
    }
  }
  return encText;
};

/**
 * provide encrypted text and it will return decrypted text
 * decrypt is just -offset 
 */
const decrypt = function (text, offset) {
  return encrypt(text, -offset);
};

/**
 * get current text and encrypt it and update the text fields
 */
const dec = document.querySelector(".dec-text-area");
const enc = document.querySelector(".enc-text-area");

/**
 changing the value of text dynamically when input changes
*/

dec.addEventListener("input", (e) => {
  enc.value = encrypt(e.target.value, 3);
});

enc.addEventListener("input", (e) => {
    dec.value = decrypt(e.target.value, 3);
});
  
  
