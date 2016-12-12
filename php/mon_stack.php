<?php
                require("../src/Article.php");

                $art=new Article("Mon stack");
                $art->set_date("Novembre 2016");
                $art->set_content_file("../html/mon_stack.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        