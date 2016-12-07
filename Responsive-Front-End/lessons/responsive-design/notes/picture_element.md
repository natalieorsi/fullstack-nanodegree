#How to display image alternatives based on browser capabilities
A fallback.
```
<picture>
  <source srcset="kittems.webp" type="image/webp">
  <source srcset="kittens.jpeg" type="image/jpeg">
  <img src="kittens.jpg" alt="Two grey tabby kittens">
</picture>
```
The `img src` element is mandatory here!
The first source will be used, if possible. Works like an OR circuit.
