<?php
                require("../src/Article.php");

                $art=new Article("Climat et technologie");
                $art->set_date("Novembre 2016");
                $art->set_content_file("../html/Climat_et_technoligie.html");
                $art->set_surrounding_flux("../rss.xml");
                $art->echo_page();
                ?>            
        