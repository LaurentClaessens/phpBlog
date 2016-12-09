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

class Article_Summary
    /* This class represents the summary of an article in a RSS flux.
     * title,link
     *
     * You do not need to instanciate this class since the class 'RSS_Flux'
     * provides you a list of articles summaries from an xml file.
    */
{
    function __constructor()
    {
        $this->title=null;
        $this->link=null;
    }
    function set_title($t) { $this->title=$t; }
    function set_link($l) { $this->link=$l; }
    function get_title()  { return $this->title; }
    function get_link()  { return $this->link; }
    
}

?>

