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


require("Article_Summary.php");

class RSS_Flux
    /* This class represents a RSS flux. It represents a RSS xml file of the form
     *
     <?xml version="1.0" encoding="utf-8"
    <rss version="2.0"> 
    <channel> 
        <title>Blog de Laurent Claessens</title> 
        <link>http://laurent.claessens-donadello.eu/feed</link> 
        <description>Mon blog personnel, tout fait à la main en Vim.</description>
            <item> 
                <title>A TITLE</title> 
                <link> LINK </link>
                <description>
                    SOME DESCRIPTION
                </description>
                <guid> OTHER LINK </guid> 
            </item>  
            <item>
                    and other article.
            </item>  
        </channel> 
    </rss>

    This class helps you to navigate in this particular structure.
 */
{

    function __constructor($xfn)
    {
        $this->xml_filename=xfn;
    }
    function get_xml_filename() { return $this->xml_filename; }
    function main_channel()
    {
        $xml=simplexml_load_file( $this->get_xml_filename  );
        return $xml->channel;
    }
    function article_list()
    // return a list (array) of articles under the form of
    // instances of `Article_Summary`.
    {
        $ans=array();
        foreach ($this->main_channel()->item as $i)
        {
            $title=$i->title;
            $url=$i->guid;

            $summary = Article_Summary();
            $summary->set_link($url);
            $summary->set_title($title);
            
            $ans[]=$summary;
        }
        return $ans;
    }
}

?>
