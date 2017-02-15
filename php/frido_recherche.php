<?php
                require("../src/Article.php");

                $art=new Article("Des nouvelles du Frido");
                $art->set_date("Février 2017");
                $art->set_content_file("../html/frido_recherche.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        