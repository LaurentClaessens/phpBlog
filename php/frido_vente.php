<?php
                require("../src/Article.php");

                $art=new Article("Le Frido est en vente");
                $art->set_date("Novembre 2016");
                $art->set_content_file("../html/frido_vente.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        