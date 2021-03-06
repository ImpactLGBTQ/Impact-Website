/**
 * Cookie consent js configuration and setup file
 */

window.cookieconsent.initialise({
  "palette": {
    "popup": {
      "background": "#343c66",
      "text": "#cfcfe8"
    },
    "button": {
      "background": "transparent",
      "text": "#f71559",
      "border": "#f71559"
    }
  },
  "position": "bottom-right",
  "content": {
    "message": "This website uses cookies to improve your experience. We do not collect any data which could be used" +
        " to personally identify you",
    "dismiss": "That's fine",
   // "href": "/data-policy"
  }
});
