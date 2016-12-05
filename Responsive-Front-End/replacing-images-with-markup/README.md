#About
This class is all about reducing the latency of a website by finding alternatives to standard image requests, in order to reduce the number of image requests the browser needs to make. Such techniques include CSS techniques such as CSS generated background images, symbol characters, icon fonts, and inlining images with SVG and data URIs.

#CSS "Image" Rendering
Unlike in my bad old days of coding up Neopets themes as a child, fonts, backdrops to fonts, and shadows can finally be done in-browser without having to fire up GIMP and upload an image to a server.

Useful `div` elements here include `background:`
* `background: linear-gradient(black,red);
`border-radius`
* `100px` produces a button effect
`box-shadow` will drop a shadow for the button
* i.e., `5px 5px 20px 0 black`
And of course, animations
* `-webkit-animation: spin 2s`

So, everything my 10 year old heart might have spent an hour painstakingly drawing, animating, and uploading can now be done in a few lines of code without having to choke up the number of HTTP requests or causing significant loading delays.

Of course, there are rendering costs. Gradient and keyframe animations take less than half as long to load as Box shadow, but combined they these features can multiply the rendering time by four relative to gradient or keyframe animations alone.

#CSS Background Rendering

You can achieve some pretty fantastic background images using CSS.

[Example]: http://udacity.github.io/responsive-images/examples/2-06/bodyWithElaboratePatternPureCSS/ 

```<style>
    body {
      background:
      linear-gradient(27deg, #151515 5px, transparent 5px) 0 5px,
      linear-gradient(207deg, #151515 5px, transparent 5px) 10px 0px,
      linear-gradient(27deg, #222 5px, transparent 5px) 0px 10px,
      linear-gradient(207deg, #222 5px, transparent 5px) 10px 5px,
      linear-gradient(90deg, #1b1b1b 10px, transparent 10px),
      linear-gradient(#1d1d1d 25%, #1a1a1a 25%, #1a1a1a 50%, transparent 50%, transparent 75%, #242424 75%, #242424);
      background-color: #131313;
      background-size: 20px 20px;
    }
  </style>
  ```

More examples:
* [Div with background image](http://udacity.github.io/responsive-images/examples/2-06/divWithBackgroundImage)
* [CSS background-size: cover](http://udacity.github.io/responsive-images/examples/2-06/backgroundSizeCover)
* [Body with background image](http://udacity.github.io/responsive-images/examples/2-06/bodyWithBackgroundImage)
* [Body with background image and gradient](http://udacity.github.io/responsive-images/examples/2-06/bodyWithBackgroundImageAndGradient)
* [Body with elaborate background using only CSS](http://udacity.github.io/responsive-images/examples/2-06/bodyWithElaboratePatternPureCSS)
* [Using CSS background images for conditional image display](http://udacity.github.io/responsive-images/examples/2-06/backgroundImageConditional)
* [Using CSS background images for alternative images](http://udacity.github.io/responsive-images/examples/2-06/backgroundImageAlternative)
* [image-set()](http://udacity.github.io/responsive-images/examples/2-06/imageSet)

#Replace images with Unicode symbol characters
[Example]: http://udacity.github.io/responsive-images/examples/2-08/unicodeStar/
Infinitely scalable and responsive without making any image requests!
* [Unicode character sets](http://unicode-table.com/en/sets/)
* [List of Unicode characters](http://en.wikipedia.org/wiki/List_of_Unicode_characters)
* Be sure to set your charset to utf-8 with `<meta http-equiv="Content-Type" content="text/html; charset=utf-8">`
* Nowadays, you no longer have to paste something like `&#119070;` into your HTML; it's now recommended just to paste in the actual symbol! Take that, 2005.

#Icon fonts
* [Zocial](http://zocial.smcllns.com/) is an excellent image-free icon font solution to including social buttons to your website.
* [Font Awesome](http://fortawesome.github.io/Font-Awesome/)
* [We Love Icon Fonts!](http://weloveiconfonts.com/)
* [Icon fonts on CSS-Tricks](https://css-tricks.com/examples/IconFont/) has a cool slider to play with and create icon fonts yourself.

#Inline Images with SVG and Data URIs
Data URIs be implemented in HTML or CSS and are well supported.
* This technique lowers both file sizes and HTTP requests.
* [SVG Data URI in HTML](http://udacity.github.io/responsive-images/examples/2-11/svgDataUri)
* [SVG Data URI in CSS](http://udacity.github.io/responsive-images/examples/2-11/svgDataUriCss)
* [SVG text on a path](http://udacity.github.io/responsive-images/examples/2-11/svgTextOnAPath)
* [SVG optimized and unoptimized](http://udacity.github.io/responsive-images/examples/2-11/svgUnoptimisedAndOptimised)
* [Browser support for inline SVG](http://caniuse.com/#feat=svg-html5)
* [Browser support for Data URIs](http://caniuse.com/datauri)
* [SVG Optimiser](http://petercollingridge.appspot.com/svg-optimiser)
More examples:
* [Trajan's Column SVG example](http://upload.wikimedia.org/wikipedia/commons/6/6c/Trajans-Column-lower-animated.svg) - interactive!
* [20 examples of SVG that will make your jaw drop](http://www.creativebloq.com/design/examples-svg-7112785)
* [SVG animation examples](http://codepen.io/chrisgannon/)

#Drawbacks to this technique
* If you are going to call the same image across pages, it can be better to set its `srcs` to an external file in order to take advantage of the browser's caching techniques, rather than rendering the image over and over again.
* Inline images can limit your responsive options
