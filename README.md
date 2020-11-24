# PythonStructuralLanguage
Language for making python desktop apps.

## Syntax

The PSL language is in base similar to html but there are some differences.

When you are using HTML u would do this to make basic structure for your web page:
```html
<html>
  <head>
    <meta charset="utf-8">
  </head>
  <body>
    <label>Some text</label>
  </body>
</html>
```
But in PSL it look like this:
```html
<formspace>
  <form,name="window1",dimensions="500x500">
    <label,name="sometext">Some text</label>
  </form>
</formspace>
```
