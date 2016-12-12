#! /usr/bin/env python3
# -*- coding: utf8 -*-

import rssflux

blog=rssflux.Blog("rss.xml")


debootstrap=rssflux.ArticleSummary(name="debootstrap")
debootstrap.set_title("Install Ubuntu with debootstrap")
debootstrap.set_date("Octobre 2016")
debootstrap.set_description("This is how I actually install my Ubutnu, using deboostrap.")
                

frido_presentation=rssflux.ArticleSummary(name="frido_presentation")
frido_presentation.set_title("Présentation du Frido")
frido_presentation.set_date("Octobre 2016")
frido_presentation.set_description("Une courte présentation du Frido, un cours de mathématique destiné aux candidats à l'agrégation")
                

esperanto=rssflux.ArticleSummary(name="esperanto")
esperanto.set_title("Pourquoi l'esperanto n'est pas le bonne solution ?")
esperanto.set_date("Octobre 2016")
esperanto.set_description("Une réponse définitive à la question du titre, qui mettre tout le monde d'accord.")
                

liens1=rssflux.ArticleSummary(name="liens_1")
liens1.set_title("Liens - 1")
liens1.set_date("Novembre 2016")
liens1.set_description("Quelque liens intéressants")
                

frido_vente=rssflux.ArticleSummary(name="frido_vente")
frido_vente.set_title("Le Frido est en vente")
frido_vente.set_date("Novembre 2016")
frido_vente.set_description("Le Frido est maintenat commercialisé, ce qui en fait un livre utilisable à l'agrégation.")
                
climat_tech=rssflux.ArticleSummary(name="Climat_et_technoligie")
climat_tech.set_title("Climat et technologie")
climat_tech.set_date("Novembre 2016")
climat_tech.set_description("Il y a un petit paradoxe à croire en même temps au «problème» climatique et à une énorme accélération technologie pour les prochaines décenies. ")
                

facebook=rssflux.ArticleSummary(name="facebook_ne_censure_pas")
facebook.set_title("Facebook ne censure pas")
facebook.set_date("Novembre 2016")
facebook.set_description("Non, Facebook ne censure pas. C'est juste un éditeur à bas coût qui vous fournit un travail de mauvaise qualité.")
                
liens2=rssflux.ArticleSummary(name="liens_2")
liens2.set_title("Liens - 2")
liens2.set_date("Novembre 2016")
liens2.set_description("Quelque liens intéressants")
                
stack=rssflux.ArticleSummary(name="mon_stack")
stack.set_title("Mon stack")
stack.set_date("Novembre 2016")
stack.set_description("Mon stack")

hollande=rssflux.ArticleSummary(name="hollande_croissance")
hollande.set_title("Hollande n'a juste pas eu la croissance sur laquelle il comptait")
hollande.set_date("Novembre 2016")
hollande.set_description("François Hollande n'a pas eu la croissance économique sur laquelle il comptait. Et cela ne dépendait pas de lui. Je crois que tous les autres se seraient plantés de la même façon.")

meta=rssflux.ArticleSummary(name="meta")
meta.set_title("Qu'est-ce que la méta programmation ?")
meta.set_date("Décembre 2016")
meta.set_description="Du code qui génère du code qui est interprété pour produire du code ..."

article_list=[]
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
article_list=[]
for art in article_list :
    blog.add_article(art)



