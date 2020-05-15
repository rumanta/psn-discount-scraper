import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

PSN_BASE_URL = 'https://store.playstation.com/'
PSN_STORE_GAMES_URL = 'https://store.playstation.com/en-id/grid/STORE-MSF86012-GAMESALL/'
LAST_PAGE_NUM = 156
MINIMUM_DISCOUNT_THRESHOLD = 70
REQUEST_TIMEOUT = 15


def get_game_price(section):
    game_link = (
        PSN_BASE_URL + section.find('a', href=True, class_='internal-app-link ember-view')['href']
    )
    title_section = section.find('div', class_='grid-cell__title')
    title_text = title_section.find('span').text
    body_section = section.find('div', class_='grid-cell__footer')

    price_before_text = 0
    price_after_text = 0

    price_before_elem = body_section.find('h3', class_='price-display__price')
    price_after_elem = body_section.find('div', class_='price-display__price--is-plus-upsell')

    if price_after_elem:
        # if PSN plus discount is active
        price_before_text = price_before_elem.text
        price_after_text = price_after_elem.text
    else:
        price_before_text = (
            body_section.find('span', class_='price-display__strikethrough')
            .find('div', class_='price')
            .text
        )
        price_after_text = price_before_elem.text

    return title_text, game_link, price_before_text, price_after_text


def game_metadata_printer(title_text, game_link, discount, price_before_text, price_after_text):
    print(title_text)
    print(game_link)
    print(f'discount: {discount}%')
    print(f'price before: {price_before_text}')
    print(f'price after: {price_after_text}')
    print('\n')


def game_metadata_writer(f, game_data):
    f.write(f"{game_data['title']}\n")
    f.write(f"{game_data['link']}\n")
    f.write(f"discount: {game_data['discount']}%\n")
    f.write(f"price before: {game_data['price_before']}\n")
    f.write(f"price after: {game_data['price_after']}\n")
    f.write('\n\n')


def write_sorted_discount_game(discount_games):
    sorted_discount_games = sorted(discount_games, key=lambda game: game['discount'], reverse=True)
    f = open('discount_game_list.txt', 'w')
    f.write(
        f"PSN Discount Game List\ndate and time: {datetime.now().strftime('%m/%d/%Y - %H:%M:%S')}\n\n"
    )
    [game_metadata_writer(f, game_data) for game_data in sorted_discount_games]
    f.close()


def main():
    discount_games = []

    for index_page in range(1, LAST_PAGE_NUM + 1):
        print('Accessing page', index_page)
        try:
            page = requests.get(f'{PSN_STORE_GAMES_URL}{index_page}', timeout=REQUEST_TIMEOUT)
        except:
            print(
                'ERROR: Request timeout reached, please check your internet connection or maybe PSN store is currently unaccessible'
            )
            break
        soup = BeautifulSoup(page.content, 'html.parser')
        results = soup.find(id='main')
        game_sections = results.find_all('div', class_='grid-cell grid-cell--game')

        for section in game_sections:
            discount_tag = section.find('span', class_='discount-badge__message')
            if not discount_tag:
                continue

            discount_numbers = re.findall(r'\d+', discount_tag.text)
            discount = int(discount_numbers[0]) if len(discount_numbers) > 0 else -1
            if discount >= MINIMUM_DISCOUNT_THRESHOLD:
                title_text, game_link, price_before_text, price_after_text = get_game_price(section)

                # Uncomment this if you want to print the game info
                # game_metadata_printer(
                #     title_text, game_link, discount, price_before_text, price_after_text
                # )
                game_data = {
                    'title': title_text,
                    'link': game_link,
                    'discount': discount,
                    'price_before': price_before_text,
                    'price_after': price_after_text,
                }
                discount_games.append(game_data)

    write_sorted_discount_game(discount_games)


if __name__ == '__main__':
    main()
