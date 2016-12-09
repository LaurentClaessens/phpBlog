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

require("Exceptions.php");

/*

The class 'article' represents an article in the blog. It is determined by its
title from which one can deduce its position in the flux (analysing the file
feed.xml) and its URL.

- $title_hook : is an hard-coded string that has to be replaced by the title
                in the <head>...</head>.
                See the line <title>ADD_HERE_YOUR_TITLE</title> in 
                "generic_head.src"



The layout of an article is :

- The main text ins insdide <div>class="maintext"</div>

            <div>class="maintext"
            TITRE
            date

            text
            </div>

- Some generic informations on the right inside <div class="sidebar"> ... </div>
  containing "Abonez-vous", précédent, suivant.


The varaibles that can change from one article to another are :
- the text itsef;
- the title
- the date
- the language (in <html lm::lang=...>)

The author writes an html file containing his text and the class 
`article` takes care of putting it inside  <div class="maintext"></div>

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
        $this->date=null;
    }

    function set_date($d) { $this->date=$d; }
    function get_date() { return $this->date;  }
    function get_lang() { return $this->lang;  }
    function get_title() { return $this->title; }
    
    function get_header()
        // return the code <head>...</head>, with the correct title.
        //
        // If the file 'generic_head.src' does not exists, the 'str_replace' 
        // function returns a 'count===0'. So the exception throwing works.
    {
        $generic_head = file_get_contents("generic_head.src");
        $count=null;
        $my_head = str_replace($this->title_hook,$this->get_title(),$generic_head,$count);
        if ($count!=1)
        {
            throw new GenericHeadException("You have $count occurences of '$this->title_hook' in the generic header.");
        }
        return $my_head;
    }
    function echo_header() 
    { 
        try
        {
            $head= $this->get_header(); 
        }
        catch (GenericHeadException $e)
        {
            $head="Problem with the header.".$e;
        }
        echo $head;
    }
    function echo_sidebar()
    {
        echo'
            <div class="sidebar">
            <ul>
                <li>
            <a href="http://laurent.claessens-donadello.eu/rss.xml">Abonnez-vous au RSS.</a> 
                </li>
                <li>
                    Précédent
                </li>
                <li>
                    Suivant
                </li>
            </ul>
        </div>';
    }
    function get_text()
    {
        return "<p>This is the text</p>";
    }
    function echo_body()
    // echoes the <body>...</body> part 
    {
        echo "<body>";
        echo '<div class="maintext">';
        echo "<h1>",$this->get_title(),"</h1>";

        echo "<small>",$this->get_date(),"</small>";

        echo $this->get_text();

        echo "</div>";
        echo $this->echo_sidebar();
        echo "</body>";
    }

    function echo_page()
    {
        echo "<html xmlns='http://www.w3.org/1999/xhtml' xml:lang=",$this->get_lang(),">";
        $this->echo_header();
        $this->echo_body();
        echo "</html>";
    }
    function echo_heu()
    {
        echo 'bonjour';
    }
}

?>            
