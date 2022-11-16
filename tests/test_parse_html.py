from scrapper_parser import parse_html

video1 = parse_html("3cIObgePakE")
video2 = parse_html("G02QEhmleYA")
video3 = parse_html("fmsoym8I-3o")

def test_parse_html_return():
        # Test if the function returns a dict
        assert type(video1) == dict

def test_parse_html_title():
        # Test if the function returns the right title
        assert video1["title"] == 'Alpha Wann & Népal - De 0 à 100'

def test_parse_html_author():
        # Test if the function returns the right author
        assert video1["author"] == 'Radio Sergio'

def test_parse_html_likes():
        # Test if the function returns the right number of likes
        assert video1["likes"] == "15875"

def test_parse_html_empty_description():
        # Test if the function returns the right description
        assert video1["description"] == "Pas de description"

def test_parse_html_empty_links():
        # Test if the function returns the right links
        assert video1["links"] == []

def test_parse_html_id():
        # Test if the function returns the right id
        assert video1["id"] == "3cIObgePakE"

def test_parse_html_title2():
        assert video2["title"] == 'Luv Resval | Grünt #45'

def test_parse_html_desc2():
        assert video2["description"] == "Nous nous excusons pour la publicité. Il arrive que les ayants droits nous l'imposent, et nous ne parvenons pas toujours à la faire retirer. \\nNous ne monétisons pas notre chaîne YouTube.\\n\\n\\nGrünt Radio : https://linktr.ee/Grunt​\\nhttps://www.instagram.com/gruntluv​\\nhttp://facebook.com/gruntmag​\\nhttp://www.gruntmag.com"

def test_parse_html_links2():
        assert video2["links"] == [
                "https://linktr.ee/Grunt",
                "https://www.instagram.com/gruntluv",
                "http://facebook.com/gruntmag",
                "http://www.gruntmag.com/"
        ]

def test_parse_html_timestamp():
        assert video3["links"] == [
                "https://youtube.com/watch?v=fmsoym8I-3o&t=0s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=22s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=212s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=611s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=849s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=1048s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=1210s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=1393s",
                "https://youtube.com/watch?v=fmsoym8I-3o&t=2362s"
        ]

test_parse_html_return()
test_parse_html_title()
test_parse_html_author()
test_parse_html_likes()
test_parse_html_empty_description()
test_parse_html_empty_links()
test_parse_html_id()
test_parse_html_title2()
test_parse_html_desc2()
test_parse_html_links2()
