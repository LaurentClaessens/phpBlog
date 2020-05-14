#! venv/bin/python3

from src.blog import Blog
from src.article_summary import ArticleSummary

blog = Blog()


article = ArticleSummary(name="debootstrap", blog=blog)
article.set_title("Install Ubuntu with debootstrap")
article.set_date("Octobre 2016")
article.set_description("This is how I actually install my Ubutnu, using deboostrap.")
blog.add_article(article)


article = ArticleSummary(name="frido_presentation", blog=blog)
article.set_title("Présentation du Frido")
article.set_date("Octobre 2016")
article.set_description("Une courte présentation du Frido, un cours de mathématique destiné aux candidats à l'agrégation")
blog.add_article(article)


article = ArticleSummary(name="esperanto", blog=blog)
article.set_title("Pourquoi l'esperanto n'est pas le bonne solution ?")
article.set_date("Octobre 2016")
article.set_description("Une réponse définitive à la question du titre, qui mettre tout le monde d'accord.")
blog.add_article(article)


article = ArticleSummary(name="liens_1", blog=blog)
article.set_title("Liens - 1")
article.set_date("Novembre 2016")
article.set_description("Quelque liens intéressants")
blog.add_article(article)


article = ArticleSummary(name="frido_vente", blog=blog)
article.set_title("Le Frido est en vente")
article.set_date("Novembre 2016")
article.set_description("Le Frido est maintenat commercialisé, ce qui en fait un livre utilisable à l'agrégation.")
blog.add_article(article)

article = ArticleSummary(name="climat_et_technologie", blog=blog)
article.set_title("Climat et technologie")
article.set_date("Novembre 2016")
article.set_description("Il y a un petit paradoxe à croire en même temps au «problème» climatique et à une énorme accélération technologie pour les prochaines décennies. ")
blog.add_article(article)

article = ArticleSummary(name="facebook_ne_censure_pas", blog=blog)
article.set_title("Facebook ne censure pas")
article.set_date("Novembre 2016")
article.set_description("Non, Facebook ne censure pas. C'est juste un éditeur à bas coût qui vous fournit un travail de mauvaise qualité.")
blog.add_article(article)

article = ArticleSummary(name="liens_2", blog=blog)
article.set_title("Liens - 2")
article.set_date("Novembre 2016")
article.set_description("Quelque liens intéressants")
blog.add_article(article)

article = ArticleSummary(name="mon_stack", blog=blog)
article.set_title("Mon stack")
article.set_date("Novembre 2016")
article.set_description("Mon stack")
blog.add_article(article)

article = ArticleSummary(name="hollande_croissance", blog=blog)
article.set_title("Hollande n'a juste pas eu la croissance sur laquelle il comptait")
article.set_date("Novembre 2016")
article.set_description("François Hollande n'a pas eu la croissance économique sur laquelle il comptait. Et cela ne dépendait pas de lui. Je crois que tous les autres se seraient plantés de la même façon.")
blog.add_article(article)

article = ArticleSummary(name="meta", blog=blog)
article.set_title("Qu'est-ce que la méta programmation ?")
article.set_date("Décembre 2016")
article.set_description="Du code qui génère du code qui est interprété pour produire du code ..."
blog.add_article(article)

article = ArticleSummary(name="frido_liens", blog=blog)
article.set_title("Quelque liens parlant du Frido")
article.set_date("Décembre 2016")
article.set_description("Je me propose de tenir ici à jour une liste des sites qui parlent du Frido")
blog.add_article(article)

article = ArticleSummary(name="les_duos", blog=blog)
article.set_title("Les duos qui font bien leur travail")
article.set_date("Décembre 2016")
article.set_description("Quelque duos logiciels que j'utilise et qui font du bien")
blog.add_article(article)

article = ArticleSummary(name="terminal_terminator", blog=blog)
article.set_title("Changement de terminal : terminator")
article.set_date("Janvier 2017")
article.set_description("Pourquoi j'utilise Terminator au lieu de terminology")
blog.add_article(article)

article = ArticleSummary(name="ecriture_epicene", blog=blog)
article.set_title("Contre l'écriture épicène")
article.set_date("Janvier 2017")
article.set_description("Pourquoi le langage épicène renforce la discrimination.")
blog.add_article(article)

article = ArticleSummary(name="frido_recherche", blog=blog)
article.set_title("Des nouvelles du Frido")
article.set_date("Février 2017")
article.set_description("Quelque nouvelles du Frido")
blog.add_article(article)

article = ArticleSummary(name="liens_3", blog=blog)
article.set_title("Liens - 3")
article.set_date("Février 2017")
article.set_description("Quelque liens en vrac")
blog.add_article(article)

article = ArticleSummary(name="intro", blog=blog)
article.set_title("Mon blog en php")
article.set_date("Février 2017")
article.set_description("Quelque mots d'introduction")
blog.add_article(article)


article = ArticleSummary(name="itrf", blog=blog)
article.set_title("Comment créer ses dossiers ITRF ?")
article.set_date("Avril 2017")
article.set_description("Créer les dossiers ITRF demande de remplir plusieurs fichiers ODT contenant essentiellement la même chose. Comment faire sans duplication de code ?")
blog.add_article(article)

article = ArticleSummary(name="negative", blog=blog)
article.set_title("Utiliser le plugin negative de Compiz")
article.set_date("Avril 2017")
article.set_description("J'utilise Compiz et KDE, j'ai pas honte, et j'inverse les couleurs de mon écran.")
blog.add_article(article)

article = ArticleSummary(name="sw1", blog=blog)
article.set_title("Je vous donne la seule façon dont la guerre des étoiles peut continuer")
article.set_date("Mai 2017")
article.set_description("Le scénario de la guerre des étoiles 10-12")
blog.add_article(article)

article = ArticleSummary(name="cadeau", blog=blog)
article.set_title("Une idée cadeau")
article.set_date("Mai 2017")
article.set_description("Une idée de cadeau pour les grands, et peut-être pas les petits")
blog.add_article(article)

article = ArticleSummary(name="fridolulu", blog=blog)
article.set_title("Le Frido chez lulu.com")
article.set_date("Juin 2017")
article.set_description("Le Frido est en vente chez lulu.com et autres nouvelles du Frido")
blog.add_article(article)


article = ArticleSummary(name="journalisme", blog=blog)
article.set_title("Du journalisme comme je le déteste")
article.set_date("Juin 2017")
article.set_description("On se contente de remettre les paroles du vendeur entre guillemets, sans (se) poser de questions")
blog.add_article(article)

article = ArticleSummary(name="git_prefere", blog=blog)
article.set_title("Mes commandes git préférées")
article.set_date("Juillet 2017")
article.set_description("Les commandes git que j'utilise le plus souvent et mon organisation personnelle.")
blog.add_article(article)

article = ArticleSummary(name="financement_univ", blog=blog)
article.set_title("Faut-il mieux financer l'université ?")
article.set_date("Octobre 2017")
article.set_description("En ce qui me concerne, augmenter le financement des universités n'est pas ouvert à négociation.")
blog.add_article(article)

article = ArticleSummary(name="piste_cyclable", blog=blog)
article.set_title("Ne pas utiliser les pistes cyclables")
article.set_date("Mars 2018")
article.set_description("tl;dr : pourquoi le volant des voitures est à gauche ?")
blog.add_article(article)

article = ArticleSummary(name="energie_electricite", blog=blog)
article.set_title("Confusion entre énergie et électricité")
article.set_date("Avril 2018")
article.set_description("Comment l'âge de fer écrit un article entier qui ne signifie strictement rien en confondant énergie et électricité")
blog.add_article(article)

article = ArticleSummary(name="gilet_jaune", blog=blog)
article.set_title("Je suis le seul gilet jaune de Besançon")
article.set_date("Janvier 2019")
article.set_description("Un gilet jaune, ça sert aussi à être vu la nuit.")
blog.add_article(article)

article = ArticleSummary(name="frido_deploy", blog=blog)
article.set_title("Comment je copie le frido de mon ordinateur vers OVH")
article.set_date("Février 2019")
article.set_description("Utilisation de sftp")
blog.add_article(article)

article = ArticleSummary(name="mdp_chez_orange", blog=blog)
article.set_title("Sécurité des mots de passe chez Orange")
article.set_date("Février 2019")
article.set_description("Gestionnaire de mot de passe")
blog.add_article(article)

article = ArticleSummary(name="cnrs_frein_climat", blog=blog)
article.set_title("Le CNRS est un frein à l'action climatique")
article.set_date("Juillet 2019")
article.set_description("")
blog.add_article(article)

article = ArticleSummary(name="pole_emploi_pire_mot_de_passe", blog=blog)
article.set_title("Pôle emploi : le pire mot de passe")
article.set_date("Aout 2019")
article.set_description("")
blog.add_article(article)

article = ArticleSummary(name="pole_emploi_pire_mot_de_passe", blog=blog)
article.set_title("Pôle emploi : le pire mot de passe")
article.set_date("Aout 2019")
article.set_description("")
blog.add_article(article)

article = ArticleSummary(name="je_n_irai_pas_voter", blog=blog)
article.set_title("Je n'irai pas voter.")
article.set_date("Mars 2020")
article.set_description("")
blog.add_article(article)

article = ArticleSummary(name="liens_4", blog=blog)
article.set_title("Liens - 4")
article.set_date("Mai 2020")
article.set_description("Quelque liens en vrac")
blog.add_article(article)


blog.build()
