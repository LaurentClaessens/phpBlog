<?php
                require("../src/Article.php");

                $art=new Article("Quelque liens parlant du Frido");
                $art->set_date("Décembre 2016");
                $art->set_content_file("../html/frido_liens.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        