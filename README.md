# PSN-discount-scraper

PSN-discount-scraper is a simple program to scrap (collect) and sort all discount games within a threshold in Playstation store.

For more detail, please check out my output file in `example` folder

## Instructions

1.&nbsp;First download the folder (or the `psn_scraper_app`)

2.&nbsp;Open up your terminal (MacOS/Linux) and access the downloaded folder.

3.&nbsp;Simply run the app by run this command in your terminal:

```bash
./psn_scraper_app
```

By default the discount value is 70% (so the program will find games with greater or equal 70% discount).

Or you can define the number by yourself by adding a 0 - 100 number in front.

```bash
# greater or equal to 50% discount games
./psn_scraper_app 50
```

4.&nbsp;Wait for about 10 mins (may vary based on your connection speed) until the program is exited

5.&nbsp;The output will be written in `discount_game_list.txt`

## [Dev] Installation

Create python's virtual environment, then activate it

```bash
virtualenv .env
source .env/bin/activate
```

Install requirements

```bash
pip3 install -r requirements.txt
```

Run the program

```bash
python3 app.py
```

## Disclaimer

This is just a tool to help people (personally me) to find discount games easier in Playstation store.
