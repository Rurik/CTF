rule valid_gif : valid_gif
{
        strings:

                        $header = {47 49 46 38 39 61 }
                        $trailer = /\x3B$/ 

        condition:
                        $header at 0 and $trailer
}

rule valid_gif : valid_gif { strings: $header = {47 49 46 38 39 61 } $trailer = /\x3B$/ condition: $header at 0 and $trailer }