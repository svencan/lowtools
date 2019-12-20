# lowtools

Most CLI programs are not intuitive, so lowtools was created.

Here's what you can do:

## rcase

Returns the given string with randomly capitalized letters.

```
$ rcase Can we get serious now?
CAN We geT SERioUS nOW?
```

## translate

Translates from a source language to one or more destination languages, optionally gives you the google translate links for it. If no source language is given it is guessed. If no destination language is given it translates to your default language.

```
$ translate from english to german, luxembourgish: English motherfucker do you speak it?
Can only give you links for now...

German:
https://translate.google.com/?view=home&op=translate&sl=english&tl=DE&text=English%20motherfucker%20do%20you%20speak%20it%3F

Luxembourgish:
https://translate.google.com/?view=home&op=translate&sl=english&tl=LB&text=English%20motherfucker%20do%20you%20speak%20it%3F

French:
https://translate.google.com/?view=home&op=translate&sl=english&tl=FR&text=English%20motherfucker%20do%20you%20speak%20it%3F
```

```
$ translate to french: Mein Baguette ist gebrochen.
Can only give you links for now...

French:
https://translate.google.com/?view=home&op=translate&sl=auto&tl=FR&text=Mein%20Baguette%20ist%20gebrochen.
```