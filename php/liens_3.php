<?php
                require("../src/Article.php");

                $art=new Article("Liens - 3");
                $art->set_date("Février 2017");
                $art->set_content_file("../html/liens_3.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        