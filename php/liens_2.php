<?php
                require("../src/Article.php");

                $art=new Article("Liens - 2");
                $art->set_date("Novembre 2016");
                $art->set_content_file("../html/liens_2.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        