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

Translates from a source language to one or more destination languages.

```
$ translate from luxembourgish to english, german, spanish, portuguese: Mir wëlle bleiwen wat mir sinn.
English:
We want to remain what we are.

German:
Wir wollen bleiben, was wir sind.

Spanish:
Queremos seguir siendo lo que somos.

Portuguese:
Queremos continuar sendo o que somos
```

You don't have to specify a source language.

```
$ translate to french: English, motherfucker, do you speak it?
French:
Anglais, enculé, tu le parles?
```

You can opt to just receive the google translator links.

```
$ translate to spanish: What? -l -c
Spanish:
https://translate.google.com/?view=home&op=translate&sl=auto&tl=ES&text=What%3F

Copied to clipboard
```