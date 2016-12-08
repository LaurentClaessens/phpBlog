<?php
/*
Copyright Laurent Claessens
contact : laurent@claessens-donadello.eu

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
//*/

/*

The class 'article' represents an article in the blog. It is determined by its
title from which one can deduce its position in the flux (analysing the file
feed.xml) and its URL.

- $title_hook : is an hard-coded string that has to be replaced by the title
                in the <head>...</head>.
                See the line <title>ADD_HERE_YOUR_TITLE</title> in 
                "generic_head.src"

//*/


class article
{
    var $title;
    var $lang;
    var $title_hook = "ADD_HERE_YOUR_TITLE"; // hard-coded in 'generic_head.src'

    function __construct($t,$l="fr")
        // - $t (string) : the title of the article to be inserted in
        //    <title>...</title>
        // - $l (string) : the language to be included in
        //    <html xml:lang=... > </html>
    {
        $this->title=$t;
        $this->lang=$l;
    }
    
    function get_header()
        // return the code <head>...</head>, with the correct title.
    {
        $generic_head = file_get_contents("generic_head.src");
        $count=null;
        $my_head = str_replace($this->title_hook,$this->get_title(),$generic_head,$count);
        if ($count!=1)
        {
            throw new Exception("You have $count occurences of '$this->title_hook' in the generic header.");
        }
        return $my_head;
    }

    function get_title() { return $this->title; }
    
}
?>            
