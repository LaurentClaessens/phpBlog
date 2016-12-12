<?php
                require("../src/Article.php");

                $art=new Article("Facebook ne censure pas");
                $art->set_date("Novembre 2016");
                $art->set_content_file("../html/facebook_ne_censure_pas.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        