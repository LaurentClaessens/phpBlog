from ArticleSummary import ArticleSummary
from MdToBlogHtml import md_to_blog_html

article_list=[]
article_list.append(ArticleSummary(name="debootstrap"))
article_list[-1].set_title("Install Ubuntu with debootstrap")
article_list[-1].set_date("Octobre 2016")
article_list[-1].set_description("This is how I actually install my Ubutnu, using deboostrap.")
                

article_list.append(ArticleSummary(name="frido_presentation"))
article_list[-1].set_title("Présentation du Frido")
article_list[-1].set_date("Octobre 2016")
article_list[-1].set_description("Une courte présentation du Frido, un cours de mathématique destiné aux candidats à l'agrégation")
                

article_list.append(ArticleSummary(name="esperanto"))
article_list[-1].set_title("Pourquoi l'esperanto n'est pas le bonne solution ?")
article_list[-1].set_date("Octobre 2016")
article_list[-1].set_description("Une réponse définitive à la question du titre, qui mettre tout le monde d'accord.")
                

article_list.append(ArticleSummary(name="liens_1"))
article_list[-1].set_title("Liens - 1")
article_list[-1].set_date("Novembre 2016")
article_list[-1].set_description("Quelque liens intéressants")
                

article_list.append(ArticleSummary(name="frido_vente"))
article_list[-1].set_title("Le Frido est en vente")
article_list[-1].set_date("Novembre 2016")
article_list[-1].set_description("Le Frido est maintenat commercialisé, ce qui en fait un livre utilisable à l'agrégation.")
                
article_list.append(ArticleSummary(name="climat_et_technologie"))
article_list[-1].set_title("Climat et technologie")
article_list[-1].set_date("Novembre 2016")
article_list[-1].set_description("Il y a un petit paradoxe à croire en même temps au «problème» climatique et à une énorme accélération technologie pour les prochaines décennies. ")

article_list.append(ArticleSummary(name="facebook_ne_censure_pas"))
article_list[-1].set_title("Facebook ne censure pas")
article_list[-1].set_date("Novembre 2016")
article_list[-1].set_description("Non, Facebook ne censure pas. C'est juste un éditeur à bas coût qui vous fournit un travail de mauvaise qualité.")
                
article_list.append(ArticleSummary(name="liens_2"))
article_list[-1].set_title("Liens - 2")
article_list[-1].set_date("Novembre 2016")
article_list[-1].set_description("Quelque liens intéressants")
                
article_list.append(ArticleSummary(name="mon_stack"))
article_list[-1].set_title("Mon stack")
article_list[-1].set_date("Novembre 2016")
article_list[-1].set_description("Mon stack")

article_list.append(ArticleSummary(name="hollande_croissance"))
article_list[-1].set_title("Hollande n'a juste pas eu la croissance sur laquelle il comptait")
article_list[-1].set_date("Novembre 2016")
article_list[-1].set_description("François Hollande n'a pas eu la croissance économique sur laquelle il comptait. Et cela ne dépendait pas de lui. Je crois que tous les autres se seraient plantés de la même façon.")

article_list.append(ArticleSummary(name="meta"))
article_list[-1].set_title("Qu'est-ce que la méta programmation ?")
article_list[-1].set_date("Décembre 2016")
article_list[-1].set_description="Du code qui génère du code qui est interprété pour produire du code ..."

article_list.append(ArticleSummary(name="frido_liens"))
article_list[-1].set_title("Quelque liens parlant du Frido")
article_list[-1].set_date("Décembre 2016")
article_list[-1].set_description("Je me propose de tenir ici à jour une liste des sites qui parlent du Frido")

article_list.append(ArticleSummary(name="les_duos"))
article_list[-1].set_title("Les duos qui font bien leur travail")
article_list[-1].set_date("Décembre 2016")
article_list[-1].set_description("Quelque duos logiciels que j'utilise et qui font du bien")

article_list.append(ArticleSummary(name="terminal_terminator"))
article_list[-1].set_title("Changement de terminal : terminator")
article_list[-1].set_date("Janvier 2017")
article_list[-1].set_description("Pourquoi j'utilise Terminator au lieu de terminology")

article_list.append(ArticleSummary(name="ecriture_epicene"))
article_list[-1].set_title("Contre l'écriture épicène")
article_list[-1].set_date("Janvier 2017")
article_list[-1].set_description("Pourquoi le langage épicène renforce la discrimination.")

article_list.append(ArticleSummary(name="frido_recherche"))
article_list[-1].set_title("Des nouvelles du Frido")
article_list[-1].set_date("Février 2017")
article_list[-1].set_description("Quelque nouvelles du Frido")

article_list.append(ArticleSummary(name="liens_3"))
article_list[-1].set_title("Liens - 3")
article_list[-1].set_date("Février 2017")
article_list[-1].set_description("Quelque liens en vrac")

article_list.append(ArticleSummary(name="intro"))
article_list[-1].set_title("Mon blog en php")
article_list[-1].set_date("Février 2017")
article_list[-1].set_description("Quelque mots d'introduction")


article_list.append(ArticleSummary(name="itrf"))
article_list[-1].set_title("Comment créer ses dossiers ITRF ?")
article_list[-1].set_date("Avril 2017")
article_list[-1].set_description("Créer les dossiers ITRF demande de remplir plusieurs fichiers ODT contenant essentiellement la même chose. Comment faire sans duplication de code ?")
md_to_blog_html("html/itrf.md")

article_list.append(ArticleSummary(name="negative"))
article_list[-1].set_title("Utiliser le plugin negative de Compiz")
article_list[-1].set_date("Avril 2017")
article_list[-1].set_description("J'utilise Compiz et KDE, j'ai pas honte, et j'inverse les couleurs de mon écran.")
md_to_blog_html("html/negative.md")

article_list.append(ArticleSummary(name="sw1"))
article_list[-1].set_title("Je vous donne la seule façon dont la guerre des étoiles peut continuer")
article_list[-1].set_date("Mai 2017")
article_list[-1].set_description("Le scénario de la guerre des étoiles 10-12")
md_to_blog_html("html/sw1.md")

article_list.append(ArticleSummary(name="cadeau"))
article_list[-1].set_title("Une idée cadeau")
article_list[-1].set_date("Mai 2017")
article_list[-1].set_description("Une idée de cadeau pour les grands, et peut-être pas les petits")
md_to_blog_html("html/cadeau.md")

article_list.append(ArticleSummary(name="fridolulu"))
article_list[-1].set_title("Le Frido chez lulu.com")
article_list[-1].set_date("Juin 2017")
article_list[-1].set_description("Le Frido est en vente chez lulu.com et autres nouvelles du Frido")
md_to_blog_html("html/fridolulu.md")


article_list.append(ArticleSummary(name="journalisme"))
article_list[-1].set_title("Du journalisme comme je le déteste")
article_list[-1].set_date("Juin 2017")
article_list[-1].set_description("On se contente de remettre les paroles du vendeur entre guillemets, sans (se) poser de questions")
md_to_blog_html("html/journalisme.md")

article_list.append(ArticleSummary(name="git_prefere"))
article_list[-1].set_title("Mes commandes git préférées")
article_list[-1].set_date("Juillet 2017")
article_list[-1].set_description("Les commandes git que j'utilise le plus souvent et mon organisation personnelle.")
md_to_blog_html("html/git_prefere.md")

article_list.append(ArticleSummary(name="financement_univ"))
article_list[-1].set_title("Faut-il mieux financer l'université ?")
article_list[-1].set_date("Octobre 2017")
article_list[-1].set_description("En ce qui me concerne, augmenter le financement des universités n'est pas ouvert à négociation.")
md_to_blog_html("html/financement_univ.md")

article_list.append(ArticleSummary(name="piste_cyclable"))
article_list[-1].set_title("Ne pas utiliser les pistes cyclables")
article_list[-1].set_date("Mars 2018")
article_list[-1].set_description("tl;dr : pourquoi le volant des voitures est à gauche ?")
md_to_blog_html("html/piste_cyclable.md")

article_list.append(ArticleSummary(name="energie_electricite"))
article_list[-1].set_title("Confusion entre énergie et électricité")
article_list[-1].set_date("Avril 2018")
article_list[-1].set_description("Comment l'âge de fer écrit un article entier qui ne signifie strictement rien en confondant énergie et électricité")
md_to_blog_html("html/energie_electricite.md")

article_list.append(ArticleSummary(name="gilet_jaune"))
article_list[-1].set_title("Je suis le seul gilet jaune de Besançon")
article_list[-1].set_date("Janvier 2019")
article_list[-1].set_description("Un gilet jaune, ça sert aussi à être vu la nuit.")
md_to_blog_html("html/gilet_jaune.md")

article_list.append(ArticleSummary(name="frido_deploy"))
article_list[-1].set_title("Comment je copie le frido de mon ordinateur vers OVH")
article_list[-1].set_date("Février 2019")
article_list[-1].set_description("Utilisation de sftp")
md_to_blog_html("html/frido_deploy.md")

article_list.append(ArticleSummary(name="mdp_chez_orange"))
article_list[-1].set_title("Sécurité des mots de passe chez Orange")
article_list[-1].set_date("Février 2019")
article_list[-1].set_description("Gestionnaire de mot de passe")
md_to_blog_html("html/mdp_chez_orange.md")

article_list.append(ArticleSummary(name="cnrs_frein_climat"))
article_list[-1].set_title("Le CNRS est un frein à l'action climatique")
article_list[-1].set_date("Juillet 2019")
article_list[-1].set_description("")
md_to_blog_html("html/cnrs_frein_climat.md")

article_list.append(ArticleSummary(name="pole_emploi_pire_mot_de_passe"))
article_list[-1].set_title("Pôle emploi : le pire mot de passe")
article_list[-1].set_date("Aout 2019")
article_list[-1].set_description("")
md_to_blog_html("html/pole_emploi_pire_mot_de_passe.md")

article_list.append(ArticleSummary(name="pole_emploi_pire_mot_de_passe"))
article_list[-1].set_title("Pôle emploi : le pire mot de passe")
article_list[-1].set_date("Aout 2019")
article_list[-1].set_description("")
md_to_blog_html("html/pole_emploi_pire_mot_de_passe.md")

article_list.append(ArticleSummary(name="je_n_irai_pas_voter"))
article_list[-1].set_title("Je n'irai pas voter.")
article_list[-1].set_date("Mars 2020")
article_list[-1].set_description("")
md_to_blog_html("html/je_n_irai_pas_voter.md")

article_list.append(ArticleSummary(name="liens_4"))
article_list[-1].set_title("Liens - 4")
article_list[-1].set_date("Mai 2020")
article_list[-1].set_description("Quelque liens en vrac")
md_to_blog_html("html/liens_4.md")

# Je crois que le 'name' doit être le même que le nom du fichier md
