<?php
                require("../src/Article.php");

                $art=new Article("Hollande n'a juste pas eu la croissance sur laquelle il comptait");
                $art->set_date("Novembre 2016");
                $art->set_content_file("../html/hollande_croissance.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        