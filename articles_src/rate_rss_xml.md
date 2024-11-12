## Raté en xml

Je crois que j'ai bien raté mon coup hier soir en voulant corriger mon `rss.xml`.

### Le problème

Un lecteur m'a averti que les liens dans le lecteur RSS étaient mauvais. La raison est que l'entête de mon `rss.xml` était comme ceci :
```
        <rss version="2.0"> 
            <channel> 
                <title>Blog de Laurent Claessens</title> 
                <link>http://laurent.claessens-donadello.eu/blog</link> 
                <description>
                    Mon blog personnel, tout fait à la main en Vim.
                </description>
```
et que les articles sont comme ceci :
```
                <link>html/debootstrap.html</link>
```
Si j'ai bien compris, le manque de `/` à la fin de l'URL dans l'entête du RSS provoque que la concaténation des deux `link` crée des URL comme
```
http://laurent.claessens-donadello.eu/html/debootstrap.html
```
au lieu de
```
http://laurent.claessens-donadello.eu/blog/html/debootstrap.html
```


### La solution

Cela est probablement fixé. J'en ai profité pour changer `http` en `https`.

Cela pour dire que vous avez probablement reçu deux fois l'entièreté des article de ce blog dans vos aggrégateurs RSS. Désolé.

### Rien à voir

J'en profite pour voir si les formules mathématiques passent.


En voici une :

<math>
  <mrow>
    <mi>a</mi>
    <mo>=</mo>
    <mrow>
      <mo>-</mo>
      <mrow>
        <mi>b</mi>
        <mo>⁢</mo>
        <mfrac>
          <mi>k</mi>
          <mi>L</mi>
        </mfrac>
      </mrow>
    </mrow>
  </mrow>
</math>

Le code mathml a été obtenu par
```
sudo apt install latexml
latexmlmath (cat ess.tex)
```
où le fichier `ess.tex` contient le code LaTeX.


Voici tel que l'exemple [de wikipédia](https://fr.wikipedia.org/wiki/MathML)

<math>
  <mrow>
    <mi>x</mi>
    <mo>=</mo>
    <mfrac>
      <mrow>
        <mrow>
          <mo>-</mo>
          <mi>b</mi>
        </mrow>
        <mo>&PlusMinus;</mo>
        <msqrt>
          <mrow>
            <msup>
              <mi>b</mi>
              <mn>2</mn>
            </msup>
            <mo>-</mo>
            <mrow>
              <mn>4</mn>
              <mo>&InvisibleTimes;</mo>
              <mi>a</mi>
              <mo>&InvisibleTimes;</mo>
              <mi>c</mi>
            </mrow>
          </mrow>
        </msqrt>
      </mrow>
      <mrow>
        <mn>2</mn>
        <mo>&InvisibleTimes;</mo>
        <mi>a</mi>
      </mrow>
    </mfrac>
  </mrow>
</math>

Ça ne passe pas dans Konqueror, mais chez moi ça a l'air d'être bon pour Firefox.

Si quelqu'un sait comme [fait Djalil Chafaï](https://djalil.chafai.net/blog/2020/12/21/an-exactly-solvable-model/), je suis preneur.

