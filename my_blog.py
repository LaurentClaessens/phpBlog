#! /usr/bin/env python3
# -*- coding: utf8 -*-

from Blog import Blog
from ArticleSummary import ArticleSummary
from MdToBlogHtml import md_to_blog_html


debootstrap=ArticleSummary(name="debootstrap")
debootstrap.set_title("Install Ubuntu with debootstrap")
debootstrap.set_date("Octobre 2016")
debootstrap.set_description("This is how I actually install my Ubutnu, using deboostrap.")
                

frido_presentation=ArticleSummary(name="frido_presentation")
frido_presentation.set_title("Présentation du Frido")
frido_presentation.set_date("Octobre 2016")
frido_presentation.set_description("Une courte présentation du Frido, un cours de mathématique destiné aux candidats à l'agrégation")
                

esperanto=ArticleSummary(name="esperanto")
esperanto.set_title("Pourquoi l'esperanto n'est pas le bonne solution ?")
esperanto.set_date("Octobre 2016")
esperanto.set_description("Une réponse définitive à la question du titre, qui mettre tout le monde d'accord.")
                

liens1=ArticleSummary(name="liens_1")
liens1.set_title("Liens - 1")
liens1.set_date("Novembre 2016")
liens1.set_description("Quelque liens intéressants")
                

frido_vente=ArticleSummary(name="frido_vente")
frido_vente.set_title("Le Frido est en vente")
frido_vente.set_date("Novembre 2016")
frido_vente.set_description("Le Frido est maintenat commercialisé, ce qui en fait un livre utilisable à l'agrégation.")
                
climat_tech=ArticleSummary(name="climat_et_technologie")
climat_tech.set_title("Climat et technologie")
climat_tech.set_date("Novembre 2016")
climat_tech.set_description("Il y a un petit paradoxe à croire en même temps au «problème» climatique et à une énorme accélération technologie pour les prochaines décennies. ")
                

facebook=ArticleSummary(name="facebook_ne_censure_pas")
facebook.set_title("Facebook ne censure pas")
facebook.set_date("Novembre 2016")
facebook.set_description("Non, Facebook ne censure pas. C'est juste un éditeur à bas coût qui vous fournit un travail de mauvaise qualité.")
                
liens2=ArticleSummary(name="liens_2")
liens2.set_title("Liens - 2")
liens2.set_date("Novembre 2016")
liens2.set_description("Quelque liens intéressants")
                
stack=ArticleSummary(name="mon_stack")
stack.set_title("Mon stack")
stack.set_date("Novembre 2016")
stack.set_description("Mon stack")

hollande=ArticleSummary(name="hollande_croissance")
hollande.set_title("Hollande n'a juste pas eu la croissance sur laquelle il comptait")
hollande.set_date("Novembre 2016")
hollande.set_description("François Hollande n'a pas eu la croissance économique sur laquelle il comptait. Et cela ne dépendait pas de lui. Je crois que tous les autres se seraient plantés de la même façon.")

meta=ArticleSummary(name="meta")
meta.set_title("Qu'est-ce que la méta programmation ?")
meta.set_date("Décembre 2016")
meta.set_description="Du code qui génère du code qui est interprété pour produire du code ..."

frido_liens=ArticleSummary(name="frido_liens")
frido_liens.set_title("Quelque liens parlant du Frido")
frido_liens.set_date("Décembre 2016")
frido_liens.set_description("Je me propose de tenir ici à jour une liste des sites qui parlent du Frido")

duos=ArticleSummary(name="les_duos")
duos.set_title("Les duos qui font bien leur travail")
duos.set_date("Décembre 2016")
duos.set_description("Quelque duos logiciels que j'utilise et qui font du bien")

terminator=ArticleSummary(name="terminal_terminator")
terminator.set_title("Changement de terminal : terminator")
terminator.set_date("Janvier 2017")
terminator.set_description("Pourquoi j'utilise Terminator au lieu de terminology")

epicene=ArticleSummary(name="ecriture_epicene")
epicene.set_title("Contre l'écriture épicène")
epicene.set_date("Janvier 2017")
epicene.set_description("Pourquoi le langage épicène renforce la discrimination.")

frido_recherche=ArticleSummary(name="frido_recherche")
frido_recherche.set_title("Des nouvelles du Frido")
frido_recherche.set_date("Février 2017")
frido_recherche.set_description("Quelque nouvelles du Frido")

liens3=ArticleSummary(name="liens_3")
liens3.set_title("Liens - 3")
liens3.set_date("Février 2017")
liens3.set_description("Quelque liens en vrac")

intro=ArticleSummary(name="intro")
intro.set_title("Mon blog en php")
intro.set_date("Février 2017")
intro.set_description("Quelque mots d'introduction")


itrf=ArticleSummary(name="itrf")
itrf.set_title("Comment créer ses dossiers ITRF ?")
itrf.set_date("Avril 2017")
itrf.set_description("Créer les dossiers ITRF demande de remplir plusieurs fichiers ODT contenant essentiellement la même chose. Comment faire sans duplication de code ?")
md_to_blog_html("html/itrf.md")

article_list=[]
article_list.append(intro)
article_list.append(debootstrap)
article_list.append(frido_presentation)
article_list.append(esperanto)
article_list.append(liens1)
article_list.append(frido_vente)
article_list.append(climat_tech)
article_list.append(facebook)
article_list.append(liens2)
article_list.append(stack)
article_list.append(hollande)
article_list.append(meta)
article_list.append(frido_liens)
article_list.append(duos)
article_list.append(terminator)
article_list.append(epicene)
article_list.append(liens3)
article_list.append(itrf)

blog=Blog("rss.xml")

for art in article_list :
    blog.add_article(art)
