<?php
                require("../src/Article.php");

                $art=new Article("Changement de terminal : terminator");
                $art->set_date("Janvier 2017");
                $art->set_content_file("../html/terminal_terminator.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        