<?php
                require("../src/Article.php");

                $art=new Article("Présentation du Frido");
                $art->set_date("Octobre 2016");
                $art->set_content_file("../html/frido_presentation.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        