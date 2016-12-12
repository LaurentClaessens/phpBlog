<?php
                require("../src/Article.php");

                $art=new Article("Pourquoi l'esperanto n'est pas le bonne solution ?");
                $art->set_date("Octobre 2016");
                $art->set_content_file("../html/esperanto.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        