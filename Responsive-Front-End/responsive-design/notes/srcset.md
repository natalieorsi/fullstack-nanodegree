#Alternative image sources based on display
* [srcset with w values](http://udacity.github.io/responsive-images/examples/3-03/srcsetWValues/)
`<img src="small.jpg" srcset="small.jpg 500w, medium.jpg 1000w, large.jpg 1500w" alt="Wallaby">`

* [srcset with w values, 50vw](http://udacity.github.io/responsive-images/examples/3-03/srcsetWValues50vw/)
`http://udacity.github.io/responsive-images/examples/3-03/srcsetWValues50vw/small.jpg`

##[Video Explanation](https://www.youtube.com/watch?v=Vv7_pYXmX0I)

#Srcset's two flavors
There are two flavors of `srcset`, one using `x` to differentiate between device pixel ratios (DPR), and the other using `w` to describe the image's width.

#Reacting to Device Pixel Ratio
`<img src="image_2x.jpg" srcset="image_2x.jpg 2x, image_1x.jpg 1x" alt="a cool image">`
Set srcset equal to a comma separated string of filename multiplier pairs, where each multiplier must be an integer followed by an `x`.
For example, `1x` represents `1x` displays and `2x` represents displays with twice the pixel density, like Apple's Retina displays.

The browser will download the image that best corresponds to its DPR.

Also, note that there's a `src` attribute as a fallback.

#Reacting to Image Width
`<img src="image_200.jpg" srcset="image_200.jpg 200w, image_100.jpg 100w" alt="a cool image">`
Set `srcset` equal to a comma separated string of `filename widthDescriptor` pairs, where each `widthDescriptor` is measured in pixels and must be an integer followed by a `w`. Here, the `widthDescriptor` gives the natural width of each image file, which enables the browser to choose the most appropriate image to request, depending on viewport size and DPR. (Without the `widthDescriptor`, the browser cannot know the width of an image **without downloading it!**)

Also, note that there's a `src` attribute as a fallback.

#Image Width with sizes
What if the image won't be displayed at the full viewport width? Then you need something more than `srcset`, which assumes the image will be full viewport width.

Add a `sizes` attribute to the image with a media query and a `vw` value. `srcset` and `sizes` together tell the browser the natural width of the image, and how wide the image will be displayed relative to viewport width. Knowing the display width of the image and the widths of the image files available to it, the browser has the information it needs to download the image with the right resolution for its needs that is as small as possible. And it can make this choice early in the page load while the HTML is still being parsed.

#`srcset` with `sizes` Syntax
Here's an example:

```
<img  src="images/great_pic_800.jpg"
      sizes="(max-width: 400px) 100vw, (min-width: 401px) 50vw"
      srcset="images/great_pic_400.jpg 400w, images/great_pic_800.jpg 800w"
      alt="great picture">
```
`sizes` consists of comma separated `mediaQuery width` pairs. `sizes` tells the browser early in the load process that the image will be displayed at some width when the mediaQuery is hit.

In fact, if `sizes` is missing, the browser defaults sizes to `100vw`, meaning that it expects the image will display at the full viewport width.

`sizes` gives the browser one more piece of information to ensure that it downloads the right image file based on the eventual display width of the image. Just to be clear, it does not actually resize the image - that's what CSS does.

In this example, the browser knows that the image will be full viewport width if the browser's viewport is `400px` wide or less, and half viewport width if greater than `400px`. It knows that it has two image options - one with a natural width of `400px` and the other `800px`.

#Fallback for browsers that don't yet support `srcset`
Picturefill polyfill is a script that allows older browsers to use `srcset`
* [demo](http://udacity.github.io/responsive-images/examples/3-08/picturefill/)
* [download](http://scottjehl.github.io/picturefill/)
