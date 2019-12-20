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

You can opt to just receive the google translator links and/or copy the output to the clipboard.

```
$ translate to spanish: What? -l -c
Spanish:
https://translate.google.com/?view=home&op=translate&sl=auto&tl=ES&text=What%3F

Copied to clipboard
```

Instead of writing text, you can specify a text file to be translated:

```
$ cat song.txt
Ech wëll net schaffen,
ech wëll net frühstücken,
ech wëll nëmmen vergiessen,
an duerno fëmmen ech!
$ translate to french: song.txt
French:
Je ne veux pas travailler,je ne veux pas déjeuner,je veux juste oublier,et puis je fume!
```