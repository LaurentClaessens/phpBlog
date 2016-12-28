<?php
                require("../src/Article.php");

                $art=new Article("Les duos qui font bien leur travail");
                $art->set_date("Décembre 2016");
                $art->set_content_file("../html/les_duos.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        