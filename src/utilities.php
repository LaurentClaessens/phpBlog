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



function slugify($t)
// Generate an URL-frinedly string from the sting $t.
// - $t is tipycally the title of an article.
// return a string that can (and will) be used as URL for the article.
// From :
// http://stackoverflow.com/questions/5222134/how-to-convert-a-nice-page-title-into-a-valid-url-string
{
$text = preg_replace('/[^\\pL0-9]+/u', '-', $t);
$text = trim($text, "-");
$text = iconv("utf-8", "us-ascii//TRANSLIT", $text);
$text = preg_replace('/[^-a-z0-9]+/i', '', $text);
$text = strtolower($text);
}

?>
