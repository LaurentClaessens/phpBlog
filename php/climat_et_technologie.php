<?php
                require("../src/Article.php");

                $art=new Article("Climat et technologie");
                $art->set_date("Novembre 2016");
                $art->set_content_file("../html/climat_et_technologie.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        