<? php
                require("src/Article.php");

                $art=new Article("Qu'est-ce que la méta programmation ?");
                $art->set_date("Décembre 2016");
                $art->set_content_file("../html/meta.html");
                $art->set_surrounding_flux("Trss.xml");
                $art->echo_page();
                ?>            
        