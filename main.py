from rich import print
from rich.prompt import Prompt
from rich.panel import Panel

from models.download import download_with_progress
from models.tools import print_banner, clear_terminal_screen
from models.messages import ShowNoticeMessage
from avamovie.scraper import AvaMovieScraper

movie_scraper = AvaMovieScraper()


def main() -> None:
    """
    Get the name of the movie and search it by scraper 
    and find the links to download the movie
    """

    movie_name = Prompt.ask(":sparkles: Enter Movie Name")

    ShowNoticeMessage.searching_message()

    search_results = movie_scraper.search_and_extract_data(movie_name)
    clear_terminal_screen()

    if not search_results:
        ShowNoticeMessage.nothing_found_message()
        quit()

    movies_link_page = dict()
    counter = 0
    for movie_name, movie_data in search_results.items():
        print(f"\n\t :movie_camera: {counter}. {movie_name}")
        movies_link_page[counter] = movie_data
        counter += 1

    choiced_link = int(Prompt.ask("\n :fire: pick one"))
    movie_informations = movies_link_page[choiced_link]

    ShowNoticeMessage.searching_for_links_message()

    download_links = movie_scraper.get_movie_download_links(
        movie_informations["movie_link"]
    )

    clear_terminal_screen()

    print(Panel(movie_informations["movie_discription"]))
    
    ls,sl = 0,[]
    for quality, download_link in download_links.items():
        print("\n:star2:",ls, quality, ":", download_link)
        sl.append(download_link)
        ls+=1
    
    choiced_link = int(Prompt.ask("\n :car: pick one to download"))
    
    clear_terminal_screen()
    
    download_with_progress(sl[choiced_link])
    
if __name__ == "__main__":
    clear_terminal_screen()
    print_banner()
    main()
