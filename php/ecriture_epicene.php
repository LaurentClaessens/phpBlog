<?php
                require("../src/Article.php");

                $art=new Article("Contre l'écriture épicène");
                $art->set_date("Janvier 2017");
                $art->set_content_file("../html/ecriture_epicene.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        