<?php
                require("../src/Article.php");

                $art=new Article("Install Ubuntu with debootstrap");
                $art->set_date("Octobre 2016");
                $art->set_content_file("../html/debootstrap.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        